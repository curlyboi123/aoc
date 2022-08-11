import sys
from collections import Counter


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
    most_common_report_copy = report
    least_common_report_copy = report

    for position in range(0, len(most_common_report_copy[0])):
        char_frequency = Counter([reading[position] for reading in most_common_report_copy]).most_common()
        if char_frequency[0][1] == char_frequency[1][1]:
            most_common_char = "1"
        else:
            most_common_char = char_frequency[0][0]
        most_common_report_copy = [i for i in most_common_report_copy if i[position] == most_common_char]
        if len(most_common_report_copy) == 1:
            break

    for position in range(0, len(least_common_report_copy[0])):
        char_frequency = Counter([reading[position] for reading in least_common_report_copy]).most_common()
        if char_frequency[0][1] == char_frequency[1][1]:
            least_common_char = "0"
        else:
            least_common_char = char_frequency[1][0]
        least_common_report_copy = [i for i in least_common_report_copy if i[position] == least_common_char]
        if len(least_common_report_copy) == 1:
            break

    oxygen_generator_rating_binary = most_common_report_copy[0]
    oxygen_generator_rating_decimal = int(oxygen_generator_rating_binary, 2)

    co2_scrubber_rating_binary = least_common_report_copy[0]
    co2_scrubber_rating_decimal = int(co2_scrubber_rating_binary, 2)

    life_support_rating = oxygen_generator_rating_decimal * co2_scrubber_rating_decimal

    return life_support_rating


def main():
    path_to_file = sys.argv[1]
    with open(path_to_file) as f:
        report = [line.strip() for line in f.readlines()]
    print(f"Part One: {part_one(report)}")
    print(f"Part Two: {part_two(report)}")


if __name__ == "__main__":
    main()
