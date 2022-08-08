import sys


def part_one(measurements):
    changes = []
    for i in range(1, len(measurements)):
        if measurements[i] > measurements[i - 1]:
            changes.append("increased")
        if measurements[i] < measurements[i - 1]:
            changes.append("decreased")
        if measurements[i] == measurements[i - 1]:
            changes.append("no change")
    return changes.count("increased")


def part_two(measurements):
    changes = []
    for i in range(3, len(measurements)):
        if measurements[i] > measurements[i - 3]:
            changes.append("increased")
        if measurements[i] < measurements[i - 3]:
            changes.append("decreased")
        if measurements[i] == measurements[i - 3]:
            changes.append("no change")
    return changes.count("increased")


def main():
    path_to_file = sys.argv[1]
    with open(path_to_file) as f:
        measurements = [int(line.strip()) for line in f.readlines()]
    print(f"Part One: {part_one(measurements)}")
    print(f"Part Two: {part_two(measurements)}")


if __name__ == "__main__":
    main()
