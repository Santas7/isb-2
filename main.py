import math

BIT = 128 # total number of bits


def read_file(filename: str) -> str:
    """
        this function is intended to read the file
        :filename: name of file
    """
    result = ""
    with open(filename, 'r', encoding='UTF-8') as file:
        result = file.read()
    return result


def frequency_beat_test(sequence: str) -> dict:
    counter = {
        '0': 0,
        '1': 0
    }
    for item in sequence:
        if item == '0':
            counter['0'] += 1
        elif item == '1':
            counter['1'] += 1
    return counter


if __name__ == '__main__':
    # part a)
    dictionary_count = frequency_beat_test(read_file("sequence.txt"))
    frequency_zeros = dictionary_count['0']/BIT
    frequency_ones = dictionary_count['1']/BIT
    difference_the_received_frequencies = frequency_zeros - frequency_ones
    print(difference_the_received_frequencies) # 0.0625
    # Considering that the difference between the frequencies is not significantly
    # large, so the test passed

    # part b)
