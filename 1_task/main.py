from pathlib import Path
from shutil import copy, rmtree
from concurrent.futures import ThreadPoolExecutor

def find_dirs(path: Path, folder_with_dirs=None):
    if folder_with_dirs is None:
        folder_with_dirs = []
    for el in path.iterdir():
        if el.is_dir():
            folder_with_dirs.append(el)
            find_dirs(el, folder_with_dirs)
    return folder_with_dirs


def copy_files(path_from_dir: Path, path_to_dir: Path):
    for el in path_from_dir.iterdir():
        if el.is_file():
            format_name_dir = el.suffix[1:]
            (path_to_dir / format_name_dir ).mkdir(exist_ok=True)
            copy(el, path_to_dir / format_name_dir / el.name)


def clear_dir(path: Path):
    for item in path.iterdir():
        if item.is_file() or item.is_symlink():
            item.unlink()
        elif item.is_dir():
            rmtree(item)


if __name__ == "__main__":
    folder_for_copy = find_dirs(Path("picture"))
    with ThreadPoolExecutor() as pool:
        for el in folder_for_copy:
            pool.submit(copy_files, el, Path("dist"))

    # clear_dir(Path("dist")) # розкоментувати для очищення цільової директорії



