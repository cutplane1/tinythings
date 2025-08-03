from PySide6 import QtWidgets
from PySide6.QtWidgets import QLabel, QLineEdit, QVBoxLayout
from uigen import Ui_MainWindow
from shared import Game
import os
from PySide6 import QtCore

from PySide6.QtCore import QThread, Signal
from shared import Game
from agent import GameGenAgent

html_temp = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <script type="importmap">
{
  "imports": {
    "three": "https://cdn.jsdelivr.net/npm/three@<version>/build/three.module.js",
    "three/addons/": "https://cdn.jsdelivr.net/npm/three@<version>/examples/jsm/"
  }
}
</script>
</head>
<body>
"""

from enum import Enum


class GenProgress(Enum):
    DETAILS = 1
    CODE = 2
    ERROR = 3


class GenWorker(QThread):
    progress = Signal(int)
    dcode = Signal(str)

    def __init__(self, agent):
        super().__init__()
        self.agent = agent

    def run(self):
        try:
            print("Details generation started")
            self.progress.emit(GenProgress.DETAILS.value)
            self.agent.generate_details()
            print("Code generation started")
            print("details:", self.agent.details)
            self.progress.emit(GenProgress.CODE.value)
            self.agent.generate_code()
        except Exception as e:
            print(f"Error during code generation: {e}")
            self.progress.emit(GenProgress.ERROR.value)
            return
        self.dcode.emit(self.agent.code)
        return


class GenerationWidget(QtWidgets.QWidget):
    def __init__(self, game: Game, api_token, model_name):
        super().__init__()
        self.game = game
        self.model_name = model_name

        self.thread = None
        self.ai_agent = GameGenAgent(game)
        self.ai_agent.api_token = api_token
        self.ai_agent.model = model_name
        self.ai_agent.language = "english"

        self.setWindowTitle("generation in progress")

        self.label = QtWidgets.QLabel("generating...")
        self.progress = QtWidgets.QProgressBar()
        self.progress.setRange(0, 0)
        self.progress.setTextVisible(False)

        layout = QtWidgets.QVBoxLayout(self)
        layout.addWidget(self.label, alignment=QtCore.Qt.AlignCenter)
        layout.addWidget(self.progress)

        self.setMinimumSize(220, 80)

    def start(self):
        print("Starting generation...")
        self.thread = GenWorker(self.ai_agent)
        self.thread.progress.connect(self.on_progress)
        self.thread.dcode.connect(self.done)
        self.thread.start()

    def on_progress(self, val):
        if val == GenProgress.DETAILS.value:
            self.label.setText("generating details...")
        elif val == GenProgress.CODE.value:
            self.label.setText("generating code...")
        elif val == GenProgress.ERROR.value:
            self.label.setText("error during generation, check console for details")
            self.progress.setRange(0, 1)
            self.progress.setValue(1)
            return

    def done(self, code):
        c = html_temp + code + "</body></html>"
        with open(
            os.path.join(
                self.game.folder_to_save, self.game.name.replace(" ", "") + ".html"
            ),
            "w",
        ) as f:
            f.write(c)

        self.label.setText(
            "done! you can find your game in the folder: " + self.game.folder_to_save
        )
        self.progress.setRange(0, 1)
        self.progress.setValue(1)

    def closeEvent(self, event):
        QtWidgets.QApplication.quit()


class TokenSettings(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Token Settings")

        self.api_token_label = QLabel("API TOKEN:")
        self.api_token_input = QLineEdit(text="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")

        self.model_name_label = QLabel("MODEL NAME (LiteLLM):")
        self.model_name_input = QLineEdit(text="openrouter/moonshotai/kimi-k2:free")

        layout = QVBoxLayout(self)
        layout.addWidget(self.api_token_label)
        layout.addWidget(self.api_token_input)
        layout.addWidget(self.model_name_label)
        layout.addWidget(self.model_name_input)


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.settings_window = TokenSettings()
        self.generation_window = None
        self.setupUi(self)
        self.file_picker.clicked.connect(self.file_pick)
        self.create_b.clicked.connect(self.create_button_action)
        self.token_settings.triggered.connect(self.settings)

    def file_pick(self):
        folder = QtWidgets.QFileDialog.getExistingDirectory(self, "Select Folder")
        if folder:
            self.path.setText(folder)

    def collect_info_from_ui(self) -> Game:
        name = self.name.text()

        genres = []
        for i in range(self.genre.count()):
            widget_1 = self.genre.itemAt(i).widget()
            widget_2 = self.genre_2.itemAt(i).widget()
            if widget_1.isChecked():
                genres.append(widget_1.text())
            if widget_2.isChecked():
                genres.append(widget_2.text())

        optimization_level = str(int(self.optimization_slider.value()) * 25) + "%"

        features = []
        for i in range(self.features.count()):
            widget_1 = self.features.itemAt(i).widget()
            widget_2 = self.features_2.itemAt(i).widget()
            if widget_1.isChecked():
                features.append(widget_1.text())
            if widget_2.isChecked():
                features.append(widget_2.text())

        folder_to_save = self.path.text()

        game = Game(
            name=name,
            genres=genres,
            optimization_level=optimization_level,
            features=features,
            folder_to_save=folder_to_save,
        )

        return game
        # return generate_game_prompt(game)

    def create_button_action(self):
        if self.settings_window.api_token_input.text() == "":
            QtWidgets.QMessageBox.warning(
                self, "Error", "Please enter your API token in the settings."
            )
            return
        self.create_b.setEnabled(False)
        game = self.collect_info_from_ui()
        self.generation_window = GenerationWidget(
            game,
            self.settings_window.api_token_input.text(),
            self.settings_window.model_name_input.text(),
        )
        self.generation_window.show()
        self.generation_window.start()
        self.hide()

    def settings(self):
        self.settings_window.show()


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    main_window = MainWindow()
    main_window.show()
    app.exec()
