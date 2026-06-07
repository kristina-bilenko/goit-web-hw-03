from pathlib import Path
from shutil import copy

def find_dirs(path:Path, folder_with_dirs = None):
    if folder_with_dirs is None:
        folder_with_dirs = []
    for el in path.iterdir():
        if el.is_dir():
            folder_with_dirs.append(el)
            find_dirs(el, folder_with_dirs)
    return folder_with_dirs

def copy_files(path_from_dir:Path, path_to_dir:Path):
    for el in path_from_dir.iterdir():




folder_for_copy = find_dirs(Path("picture"))
print(folder_for_copy)

# for el in folder_for_copy:
#     copy_files(el)


