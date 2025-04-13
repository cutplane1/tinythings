#include "mainwindow.h"
#include "./ui_mainwindow.h"

MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::MainWindow)
{
    ui->setupUi(this);
    connect(ui->file_picker, &QPushButton::released, this, &MainWindow::filedialog);
    connect(ui->create_b, &QPushButton::released, this, &MainWindow::cheese);

}

void MainWindow::cheese()
{
    QString gamename = ui->name->text();
    auto genres = new QList<QString>();

    //genre_append
    for (int i = 0; i < ui->genre->count(); ++i) {
        auto ch = qobject_cast<QCheckBox*>(ui->genre->itemAt(i)->widget());
        auto ch2 = qobject_cast<QCheckBox*>(ui->genre_2->itemAt(i)->widget());
        if (ch) {
            if(ch->isChecked()) {
                genres->append(ch->text());
            }
        }

        if (ch2) {
            if(ch2->isChecked()) {
                genres->append(ch2->text());
            }
        }
    }

    int optimisation = ui->optimization_slider->sliderPosition()*25;

    auto feature = new QList<QString>();

    //feature_append
    for (int i = 0; i < ui->features->count(); ++i) {
        auto ch = qobject_cast<QCheckBox*>(ui->features->itemAt(i)->widget());
        auto ch2 = qobject_cast<QCheckBox*>(ui->features_2->itemAt(i)->widget());
        if (ch) {
            if(ch->isChecked()) {
                feature->append(ch->text());
            }
        }

        if (ch2) {
            if(ch2->isChecked()) {
                feature->append(ch2->text());
            }
        }
    }
    qDebug() << feature->count();
    delete genres;
    delete feature;

}

void MainWindow::filedialog()
{
    auto f = QFileDialog::getExistingDirectory(0, ("папка куда всё будет сохраняться"), QDir::currentPath());
    ui->path->setText(f);
}

MainWindow::~MainWindow()
{
    delete ui;
}
