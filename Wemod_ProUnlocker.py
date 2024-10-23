import os
import shutil
import glob
import subprocess
from colorama import init, Fore, Style

# Initialize colorama for colored output
init(autoreset=True)

# Function to display the text start menu
def display_start_menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"{Fore.RED}{Style.BRIGHT}WeMod Patcher")
    print("By Sten\n")

    print(f"{Fore.GREEN}Unlocks Pro on WeMod.")
    print(f"{Fore.YELLOW}Tested on version: 8.20.0")
    print(f"{Fore.RED}What doesn't work: RC from phone (this feature is server-side)\n")

    print(f"{Style.BRIGHT}Instructions:")
    print("Close app fully from task manager if it's running")
    print("If patch fails and something happens to the app, run 'Restore app'\n")

    print(f"{Style.BRIGHT}Options:")
    print("1. Patch app")
    print("2. Restore app")
    print("3. Exit\n")

# Function to wait for user input and clear terminal window
def wait_and_clear():
    input("Press Enter to continue...")
    os.system('cls' if os.name == 'nt' else 'clear')

# Function to patch the app
def patch_app():
    app_folders = glob.glob(os.path.join(user_directory, 'AppData', 'Local', 'WeMod', 'app-*'))
    print(f"Searching for WeMod app folders in: {os.path.join(user_directory, 'AppData', 'Local', 'WeMod')}")  # Debugging log

    if not app_folders:
        print(f"{Fore.RED}Error: No app- folders found.")
        wait_and_clear()
        return

    for app_folder in app_folders:
        version = app_folder.split('-')[-1]
        print(f"{Fore.GREEN}Found version: {version}")  # Debugging log

        source_path = os.path.join(os.getcwd(), 'app.asar')
        destination_path = os.path.join(app_folder, 'resources', 'app.asar')

        # Ensure the Backups directory exists
        backup_folder = os.path.join(os.getcwd(), 'Backups')
        if not os.path.exists(backup_folder):
            os.makedirs(backup_folder)
            print(f"Backups folder created at: {backup_folder}")  # Debugging log

        backup_path = os.path.join(backup_folder, f'app_backup_{version}.asar')

        # Check if the original app.asar file exists before attempting to back it up
        if os.path.exists(destination_path):
            # Backup the original app.asar file to the Backups folder
            shutil.copy(destination_path, backup_path)
            print(f"{Fore.GREEN}Backup created for version: {version}.")
        else:
            print(f"{Fore.YELLOW}Warning: No original app.asar found for version {version}. Skipping backup.")

        # Copy the new app.asar file to the app-* folder, overwriting the existing one
        shutil.copy(source_path, destination_path)

    print(f"{Fore.GREEN}Patch successful.")
    wait_and_clear()

# Function to restore the app
def restore_app():
    backup_folder = os.path.join(os.getcwd(), 'Backups')
    print(f"Looking for backups in: {backup_folder}")  # Debugging log

    if not os.listdir(backup_folder):
        print(f"{Fore.RED}Error: No backup files found.")
        wait_and_clear()
        return

    for backup_file in os.listdir(backup_folder):
        if backup_file.startswith('app_backup_') and backup_file.endswith('.asar'):
            version = backup_file.split('_')[2][:-5]
            print(f"Restoring version: {version}")  # Debugging log

            source_path = os.path.join(backup_folder, backup_file)
            destination_path = os.path.join(user_directory, 'AppData', 'Local', 'WeMod', f'app-{version}', 'resources', 'app.asar')

            print(f"Restoring from {source_path} to {destination_path}")  # Debugging log

            try:
                shutil.copy(source_path, destination_path)
                print(f"{Fore.GREEN}Restore successful for version: {version}.")
            except Exception as e:
                print(f"{Fore.RED}Error restoring version {version}: {e}")
                continue

    wait_and_clear()


if __name__ == "__main__":
    user_directory = os.path.expanduser("~")

    while True:
        display_start_menu()
        option = input("Enter the option number: ")

        if option == '1':
            patch_app()
        elif option == '2':
            restore_app()
        elif option == '3':
            break  # Exit the loop and end the script
        else:
            print(f"{Fore.RED}Invalid option. Please enter a valid option.")
            wait_and_clear()
