from PyQt6.QtCore import QThread, pyqtSignal

import subprocess
import os

from ffmpeg import FFmpeg

class ConverterThread(QThread):
    conversion_finished = pyqtSignal()
    files_length = pyqtSignal(int)
    current_file = pyqtSignal(int)
    current_file_name = pyqtSignal(str)

    def __init__(self, source, dest):
        super().__init__()
        self.source = source
        self.dest = dest

    def run(self):
        try:
            fichiers_a_convertir = [
                f for f in os.listdir(self.source)
            ]

            self.files_length.emit(len(fichiers_a_convertir))

            for fichier in fichiers_a_convertir:
                self.current_file_name.emit(fichier)
                print(f"Conversion du fichier {fichier} en cours...")
                source = os.path.join(self.source, fichier)
                destination = os.path.join(self.dest, fichier)
                ffmpeg = FFmpeg().option("y").input(source).output(destination)

                ffmpeg.execute()
                self.current_file.emit(fichiers_a_convertir.index(fichier))
                print(f"Fichier {fichier} converti avec succès !\n")

            print("Tous les fichiers ont été convertis avec succès !")
            self.conversion_finished.emit()
        except Exception as e:
            install_ffmpeg_for_plateform()
            self.run()
            print(f"Erreur pendant la conversion : {e}")
            self.conversion_finished.emit()
            
    
def install_ffmpeg_for_plateform():
    platform = os.name
    print(platform)
    if platform == "nt":
        subprocess.run(["choco", "install", "ffmpeg"])
        
    elif platform == "posix":
        subprocess.run(["sudo", "apt-get", "install", "ffmpeg"])