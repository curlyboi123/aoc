import sys
from collections import Counter


def part_one(report):
    most_common_bits = ""
    for i in range(0, len(report[0])):
        most_common_bits += Counter([reading[i] for reading in report]).most_common(1)[0][0]
    least_common_bits = "".join(["0" if i == "1" else "1" for i in most_common_bits])

    gamma_rate = int(most_common_bits, 2)
    epsilon_rate = int(least_common_bits, 2)
    power_consumption = gamma_rate * epsilon_rate

    return power_consumption


def main():
    path_to_file = sys.argv[1]
    with open(path_to_file) as f:
        report = [line.strip() for line in f.readlines()]
    print(f"Part One: {part_one(report)}")


if __name__ == "__main__":
    main()
