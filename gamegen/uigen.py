# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QMenu,
    QMenuBar, QPushButton, QSizePolicy, QSlider,
    QTabWidget, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(402, 627)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setTabShape(QTabWidget.TabShape.Rounded)
        self.token_settings = QAction(MainWindow)
        self.token_settings.setObjectName(u"token_settings")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.genre_fr = QFrame(self.centralwidget)
        self.genre_fr.setObjectName(u"genre_fr")
        self.genre_fr.setGeometry(QRect(10, 50, 381, 201))
        self.genre_fr.setAutoFillBackground(False)
        self.genre_fr.setFrameShape(QFrame.Shape.Panel)
        self.genre_fr.setFrameShadow(QFrame.Shadow.Sunken)
        self.label = QLabel(self.genre_fr)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(170, 0, 49, 16))
        self.verticalLayoutWidget = QWidget(self.genre_fr)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 10, 160, 192))
        self.genre = QVBoxLayout(self.verticalLayoutWidget)
        self.genre.setObjectName(u"genre")
        self.genre.setContentsMargins(0, 0, 0, 0)
        self.checkBox_3 = QCheckBox(self.verticalLayoutWidget)
        self.checkBox_3.setObjectName(u"checkBox_3")

        self.genre.addWidget(self.checkBox_3)

        self.checkBox = QCheckBox(self.verticalLayoutWidget)
        self.checkBox.setObjectName(u"checkBox")

        self.genre.addWidget(self.checkBox)

        self.checkBox_2 = QCheckBox(self.verticalLayoutWidget)
        self.checkBox_2.setObjectName(u"checkBox_2")

        self.genre.addWidget(self.checkBox_2)

        self.checkBox_6 = QCheckBox(self.verticalLayoutWidget)
        self.checkBox_6.setObjectName(u"checkBox_6")

        self.genre.addWidget(self.checkBox_6)

        self.checkBox_5 = QCheckBox(self.verticalLayoutWidget)
        self.checkBox_5.setObjectName(u"checkBox_5")

        self.genre.addWidget(self.checkBox_5)

        self.checkBox_4 = QCheckBox(self.verticalLayoutWidget)
        self.checkBox_4.setObjectName(u"checkBox_4")

        self.genre.addWidget(self.checkBox_4)

        self.checkBox_7 = QCheckBox(self.verticalLayoutWidget)
        self.checkBox_7.setObjectName(u"checkBox_7")

        self.genre.addWidget(self.checkBox_7)

        self.verticalLayoutWidget_5 = QWidget(self.genre_fr)
        self.verticalLayoutWidget_5.setObjectName(u"verticalLayoutWidget_5")
        self.verticalLayoutWidget_5.setGeometry(QRect(220, 10, 151, 192))
        self.genre_2 = QVBoxLayout(self.verticalLayoutWidget_5)
        self.genre_2.setObjectName(u"genre_2")
        self.genre_2.setContentsMargins(0, 0, 0, 0)
        self.checkBox_13 = QCheckBox(self.verticalLayoutWidget_5)
        self.checkBox_13.setObjectName(u"checkBox_13")

        self.genre_2.addWidget(self.checkBox_13)

        self.checkBox_14 = QCheckBox(self.verticalLayoutWidget_5)
        self.checkBox_14.setObjectName(u"checkBox_14")

        self.genre_2.addWidget(self.checkBox_14)

        self.checkBox_15 = QCheckBox(self.verticalLayoutWidget_5)
        self.checkBox_15.setObjectName(u"checkBox_15")

        self.genre_2.addWidget(self.checkBox_15)

        self.checkBox_16 = QCheckBox(self.verticalLayoutWidget_5)
        self.checkBox_16.setObjectName(u"checkBox_16")

        self.genre_2.addWidget(self.checkBox_16)

        self.checkBox_17 = QCheckBox(self.verticalLayoutWidget_5)
        self.checkBox_17.setObjectName(u"checkBox_17")

        self.genre_2.addWidget(self.checkBox_17)

        self.checkBox_18 = QCheckBox(self.verticalLayoutWidget_5)
        self.checkBox_18.setObjectName(u"checkBox_18")

        self.genre_2.addWidget(self.checkBox_18)

        self.checkBox_19 = QCheckBox(self.verticalLayoutWidget_5)
        self.checkBox_19.setObjectName(u"checkBox_19")

        self.genre_2.addWidget(self.checkBox_19)

        self.optimization = QFrame(self.centralwidget)
        self.optimization.setObjectName(u"optimization")
        self.optimization.setGeometry(QRect(10, 260, 381, 71))
        self.optimization.setFrameShape(QFrame.Shape.Panel)
        self.optimization.setFrameShadow(QFrame.Shadow.Sunken)
        self.verticalLayoutWidget_2 = QWidget(self.optimization)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(10, 20, 361, 53))
        self.optimization_l = QVBoxLayout(self.verticalLayoutWidget_2)
        self.optimization_l.setSpacing(6)
        self.optimization_l.setObjectName(u"optimization_l")
        self.optimization_l.setContentsMargins(0, 0, 0, 0)
        self.optimization_slider = QSlider(self.verticalLayoutWidget_2)
        self.optimization_slider.setObjectName(u"optimization_slider")
        self.optimization_slider.setMaximum(4)
        self.optimization_slider.setSingleStep(1)
        self.optimization_slider.setPageStep(1)
        self.optimization_slider.setValue(0)
        self.optimization_slider.setTracking(False)
        self.optimization_slider.setOrientation(Qt.Orientation.Horizontal)
        self.optimization_slider.setInvertedAppearance(False)
        self.optimization_slider.setInvertedControls(False)
        self.optimization_slider.setTickPosition(QSlider.TickPosition.TicksBelow)
        self.optimization_slider.setTickInterval(1)

        self.optimization_l.addWidget(self.optimization_slider)

        self.percent_l = QHBoxLayout()
        self.percent_l.setObjectName(u"percent_l")
        self.zero = QLabel(self.verticalLayoutWidget_2)
        self.zero.setObjectName(u"zero")

        self.percent_l.addWidget(self.zero)

        self.fifty = QLabel(self.verticalLayoutWidget_2)
        self.fifty.setObjectName(u"fifty")

        self.percent_l.addWidget(self.fifty)

        self.one_hundred = QLabel(self.verticalLayoutWidget_2)
        self.one_hundred.setObjectName(u"one_hundred")

        self.percent_l.addWidget(self.one_hundred)


        self.optimization_l.addLayout(self.percent_l)

        self.label_5 = QLabel(self.optimization)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(150, 0, 81, 16))
        self.features_fr = QFrame(self.centralwidget)
        self.features_fr.setObjectName(u"features_fr")
        self.features_fr.setGeometry(QRect(10, 340, 381, 151))
        self.features_fr.setFrameShape(QFrame.Shape.Panel)
        self.features_fr.setFrameShadow(QFrame.Shadow.Sunken)
        self.features_l = QLabel(self.features_fr)
        self.features_l.setObjectName(u"features_l")
        self.features_l.setGeometry(QRect(160, 0, 49, 16))
        self.verticalLayoutWidget_3 = QWidget(self.features_fr)
        self.verticalLayoutWidget_3.setObjectName(u"verticalLayoutWidget_3")
        self.verticalLayoutWidget_3.setGeometry(QRect(10, 20, 172, 136))
        self.features = QVBoxLayout(self.verticalLayoutWidget_3)
        self.features.setObjectName(u"features")
        self.features.setContentsMargins(0, 0, 0, 0)
        self.checkBox_10 = QCheckBox(self.verticalLayoutWidget_3)
        self.checkBox_10.setObjectName(u"checkBox_10")

        self.features.addWidget(self.checkBox_10)

        self.checkBox_11 = QCheckBox(self.verticalLayoutWidget_3)
        self.checkBox_11.setObjectName(u"checkBox_11")

        self.features.addWidget(self.checkBox_11)

        self.checkBox_8 = QCheckBox(self.verticalLayoutWidget_3)
        self.checkBox_8.setObjectName(u"checkBox_8")

        self.features.addWidget(self.checkBox_8)

        self.checkBox_9 = QCheckBox(self.verticalLayoutWidget_3)
        self.checkBox_9.setObjectName(u"checkBox_9")

        self.features.addWidget(self.checkBox_9)

        self.checkBox_12 = QCheckBox(self.verticalLayoutWidget_3)
        self.checkBox_12.setObjectName(u"checkBox_12")

        self.features.addWidget(self.checkBox_12)

        self.verticalLayoutWidget_6 = QWidget(self.features_fr)
        self.verticalLayoutWidget_6.setObjectName(u"verticalLayoutWidget_6")
        self.verticalLayoutWidget_6.setGeometry(QRect(180, 20, 201, 136))
        self.features_2 = QVBoxLayout(self.verticalLayoutWidget_6)
        self.features_2.setObjectName(u"features_2")
        self.features_2.setContentsMargins(0, 0, 0, 0)
        self.checkBox_20 = QCheckBox(self.verticalLayoutWidget_6)
        self.checkBox_20.setObjectName(u"checkBox_20")

        self.features_2.addWidget(self.checkBox_20)

        self.checkBox_21 = QCheckBox(self.verticalLayoutWidget_6)
        self.checkBox_21.setObjectName(u"checkBox_21")

        self.features_2.addWidget(self.checkBox_21)

        self.checkBox_22 = QCheckBox(self.verticalLayoutWidget_6)
        self.checkBox_22.setObjectName(u"checkBox_22")

        self.features_2.addWidget(self.checkBox_22)

        self.checkBox_23 = QCheckBox(self.verticalLayoutWidget_6)
        self.checkBox_23.setObjectName(u"checkBox_23")

        self.features_2.addWidget(self.checkBox_23)

        self.checkBox_24 = QCheckBox(self.verticalLayoutWidget_6)
        self.checkBox_24.setObjectName(u"checkBox_24")

        self.features_2.addWidget(self.checkBox_24)

        self.horizontalLayoutWidget_2 = QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(10, 10, 381, 31))
        self.game_name = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.game_name.setObjectName(u"game_name")
        self.game_name.setContentsMargins(0, 0, 0, 0)
        self.name_label = QLabel(self.horizontalLayoutWidget_2)
        self.name_label.setObjectName(u"name_label")

        self.game_name.addWidget(self.name_label)

        self.name = QLineEdit(self.horizontalLayoutWidget_2)
        self.name.setObjectName(u"name")

        self.game_name.addWidget(self.name)

        self.horizontalLayoutWidget_3 = QWidget(self.centralwidget)
        self.horizontalLayoutWidget_3.setObjectName(u"horizontalLayoutWidget_3")
        self.horizontalLayoutWidget_3.setGeometry(QRect(10, 500, 381, 31))
        self.game_save = QHBoxLayout(self.horizontalLayoutWidget_3)
        self.game_save.setObjectName(u"game_save")
        self.game_save.setContentsMargins(0, 0, 0, 0)
        self.save_to_folder = QLabel(self.horizontalLayoutWidget_3)
        self.save_to_folder.setObjectName(u"save_to_folder")

        self.game_save.addWidget(self.save_to_folder)

        self.path = QLineEdit(self.horizontalLayoutWidget_3)
        self.path.setObjectName(u"path")

        self.game_save.addWidget(self.path)

        self.file_picker = QPushButton(self.horizontalLayoutWidget_3)
        self.file_picker.setObjectName(u"file_picker")
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.FolderOpen))
        self.file_picker.setIcon(icon)

        self.game_save.addWidget(self.file_picker)

        self.create_b = QPushButton(self.centralwidget)
        self.create_b.setObjectName(u"create_b")
        self.create_b.setGeometry(QRect(10, 540, 381, 51))
        font = QFont()
        font.setFamilies([u"Comic Sans MS"])
        font.setPointSize(28)
        font.setBold(True)
        self.create_b.setFont(font)
        self.create_b.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 0, 0, 255), stop:0.166 rgba(255, 255, 0, 255), stop:0.333 rgba(0, 255, 0, 255), stop:0.5 rgba(0, 255, 255, 255), stop:0.666 rgba(0, 0, 255, 255), stop:0.833 rgba(255, 0, 255, 255), stop:1 rgba(255, 0, 0, 255))")
        self.create_b.setCheckable(False)
        self.create_b.setFlat(False)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 402, 22))
        self.menu_P = QMenu(self.menubar)
        self.menu_P.setObjectName(u"menu_P")
        MainWindow.setMenuBar(self.menubar)
        QWidget.setTabOrder(self.name, self.checkBox_3)
        QWidget.setTabOrder(self.checkBox_3, self.checkBox)
        QWidget.setTabOrder(self.checkBox, self.checkBox_2)
        QWidget.setTabOrder(self.checkBox_2, self.checkBox_6)
        QWidget.setTabOrder(self.checkBox_6, self.checkBox_5)
        QWidget.setTabOrder(self.checkBox_5, self.checkBox_4)
        QWidget.setTabOrder(self.checkBox_4, self.checkBox_7)
        QWidget.setTabOrder(self.checkBox_7, self.optimization_slider)
        QWidget.setTabOrder(self.optimization_slider, self.checkBox_10)
        QWidget.setTabOrder(self.checkBox_10, self.checkBox_11)
        QWidget.setTabOrder(self.checkBox_11, self.checkBox_8)
        QWidget.setTabOrder(self.checkBox_8, self.checkBox_9)
        QWidget.setTabOrder(self.checkBox_9, self.checkBox_12)
        QWidget.setTabOrder(self.checkBox_12, self.path)
        QWidget.setTabOrder(self.path, self.file_picker)
        QWidget.setTabOrder(self.file_picker, self.create_b)

        self.menubar.addAction(self.menu_P.menuAction())
        self.menu_P.addAction(self.token_settings)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u0413\u0435\u043d\u0435\u0440\u0430\u0442\u043e\u0440 \u0438\u0433\u0440 v0.01", None))
        self.token_settings.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438 \u0442\u043e\u043a\u0435\u043d\u043e\u0432", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0416\u0430\u043d\u0440:", None))
        self.checkBox_3.setText(QCoreApplication.translate("MainWindow", u"FPS", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043b\u0430\u0442\u0444\u043e\u0440\u043c\u0435\u0440", None))
        self.checkBox_2.setText(QCoreApplication.translate("MainWindow", u"RTS", None))
        self.checkBox_6.setText(QCoreApplication.translate("MainWindow", u"Rouge-Like", None))
        self.checkBox_5.setText(QCoreApplication.translate("MainWindow", u"\u041c\u0443\u043b\u044c\u0442\u0438\u043f\u043b\u0435\u0435\u0440", None))
        self.checkBox_4.setText(QCoreApplication.translate("MainWindow", u"RPG", None))
        self.checkBox_7.setText(QCoreApplication.translate("MainWindow", u"Battle Royale", None))
        self.checkBox_13.setText(QCoreApplication.translate("MainWindow", u"\u0425\u043e\u0440\u0440\u043e\u0440", None))
        self.checkBox_14.setText(QCoreApplication.translate("MainWindow", u"\u0410\u0440\u043a\u0430\u0434\u0430", None))
        self.checkBox_15.setText(QCoreApplication.translate("MainWindow", u"Extraction Shooter", None))
        self.checkBox_16.setText(QCoreApplication.translate("MainWindow", u"Hack and Slash", None))
        self.checkBox_17.setText(QCoreApplication.translate("MainWindow", u"\u0413\u043e\u043b\u043e\u0432\u043e\u043b\u043e\u043c\u043a\u0430", None))
        self.checkBox_18.setText(QCoreApplication.translate("MainWindow", u"Gacha", None))
        self.checkBox_19.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0438\u043c\u0443\u043b\u044f\u0442\u043e\u0440", None))
        self.zero.setText(QCoreApplication.translate("MainWindow", u"0%", None))
        self.fifty.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">50%</p></body></html>", None))
        self.one_hundred.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"right\">100%</p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u041e\u043f\u0442\u0438\u043c\u0438\u0437\u0430\u0446\u0438\u044f", None))
        self.features_l.setText(QCoreApplication.translate("MainWindow", u"\u0424\u0438\u0447\u0438:", None))
        self.checkBox_10.setText(QCoreApplication.translate("MainWindow", u"\u041a\u0440\u0443\u0442\u0430\u044f \u0444\u0438\u0437\u0438\u043a\u0430", None))
        self.checkBox_11.setText(QCoreApplication.translate("MainWindow", u"\u041a\u0440\u0443\u0442\u0430\u044f \u0433\u0440\u0430\u0444\u0438\u043a\u0430", None))
        self.checkBox_8.setText(QCoreApplication.translate("MainWindow", u"Raytracing", None))
        self.checkBox_9.setText(QCoreApplication.translate("MainWindow", u"DLSS", None))
        self.checkBox_12.setText(QCoreApplication.translate("MainWindow", u"\u041c\u043e\u0436\u043d\u043e \u0433\u0440\u0430\u0431\u0438\u0442\u044c \u043a\u043e\u0440\u043e\u0432\u0430\u043d\u044b", None))
        self.checkBox_20.setText(QCoreApplication.translate("MainWindow", u"\u041c\u043d\u043e\u0433\u043e \u0441\u043a\u0438\u043d\u043e\u0432", None))
        self.checkBox_21.setText(QCoreApplication.translate("MainWindow", u"AAAA", None))
        self.checkBox_22.setText(QCoreApplication.translate("MainWindow", u"Solus-like (\u0442\u0438\u043f\u0430 \u043e\u0447\u0435\u043d\u044c \u0441\u043b\u043e\u0436\u043d\u0430)", None))
        self.checkBox_23.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0433\u0440\u043e\u043c\u043d\u044b\u0435 \u0430\u043d\u0438\u043c\u0435\u0448\u043d\u044b\u0435 \u0441\u0438\u0441\u044c\u043a\u0438", None))
        self.checkBox_24.setText(QCoreApplication.translate("MainWindow", u"\u0418\u043d\u043a\u043b\u044e\u0437\u0438\u0432\u043d\u043e\u0441\u0442\u044c", None))
        self.name_label.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0438\u0433\u0440\u044b:", None))
        self.save_to_folder.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u0432 \u043f\u0430\u043f\u043a\u0443:", None))
        self.file_picker.setText("")
        self.create_b.setText(QCoreApplication.translate("MainWindow", u"\u0421\u041e\u0417\u0414\u0410\u0422\u042c!!!", None))
        self.menu_P.setTitle(QCoreApplication.translate("MainWindow", u":P", None))
    # retranslateUi

