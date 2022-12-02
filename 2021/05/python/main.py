import sys
from collections import Counter


def main():
    path_to_file = sys.argv[1]
    with open(path_to_file) as f:
        lines = [tuple([tuple(position.strip().split(",")) for position in line.strip().split(" -> ")]) for line in f.readlines()]
    
    pipes = []
    for pair in lines:
        x_pos_one = int(pair[0][0])
        y_pos_one = int(pair[0][1])

        x_pos_two = int(pair[1][0])
        y_pos_two = int(pair[1][1])

        # Vertical line
        if x_pos_one == x_pos_two:
            for i in range(min(y_pos_one, y_pos_two), max(y_pos_one, y_pos_two) + 1):
                pipes.append((x_pos_one, i))
        # Horizontal line
        elif y_pos_one == y_pos_two:
            for i in range(min(x_pos_one, x_pos_two), max(x_pos_one, x_pos_two) + 1):
                pipes.append((i, y_pos_one))
        # Diagonal line
        else:
            for i in range(0, abs(x_pos_one - x_pos_two) + 1):
                coord = ()
                if x_pos_one > x_pos_two:
                    if y_pos_one > y_pos_two:
                        coord = (x_pos_one - i, y_pos_one - i)
                    else:
                        coord = (x_pos_one - i, y_pos_one + i)
                elif x_pos_one < x_pos_two:
                    if y_pos_one > y_pos_two:
                        coord = (x_pos_one + i, y_pos_one - i)
                    else:
                        coord = (x_pos_one + i, y_pos_one + i)
                pipes.append(coord)

    counts = Counter(pipes)
    num_of_coords_above_two = len([count for count in counts.values() if count >= 2])
    print(num_of_coords_above_two)


if __name__ == "__main__":
    main()
