from src.compressor_thread import ConverterThread
from src.pyui.main_ui import Ui_MainWindow
from PyQt6.QtWidgets import QMainWindow, QFileDialog, QMessageBox

import sys
from PyQt6.QtWidgets import QApplication
from src.about import About


# noinspection PyUnresolvedReferences
class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.files_length = 0
        self.converter_thread = None
        self.dest_folder = None
        self.source_folder = None

        self.setupUi(self)

        self.progressBar.hide()

        self.add_actions()

    def add_actions(self):
        self.source_btn.clicked.connect(self.get_source_folder)
        self.dest_btn.clicked.connect(self.get_destination_folder)
        self.convert_pushButton.clicked.connect(self.convert_video)
        self.actionAbout_Dev.triggered.connect(self.show_about)

    def get_source_folder(self):
        self.source_folder = QFileDialog.getExistingDirectory(
            self, "Select Source Folder", "", QFileDialog.Option.ShowDirsOnly
        )
        self.source_lineEdit.setText(self.source_folder)

    def get_destination_folder(self):
        self.dest_folder = QFileDialog.getExistingDirectory(
            self, "Select Destination Folder", "", QFileDialog.Option.ShowDirsOnly
        )
        self.dest_lineEdit.setText(self.dest_folder)

    def convert_video(self):
        if self.source_folder is None or self.dest_folder is None:
            QMessageBox.warning(
                self, "Error", "Please select source and destination folders"
            )
            return

        self.statusbar.showMessage("Conversion started")
        self.progressBar.show()
        # Lancer la conversion dans un thread
        self.converter_thread = ConverterThread(self.source_folder, self.dest_folder)
        self.converter_thread.conversion_finished.connect(self.on_conversion_finished)
        self.converter_thread.files_length.connect(self.on_files_length)
        self.converter_thread.current_file.connect(self.on_current_file)
        self.converter_thread.current_file_name.connect(self.on_current_file_name)
        self.converter_thread.start()

    def on_conversion_finished(self):
        self.progressBar.hide()
        self.statusbar.showMessage("Conversion finished")
        QMessageBox.information(
            self, "Conversion finished", "Conversion finished successfully"
        )

    def on_files_length(self, length):
        self.files_length = length
        self.statusbar.showMessage(f"Converting {length} files")

    def on_current_file(self, current_file):
        # self.statusbar.showMessage(f"Converting file {current_file + 1}/{self.files_length}")
        self.progressBar.show()
        self.progressBar.setValue((current_file + 1) * 100 // self.files_length)

    def on_current_file_name(self, current_file_name):
        self.statusbar.showMessage(f"Converting file {current_file_name}")
        
    def show_about(self):
        self.about_dialog = About()
        self.about_dialog.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
