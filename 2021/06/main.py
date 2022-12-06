import sys


def solver(days: int, fish_states: list) -> int:
    states = {i: fish_states.count(i) for i in range(9)}
    for i in range(days):
        num_of_expired_fish = states[0]
        for fish_age in states.keys():
            if fish_age == 6:
                states[fish_age] = states[fish_age + 1] + num_of_expired_fish
            elif fish_age == 8:
                states[8] = num_of_expired_fish
            else:
                states[fish_age] = states[fish_age + 1]
    total_fish = sum([amount for amount in states.values()])
    return total_fish


def main():
    path_to_file = sys.argv[1]
    with open(path_to_file) as f:
        content = f.read()
    fish_states = [int(i) for i in content.strip().split(",")]

    # Part one solution

    # for i in range(days):
    #     num_fish_to_add = 0
    #     for idx, state in enumerate(fish_states):
    #         if state == 0:
    #             num_fish_to_add += 1
    #             fish_states[idx] = 6
    #         else:
    #             fish_states[idx] -= 1
    #     fish_to_add = [8] * num_fish_to_add
    #     fish_states.extend(fish_to_add)
    # total_fish = len(fish_states)
    # print(total_fish)

    part_one_solution = solver(80, fish_states)
    part_two_solution = solver(256, fish_states)
    print(part_one_solution)
    print(part_two_solution)


if __name__ == "__main__":
    main()
