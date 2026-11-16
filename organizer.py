import os
import shutil
from pathlib import Path

EXTENSION_MAP = {
    ".pdf": "Documents",
    ".doc": "Documents",
    ".docx": "Documents",
    ".txt": "Documents",
    ".xlsx": "Documents",
    ".jpg": "Images",
    ".jpeg": "Images",
    ".png": "Images",
    ".gif": "Images",
    ".mp4": "Videos",
    ".mkv": "Videos",
    ".avi": "Videos",
    ".zip": "Archives",
    ".rar": "Archives",
    ".tar": "Archives",
    ".py": "Code",
    ".html": "Code",
    ".css": "Code",
    ".js": "Code"
}

def organize_directory(target_dir):
    if not os.path.exists(target_dir):
        print(f"Error: Directory '{target_dir}' does not exist.")
        return

    moved_count = 0
    skipped_count = 0

    print(f"Scanning directory: {target_dir}\n")

    with os.scandir(target_dir) as entries:
        for entry in entries:
            if entry.is_file():
                if entry.name == os.path.basename(__file__):
                    continue

                ext = Path(entry.name).suffix.lower()
                folder_name = EXTENSION_MAP.get(ext, "Others")
                dest_folder = os.path.join(target_dir, folder_name)

                try:
                    os.makedirs(dest_folder, exist_ok=True)
                    dest_path = os.path.join(dest_folder, entry.name)

                    counter = 1
                    base_name = Path(entry.name).stem
                    while os.path.exists(dest_path):
                        new_name = f"{base_name}_{counter}{ext}"
                        dest_path = os.path.join(dest_folder, new_name)
                        counter += 1

                    shutil.move(entry.path, dest_path)
                    print(f"[MOVED] {entry.name} -> {folder_name}/")
                    moved_count += 1

                except (PermissionError, FileExistsError) as e:
                    print(f"[ERROR] Could not move {entry.name}: {e}")
                    skipped_count += 1

    print("\n--- Execution Summary ---")
    print(f"Total files relocated: {moved_count}")
    print(f"Total files skipped:   {skipped_count}")

if __name__ == "__main__":
    folder_to_clean = input("Enter folder path to organize (press Enter for current folder): ").strip()
    if not folder_to_clean:
        folder_to_clean = os.getcwd()
    organize_directory(folder_to_clean)
              
