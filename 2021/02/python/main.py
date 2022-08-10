import sys


def part_one(commands):
    horizontal_position = 0
    depth = 0
    for command in commands:
        direction = command[0]
        magnitude = int(command[1])
        if direction == "forward":
            horizontal_position += magnitude
        elif direction == "up":
            depth -= magnitude
        elif direction == "down":
            depth += magnitude
    return horizontal_position * depth


def part_two(commands):
    horizontal_position = 0
    depth = 0
    aim = 0
    for command in commands:
        direction = command[0]
        magnitude = int(command[1])
        if direction == "forward":
            horizontal_position += magnitude
            depth += aim * magnitude
        elif direction == "up":
            aim -= magnitude
        elif direction == "down":
            aim += magnitude
    return horizontal_position * depth


def main():
    path_to_file = sys.argv[1]
    with open(path_to_file) as f:
        commands = [tuple(line.strip().split()) for line in f.readlines()]

    print(f"Part One: {part_one(commands)}")
    print(f"Part Two: {part_two(commands)}")


if __name__ == "__main__":
    main()
