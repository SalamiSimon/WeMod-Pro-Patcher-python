import subprocess

def install_requirements():
    try:
        subprocess.run(['pip', 'install', '-r', 'requirements.txt'], check=True)
        print("Requirements installed successfully.")
    except subprocess.CalledProcessError:
        print("Error installing requirements.")

if __name__ == "__main__":
    install_requirements()
import subprocess

def install_requirements():
    try:
        subprocess.run(['pip', 'install', '-r', 'requirements.txt'], check=True)
        print("Requirements installed successfully.")
    except subprocess.CalledProcessError:
        print("Error installing requirements.")

if __name__ == "__main__":
    install_requirements()
