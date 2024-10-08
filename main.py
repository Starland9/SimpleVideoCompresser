from gui_main import Ui_MainWindow
from PyQt6.QtWidgets import QMainWindow, QDialog, QFileDialog, QMessageBox

import os
import sys
from PyQt6.QtWidgets import QApplication
import converter


class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.dest_folder = None
        self.source_folder = None
        self.setupUi(self)

        self.add_actions()

    def add_actions(self):
        self.source_btn.clicked.connect(self.get_source_folder)
        self.dest_btn.clicked.connect(self.get_destination_folder)
        self.convert_pushButton.clicked.connect(self.convert_video)

    def get_source_folder(self):
        self.source_folder = QFileDialog.getExistingDirectory(self, "Select Source Folder", "",
                                                              QFileDialog.Option.ShowDirsOnly)
        self.source_lineEdit.setText(self.source_folder)

    def get_destination_folder(self):
        self.dest_folder = QFileDialog.getExistingDirectory(self, "Select Destination Folder", "",
                                                            QFileDialog.Option.ShowDirsOnly)
        self.dest_lineEdit.setText(self.dest_folder)

    def convert_video(self):
        if self.source_folder is None or self.dest_folder is None:
            QMessageBox.warning(self, "Error", "Please select source and destination folders")
            return

        self.statusbar.showMessage("Converting...")
        # Lancer la conversion
        converter.convert(self.source_folder, self.dest_folder)

        # Afficher un message indiquant que la conversion est terminee
        QMessageBox.information(self, "Conversion terminee", "Conversion terminee !")
        self.statusbar.clearMessage()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
