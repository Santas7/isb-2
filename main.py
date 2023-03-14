import math


def read_file(filename: str) -> str:
    """
        this function is intended to read the file
        :filename: name of file
    """
    result = ""
    with open(filename, 'r', encoding='UTF-8') as file:
        result = file.read()
    return result


print(read_file("sequence.txt"))