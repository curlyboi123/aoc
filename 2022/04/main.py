import sys


def part_one(lines: list) -> int:
    fully_contains_pairs_total = 0
    for line in lines:
        pairs = [[int(char) for char in pair.split("-")] for pair in line.split(",")]
        # Situation where pair 1 is included in pair 2 and vice versa
        if (pairs[0][0] >= pairs[1][0] and pairs[0][1] <= pairs[1][1]) or (pairs[1][0] >= pairs[0][0] and pairs[1][1] <= pairs[0][1]):
            fully_contains_pairs_total += 1
    return fully_contains_pairs_total


def part_two(lines: list) -> int:
    overlapping_pairs_total = 0
    for line in lines:
        pairs = [[int(char) for char in pair.split("-")] for pair in line.split(",")]
        pair_one_range = {i for i in range(pairs[0][0], pairs[0][1] + 1)}
        pair_two_range = {i for i in range(pairs[1][0], pairs[1][1] + 1)}
        overlapping_sections = pair_one_range.intersection(pair_two_range)
        if overlapping_sections:
            overlapping_pairs_total += 1
    return overlapping_pairs_total


def main():
    path_to_file = sys.argv[1]
    with open(path_to_file) as f:
        lines = [l.strip() for l in f.readlines()]

    print(part_one(lines))
    print(part_two(lines))


if __name__ == "__main__":
    main()
