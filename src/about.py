from src.pyui.about_ui import Ui_Dialog
from PyQt6.QtWidgets import QDialog

class About(QDialog, Ui_Dialog):
    
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.retranslateUi(self)