from src.services.settings_services import VIDEO_EXTENSIONS, SettingsService
from src.pyui.settings_ui import Ui_Dialog
from PyQt6.QtWidgets import QDialog, QCheckBox, QSpacerItem, QSizePolicy


class Settings(Ui_Dialog, QDialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.retranslateUi(self)

        self.selected_extensions = SettingsService().get_selected_extensions()

        self.fill_extensions()

    def fill_extensions(self):
        for ext in VIDEO_EXTENSIONS:
            chk = QCheckBox(ext.upper())
            chk.setChecked(ext in self.selected_extensions)
            chk.stateChanged.connect(
                lambda state, chk=chk: self.toggle_selected_exts(state, chk.text())
            )
            self.extensions_groupBox.layout().addWidget(chk)

        self.extensions_groupBox.layout().addItem(
            QSpacerItem(
                20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding
            )
        )

    def toggle_selected_exts(self, state, text):
        if state == 2:
            self.selected_extensions.append(text)
        else:
            self.selected_extensions.remove(text)

    def get_selected_extensions(self):
        return self.selected_extensions

    def accept(self):
        SettingsService().set_selected_extensions(self.selected_extensions)
        return super().accept()
