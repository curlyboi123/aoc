import sys


def solver(block_size: int) -> int:
    path_to_file = sys.argv[1]
    with open(path_to_file) as f:
        content = f.read()

    for i in range(0, len(content) - block_size):
        block = content[i: i + block_size]
        if len(set(block)) == block_size:
            pos_of_first_repeated = i + block_size
            return pos_of_first_repeated


def main():
    part_one_result = solver(4)
    part_two_result = solver(14)

    print(part_one_result)
    print(part_two_result)


if __name__ == "__main__":
    main()
