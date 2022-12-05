import sys


def solver(part_to_solve: str) -> str:
    path_to_file = sys.argv[1]
    with open(path_to_file) as f:
        lines = f.read()

    crate_positions = lines.split("\n\n")[0]
    movements = lines.split("\n\n")[1]

    rows = crate_positions.splitlines()
    cols = []
    for i in range(0, len(rows[-1]), 4):
        col = []
        for row in rows[:-1]:
            crate = row[i:i+4].strip().replace("[", "").replace("]", "")
            if crate:
                col.append(crate)
        cols.append(col)

    for movement in [movement.split(" ") for movement in movements.splitlines()]:
        num_crates_moved, stack_move_from, stack_move_to = int(movement[1]), int(movement[3]), int(movement[5])
        crates_to_move = cols[stack_move_from - 1][:num_crates_moved]  # Get list slice of crates to move
        # For each crate to move, insert it at the start of the list of the col to move to
        if part_to_solve == "1":
            for crate in crates_to_move:
                cols[stack_move_to - 1].insert(0, crate)
        elif part_to_solve == "2":
            for crate in crates_to_move[::-1]:
                cols[stack_move_to - 1].insert(0, crate)
        del cols[stack_move_from - 1][:num_crates_moved]  # Delete crates from col they came from

    crates_on_top_of_stacks = [crate[0] for crate in cols]
    return "".join(crates_on_top_of_stacks)


def main():
    part_one_answer = solver("1")
    part_two_answer = solver("2")

    print(part_one_answer)
    print(part_two_answer)


if __name__ == "__main__":
    main()
