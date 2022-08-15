import sys
from collections import Counter


def main():
    path_to_file = sys.argv[1]
    with open(path_to_file) as f:
        lines = [tuple([tuple(position.strip().split(",")) for position in line.strip().split("-> ")]) for line in f.readlines()]
    
    pipes = []
    for pair in lines:
        x_pos_one = int(pair[0][0])
        y_pos_one = int(pair[0][1])

        x_pos_two = int(pair[1][0])
        y_pos_two = int(pair[1][1])


        if x_pos_one == x_pos_two:
            for i in range(min(y_pos_one, y_pos_two), max(y_pos_one, y_pos_two) + 1):
                pipes.append((x_pos_one, i))
            
        if y_pos_one == y_pos_two:
            for i in range(min(x_pos_one, x_pos_two), max(x_pos_one, x_pos_two) + 1):
                pipes.append((i, y_pos_one))
            
    counts = Counter(pipes)
    num_of_coords_above_two = len([coord for coord, count in counts.items() if count >= 2])
    print(num_of_coords_above_two)


if __name__ == "__main__":
    main()
