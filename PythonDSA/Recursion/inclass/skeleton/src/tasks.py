import os


def traverse_directories(path: str) -> list[str]:
    files_and_folders = []
    folder_name = os.path.split(path)[-1]
    files_and_folders.append(folder_name)
    entries = os.listdir(path)
    for entry in entries:
        full_path = os.path.join(path, entry)
        if os.path.isdir(full_path):
            files_and_folders.extend(traverse_directories(full_path))
        else:
            files_and_folders.append(entry)
    return files_and_folders


def find_files(path: str, extension: str) -> list[str]:
    matching_files = []
    entries = os.listdir(path)
    for entry in entries:
        full_path = os.path.join(path, entry)
        if os.path.isfile(full_path) and entry.endswith(extension):
            matching_files.append(entry)
        elif os.path.isdir(full_path):
            matching_files.extend(find_files(full_path, extension))
    return matching_files


def file_exists(path: str, file_name: str) -> bool:
    entries = os.listdir(path)
    if file_name in entries:
        return True
    for entry in entries:
        full_path = os.path.join(path, entry)
        if os.path.isdir(full_path):
            if file_exists(full_path, file_name):
                return True
    return False


def directory_stats(path: str) -> dict:
    stats = {}
    entries = os.listdir(path)
    for entry in entries:
        full_path = os.path.join(path, entry)
        if os.path.isfile(full_path):
            _, file_extension = os.path.splitext(entry)
            stats[file_extension] = stats.get(file_extension, 0) + 1
        elif os.path.isdir(full_path):
            subdir_stats = directory_stats(full_path)
            for ext, count in subdir_stats.items():
                stats[ext] = stats.get(ext, 0) + count
    return stats
