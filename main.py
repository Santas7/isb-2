import math

BIT = 128  # total number of bits


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


def test_consecutive_bits(sequence) -> bool:
    # check if there are two consecutive bits with the same value
    for i in range(len(sequence) - 1):
        if sequence[i] == sequence[i + 1]:
            return True
    # if there are no two consecutive bits with the same value, the test is successful
    return False


if __name__ == '__main__':
    sequence = read_file("sequence.txt")
    dictionary_count = frequency_beat_test(sequence)
    frequency_zeros = dictionary_count['0'] / BIT
    frequency_ones = dictionary_count['1'] / BIT
    difference_the_received_frequencies = frequency_zeros - frequency_ones
    print(difference_the_received_frequencies)
    p_1 = difference_the_received_frequencies # 0.0625
    # Considering that the difference between the frequencies is not significantly
    # large, so the test passed

    # part b)
    print(test_consecutive_bits(sequence))
    p_2 = math.erfc((abs(dictionary_count['1'] - 2 * 128 * frequency_ones * (1 - frequency_ones))) / (2 * math.sqrt(2 * 128) * frequency_ones * (1 - frequency_ones)))
    print(p_2)
    # 0.5057229016557836
    # True

    # part c)
