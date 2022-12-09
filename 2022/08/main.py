import sys


def scenic_score_calculator(trees_to_compare: list, current_tree: int) -> int:
    scenic_score = len(trees_to_compare)
    for idx, tree in enumerate(trees_to_compare):
        if tree >= current_tree:
            scenic_score = idx + 1
            break
    return scenic_score


def main():
    path_to_file = sys.argv[1]
    with open(path_to_file) as f:
        lines = [list(f.strip()) for f in f.readlines()]
    # Part one
    visible_trees = 0
    height = len(lines)
    width = len(lines[0])

    for x in range(width):
        for y in range(height):
            tree = lines[y][x]
            # If tree is on the edge then it is definitely visible
            if x == 0 or x == width - 1 or y == 0 or y == height - 1:
                visible_trees += 1
            # Check if inner tree is visible from any direction
            else:
                trees_above = [i[x] for i in lines[:y]]
                trees_right = lines[y][x + 1:]
                trees_below = [i[x] for i in lines[y + 1:]]
                trees_left = lines[y][:x]
                if any(max(trees) < tree for trees in [trees_above, trees_right, trees_below, trees_left]):
                    visible_trees += 1
    print(visible_trees)

    # Part two
    largest_scenic_score = 0
    for x in range(width):
        for y in range(height):
            tree = lines[y][x]
            # If tree is on the edge then it is definitely visible
            if not (x == 0 or x == width - 1 or y == 0 or y == height - 1):
                trees_above = [i[x] for i in lines[:y]][::-1]
                trees_right = lines[y][x + 1:]
                trees_below = [i[x] for i in lines[y + 1:]]
                trees_left = lines[y][:x][::-1]

                above_scenic_score = scenic_score_calculator(trees_above, tree)
                right_scenic_score = scenic_score_calculator(trees_right, tree)
                below_scenic_score = scenic_score_calculator(trees_below, tree)
                left_scenic_score = scenic_score_calculator(trees_left, tree)

                scenic_score_total = above_scenic_score * right_scenic_score * below_scenic_score * left_scenic_score
                largest_scenic_score = max(largest_scenic_score, scenic_score_total)
    print(largest_scenic_score)
                

if __name__ == "__main__":
    main()
