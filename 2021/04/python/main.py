import sys
import itertools


class Num:
    def __init__(self, val: int) -> None:
        self.val = val
        self.is_marked = False

    def update_is_marked(self, num_to_check: int):
        if self.val == num_to_check:
            self.is_marked = True


class Line:
    def __init__(self, nums) -> None:
        self.nums = [Num(int(num)) for num in nums]
        self.is_complete = False

    def update_line_completed(self) -> None:
        if len([num for num in self.nums if num.is_marked]) == len(self.nums):
            self.is_complete = True


class Grid:
    def __init__(self, lines: list) -> None:
        self.rows = [Line(line) for line in lines]
        self.columns = [Line([line[i] for line in lines]) for i in range(0, len(lines))]
        self.is_complete = False

    def update_grid_completed(self) -> None:
        if any([line.is_complete for line in self.rows]) or any([line.is_complete for line in self.columns]):
            self.is_complete = True


def part_one(grids: list, numbers_drawn: list) -> int:
    for num_drawn in numbers_drawn:
        for idx, grid in enumerate(grids):
            # Check for completed line in rows
            for line in grid.rows:
                if line.is_complete:
                    continue
                for num in line.nums:
                    if num.is_marked:
                        continue
                    num.update_is_marked(int(num_drawn))
                line.update_line_completed()
            # Check for completed line in columns
            for line in grid.columns:
                if line.is_complete:
                    continue
                for num in line.nums:
                    if num.is_marked:
                        continue
                    num.update_is_marked(int(num_drawn))
                line.update_line_completed()
            grid.update_grid_completed()
            if grid.is_complete:
                unmarked_nums = list(itertools.chain(*[[num.val for num in line.nums if not num.is_marked] for line in grid.rows]))
                return num_drawn * sum(unmarked_nums)


def part_two(grids: list, numbers_drawn: list) -> int:
    completed_grids = []
    for num_drawn in numbers_drawn:
        for idx, grid in enumerate(grids):
            # Check for completed line in rows
            for line in grid.rows:
                if line.is_complete:
                    continue
                for num in line.nums:
                    if num.is_marked:
                        continue
                    num.update_is_marked(int(num_drawn))
                line.update_line_completed()
            # Check for completed line in columns
            for line in grid.columns:
                if line.is_complete:
                    continue
                for num in line.nums:
                    if num.is_marked:
                        continue
                    num.update_is_marked(int(num_drawn))
                line.update_line_completed()
            grid.update_grid_completed()
            if grid.is_complete and grid not in completed_grids:
                completed_grids.append(grid)
        if len(completed_grids) == len(grids):
            unmarked_nums = list(itertools.chain(*[[num.val for num in line.nums if not num.is_marked] for line in completed_grids[-1].rows]))
            return num_drawn * sum(unmarked_nums)


def main():
    path_to_file = sys.argv[1]
    with open(path_to_file) as f:
        lines = [line.strip() for line in f.readlines() if line.strip()]

    numbers_drawn = [int(num) for num in lines[0].split(",")]

    grids = [Grid([line.split() for line in lines[x:x + 5]]) for x in range(1, len(lines[1:]), 5)]

    print(f"Part One: {part_one(grids, numbers_drawn)}")
    print(f"Part Two: {part_two(grids, numbers_drawn)}")


if __name__ == "__main__":
    main()
