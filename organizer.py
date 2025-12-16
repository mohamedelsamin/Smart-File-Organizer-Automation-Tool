import os
import shutil
from config import FILE_TYPES
from logger import log_action


def create_folder(path):
    if not os.path.exists(path):
        os.makedirs(path)

def organize_files(directory):
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)

        if os.path.isfile(file_path):
            moved = False

            for folder, extensions in FILE_TYPES.items():
                if filename.lower().endswith(tuple(extensions)):
                    folder_path = os.path.join(directory, folder)
                    create_folder(folder_path)

                    shutil.move(file_path, os.path.join(folder_path, filename))
                    log_action(f"Moved {filename} to {folder}")
                    moved = True
                    break

            if not moved:
                other_path = os.path.join(directory, "Others")
                create_folder(other_path)
                shutil.move(file_path, os.path.join(other_path, filename))
                log_action(f"Moved {filename} to Others")

if __name__ == "__main__":
    target_directory = input("Enter directory path: ")
    organize_files(target_directory)
    print("✅ Files organized successfully!")
