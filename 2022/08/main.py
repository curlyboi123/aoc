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
    for row_pos, tree_row in enumerate(lines):
        for col_pos, current_tree in enumerate(tree_row):
            # If tree is on the edge then it is definitely visible
            if row_pos == 0 or row_pos == len(lines) - 1 or col_pos == 0 or col_pos == len(tree_row) - 1:
                visible_trees += 1
            # Check if inner tree is visible from any direction
            else:
                trees_above = [i[col_pos] for i in lines[:row_pos]]
                trees_right = tree_row[col_pos + 1:]
                trees_below = [i[col_pos] for i in lines[row_pos + 1:]]
                trees_left = tree_row[:col_pos]
                if any(max(trees) < current_tree for trees in [trees_above, trees_right, trees_below, trees_left]):
                    visible_trees += 1
    print(visible_trees)

    # Part two
    largest_scenic_score = 0
    for row_pos, tree_row in enumerate(lines):
        for col_pos, current_tree in enumerate(tree_row):       
            if not (row_pos == 0 or row_pos == len(lines) - 1 or col_pos == 0 or col_pos == len(tree_row) - 1):
                trees_above = [i[col_pos] for i in lines[:row_pos]][::-1]
                trees_right = tree_row[col_pos + 1:]
                trees_below = [i[col_pos] for i in lines[row_pos + 1:]]
                trees_left = tree_row[:col_pos][::-1]

                above_scenic_score = scenic_score_calculator(trees_above, current_tree)
                right_scenic_score = scenic_score_calculator(trees_right, current_tree)
                below_scenic_score = scenic_score_calculator(trees_below, current_tree)
                left_scenic_score = scenic_score_calculator(trees_left, current_tree)

                scenic_score_total = above_scenic_score * right_scenic_score * below_scenic_score * left_scenic_score
                largest_scenic_score = max(largest_scenic_score, scenic_score_total)
    print(largest_scenic_score)
                

if __name__ == "__main__":
    main()
