import os


def get_file_path(filename: str) -> str:
    package_directory = os.path.dirname(__file__)
    file_path = os.path.join(package_directory, filename)
    return file_path
