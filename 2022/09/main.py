import sys


def main():
    path_to_file = sys.argv[1]
    with open(path_to_file) as f:
        content = f.read()

    positions_visited = []
    head_pos = (0, 0)
    tail_pos = (-1, 0)
    for line in content.splitlines():
        direction, magnitude = line.split(" ")
        # Move head
        for i in range(int(magnitude)):
            if direction == "U":
                head_pos = (head_pos[0], head_pos[1] + 1)
            elif direction == "D":
                head_pos = (head_pos[0], head_pos[1] - 1)
            elif direction == "R":
                head_pos = (head_pos[0] + 1, head_pos[1])
            elif direction == "L":
                head_pos = (head_pos[0] - 1, head_pos[1])
            # Check if tail adjacent to head
            if abs(tail_pos[0] - head_pos[0]) > 1 or abs(tail_pos[1] - head_pos[1]) > 1:
                if direction == "U":
                    tail_pos = (head_pos[0], head_pos[1] - 1)
                elif direction == "D":
                    tail_pos = (head_pos[0], head_pos[1] + 1)
                elif direction == "R":
                    tail_pos = (head_pos[0] - 1, head_pos[1])
                elif direction == "L":
                    tail_pos = (head_pos[0] + 1, head_pos[1])
                positions_visited.append(tail_pos)
    print(len(set(positions_visited)))


if __name__ == "__main__":
    main()
