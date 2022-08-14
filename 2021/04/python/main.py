from re import L
import sys
import itertools


def part_one(numbers_drawn: list, grids: list):
    game_has_winner = False
    winner_index = None

    for number_drawn in numbers_drawn:
        print(f"Number drawn is {number_drawn}")
        for grid in grids:
            for line in grid:
                for num in line:
                    if number_drawn == num.val:
                        num.is_marked = True
        # Check for completed row or column
        for idx, grid in enumerate(grids):
            if check_for_completed_row(grid) or check_for_completed_column(grid):
                winner_index = idx
                game_has_winner = True
                break
        if game_has_winner == True:
            winner_unmarked_numbers_sum = get_unmarked_numbers_sum(grids[winner_index])
            return winner_unmarked_numbers_sum * number_drawn



def part_two():
    pass


class Num:
    def __init__(self, val: int) -> None:
        self.val = val
        self.is_marked = False


class Grid:
    def __init__(self, lines: list) -> None:
        self.lines = lines
        self.is_complete = False


def check_for_completed_row(grid: list) -> bool:
    for line in grid:
        pick_count = 0
        for num in line:
            if num.is_marked == True:
                pick_count += 1
        if pick_count == len(line):
            return True
    return False


def check_for_completed_column(grid: list) -> bool: 
    for i in range(0, len(grid)):
        pick_count = 0
        for line in grid:
            if line[i].is_marked == True:
                pick_count += 1
        if pick_count == len(line):
            return True
    return False
        

def get_unmarked_numbers_sum(grid: list) -> int:
    unmarked_numbers = list(itertools.chain(*([[num.val for num in line if num.is_marked == False] for line in grid])))
    return sum(unmarked_numbers)



def main():
    path_to_file = sys.argv[1]
    with open(path_to_file) as f:
        lines = [line.strip() for line in f.readlines() if line.strip()]

    numbers_drawn = [int(num) for num in lines[0].split(",")]
    
    grids = [[[Num(int(number)) for number in line.split()] for line in lines[x:x + 5]] for x in range(1, len(lines[1:]), 5)]
    grids_two = [Grid([[Num(int(number)) for number in line.split()] for line in lines[x:x + 5]]) for x in range(1, len(lines[1:]), 5)]

    print(f"Part One: {part_one(numbers_drawn, grids)}")


if __name__ == "__main__":
    main()
