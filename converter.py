import os

from ffmpeg import FFmpeg


def convert(dossier_source, dossier_destination):
    fichiers_a_convertir = [
        f for f in os.listdir(dossier_source)
    ]

    for fichier in fichiers_a_convertir:
        print(f"Conversion du fichier {fichier} en cours...")

        # Lire le fichier source
        source = os.path.join(dossier_source, fichier)

        # Lire le fichier destination
        destination = os.path.join(dossier_destination, fichier)

        # Effectuer la conversion
        ffmpeg = FFmpeg().option("y").input(source).output(destination)

        ffmpeg.execute()
        print(f"Fichier {fichier} converti avec succès !\n")

    # Afficher un message indiquant que tous les fichiers ont été convertis
    print("Tous les fichiers ont été convertis avec succès !")
