from tqdm import tqdm
import os
import shutil
import sys

def sort_downloads(download_folder):
    file_types = {
        "Pictures": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff"],
        "Documents": [".pdf", ".doc", ".docx", ".txt", ".xls", ".xlsx", ".ppt", ".pptx"],
        "Videos": [".mp4", ".mkv", ".avi", ".mov", ".wmv"],
        "Music": [".mp3", ".wav", ".aac", ".flac"],
        "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
        "Programs": [".exe", ".msi", ".bat", ".sh"],
        "Others": []
    }

    current_exe = None
    if getattr(sys, 'frozen', False):  # Running as a PyInstaller .exe
        current_exe = os.path.basename(sys.executable)

    for category in file_types:
        os.makedirs(os.path.join(download_folder, category), exist_ok=True)

    files = [f for f in os.listdir(download_folder) if os.path.isfile(os.path.join(download_folder, f))]

    for file_name in tqdm(files, desc="Sorting Files", dynamic_ncols=True):
        if file_name == current_exe:
            continue

        file_path = os.path.join(download_folder, file_name)
        file_extension = os.path.splitext(file_name)[1].lower()

        target_folder = "Others"
        for category, extensions in file_types.items():
            if file_extension in extensions:
                target_folder = category
                break

        destination = os.path.join(download_folder, target_folder, file_name)
        shutil.move(file_path, destination)

if __name__ == "__main__":
    downloads_path = os.path.expanduser("~/Downloads")
    sort_downloads(downloads_path)
    print("\nDownloads folder sorted successfully!")