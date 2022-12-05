import sys


def split(list_a, chunk_size):
    for i in range(0, len(list_a), chunk_size):
        yield list_a[i:i + chunk_size]


def priority_calculator(letter: str) -> int:
    if letter.islower():
        priority = ord(letter) - 96
    else:
        priority = ord(letter) - 38
    return priority


def part_one(lines: list) -> int:
    priority_total = 0
    for line in lines:
        first_rucksack = line[:len(line)//2]
        second_rucksack = line[len(line)//2:]
        common_element = ''.join(set(first_rucksack).intersection(second_rucksack))
        priority_total += priority_calculator(common_element)
    return priority_total


def part_two(lines: list) -> int:
    groups = (list(split(lines, 3)))
    priority_total = 0
    for group in groups:
        common_element = ''.join(set(group[0]).intersection(group[1], group[2]))
        priority_total += priority_calculator(common_element)
    return priority_total
        

def main():
    path_to_file = sys.argv[1]
    with open(path_to_file) as f:
        lines = [l.strip() for l in f.readlines()]
    print(part_one(lines))
    print(part_two(lines))


if __name__ == "__main__":
    main()
