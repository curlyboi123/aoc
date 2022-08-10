import sys
from collections import Counter


def get_most_common_bit_in_reading(readings: list, position: int):
   most_common_element = Counter([reading[position] for reading in readings]).most_common()[0][0]
   print(f"Most common element is {most_common_element}")
   return most_common_element


def remove_from_list(readings: list, value_to_remove: str, position: int):
    for i in readings:  
        print(i[position])
        print(value_to_remove)
        if i[position] != value_to_remove:
            readings.remove(i)
    return readings


def part_one(report):
    most_common_bits, least_common_bits = "", ""
    for i in range(0, len(report[0])):
        bit_appearances = Counter([reading[i] for reading in report]).most_common()
        most_common_bits += bit_appearances[0][0]
        least_common_bits += bit_appearances[-1][0]

    gamma_rate = int(most_common_bits, 2)
    epsilon_rate = int(least_common_bits, 2)
    power_consumption = gamma_rate * epsilon_rate

    return power_consumption


def part_two(report):
    for i in range(0, len(report[0])):
        print(f"Evaluating position {i + 1}")
        report = remove_from_list(report, get_most_common_bit_in_reading(report, i), i)
    return report


def main():
    path_to_file = sys.argv[1]
    with open(path_to_file) as f:
        report = [line.strip() for line in f.readlines()]
    print(f"Part One: {part_one(report)}")
    print(part_two(report))





if __name__ == "__main__":
    main()
