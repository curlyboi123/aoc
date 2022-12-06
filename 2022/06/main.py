import sys


def solver(part: str) -> int:
    path_to_file = sys.argv[1]
    with open(path_to_file) as f:
        content = f.read()

    if part == "1":
        block_size = 4
    elif part == "2":
        block_size = 14
    else:
        raise ValueError("Function only accepts values '1' and '2'")

    for i in range(0, len(content) - block_size):
        block = content[i: i + block_size]
        if len(set(block)) == block_size:
            pos_of_first_repeated = i + block_size
            return pos_of_first_repeated


def main():
    part_one_result = solver("1")
    part_two_result = solver("2")

    print(part_one_result)
    print(part_two_result)


if __name__ == "__main__":
    main()
