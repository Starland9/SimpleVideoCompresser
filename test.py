import os
import subprocess

def install_ffmpeg_for_plateform():
    platform = os.name
    print(platform)
    if platform == "nt":
        subprocess.run(["choco", "install", "ffmpeg"])
        
    elif platform == "posix":
        subprocess.run(["sudo", "apt-get", "install", "ffmpeg"])
    

if __name__ == "__main__":
    install_ffmpeg_for_plateform()