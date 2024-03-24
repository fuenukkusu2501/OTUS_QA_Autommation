import os.path

FILES_DIR = os.path.dirname(__file__)


def get_path(filename: str):
    return os.path.join(FILES_DIR, filename)


CSV_FILE_PATH = get_path(filename="books.csv")
JSON_FILE_PATH = get_path(filename="users.json")
JSON_FILE_PATH_US = get_path(filename="users_us.json")
JSON_FILE_PATH_RESULT = get_path(filename="result.json")
JSON_FILE_PATH_EX = get_path(filename="example.json")