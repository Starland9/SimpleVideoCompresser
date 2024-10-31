import json
import os

VIDEO_EXTENSIONS = ["MP4", "MOV", "AVI", "MKV"]


class SettingsService:
    SETTINGS_FILE = "settings.json"

    def __init__(self):
        self.settings = self.load_settings()

    def load_settings(self):
        if not os.path.exists(self.SETTINGS_FILE):
            return {}

        with open(self.SETTINGS_FILE) as f:
            return json.load(f)

    def save_settings(self):
        with open(self.SETTINGS_FILE, "w") as f:
            json.dump(self.settings, f, indent=4)

    def update_settings(self, new_settings):
        self.settings.update(new_settings)
        self.save_settings()

    def get_selected_extensions(self):
        return self.settings.get("selected_extensions", VIDEO_EXTENSIONS)

    def set_selected_extensions(self, extensions):
        self.settings["selected_extensions"] = extensions
        self.save_settings()
