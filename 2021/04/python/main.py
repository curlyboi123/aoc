import sys


def part_one():
    pass


def part_two():
    pass


class Player:
    def __init__(self):
        pass


class Grid:
    def __init__(self, lines: list):
        self.nums = []
        for col_position, line in enumerate(lines):
            for row_position, val in enumerate(line):
                self.nums.append(Num(int(val), row_position, col_position))


class Num:
    def __init__(self, value: int, row: int, col: int):
        self.value = value
        self.row = row
        self.col = col
        self.has_been_picked = False


def main():
    path_to_file = sys.argv[1]
    with open(path_to_file) as f:
        lines = [line.strip() for line in f.readlines() if line.strip()]

    # numbers_drawn = lines[0].split(",")
    # print(f"Numbers drawn: {numbers_drawn}")
    #
    # grids = [[line.split() for line in lines[x:x + 5]] for x in range(1, len(lines[1:]), 5)]
    #
    # player_to_grid_mapping = {}
    # for idx, grid in enumerate(grids):
    #     player_to_grid_mapping[idx] = grid
    first_grid = [line.split() for line in lines[1: 6]]
    grid_one = Grid(first_grid)

# value, row, col, has been picked
# e.g 22, 1, 1, false

# grid has 25 nums, has row complete, has col complete
# e.g. [nums], false, false

# player has grid, has win
# e.g. grid, false


if __name__ == "__main__":
    main()
