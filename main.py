import math
import re

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


def get_max(lst: list) -> int:
    max = lst[0]
    for i in range(len(lst)):
        if lst[i] > max:
            max = lst[i]
    return max


def get_sum_quadro_x(v_1: int, v_2: int, v_3: int, v_4: int):
    quadro_x = 0
    # pi_1 = 0.2148
    # pi_2 = 0.3672
    # pi_3 = 0.2305
    # pi_4 = 0.1875

    quadro_x += (pow((v_1 - 16 * 0.2148), 2)) / (16 * 0.2148)
    quadro_x += (pow((v_2 - 16 * 0.3672), 2)) / (16 * 0.3672)
    quadro_x += (pow((v_3 - 16 * 0.2305), 2)) / (16 * 0.2305)
    quadro_x += (pow((v_4 - 16 * 0.1875), 2)) / (16 * 0.1875)
    return quadro_x


def get_count_blocks_max_length(sequence: str):
    # split our sequence into 8 bits
    lst = re.sub('([^ ]{8})', r'\1 ', sequence).replace('  ', ' ').split(' ')

    dict = {
        "<=1": 0,
        "=2": 0,
        "=3": 0,
        ">=4": 0
    }

    for i in range(len(lst) - 1):
        # ['10101001', '01111010', '00011001', ... ]
        for j in range(len(lst[i]) - 1):
            # '10101001', '01111010', ...
            # finding a block of units of maximum length
            longest_match = len(max(re.findall('1+', lst[i]), key=len))

            # distribute the found maximum in the created dictionary
            if longest_match <= 1:
                dict["<=1"] += 1
            elif longest_match == 2:
                dict["=2"] += 1
            elif longest_match == 3:
                dict["=3"] += 1
            elif longest_match >= 4:
                dict[">=4"] += 1
            break
    return dict["<=1"], dict["=2"], dict["=3"], dict[">=4"]


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
    # print(test_consecutive_bits(sequence))
    p_2 = math.erfc((abs(dictionary_count['1'] - 2 * BIT * frequency_ones * (1 - frequency_ones))) / (2 * math.sqrt(2 * BIT) * frequency_ones * (1 - frequency_ones)))
    print(p_2)
    # 0.5057229016557836
    # True

    # part c)
    v_1, v_2, v_3, v_4 = get_count_blocks_max_length(sequence)
    # print(v_1, v_2, v_3, v_4)
    p_3 = get_sum_quadro_x(v_1, v_2, v_3, v_4)
    print(p_3) # 2.6385189536200038