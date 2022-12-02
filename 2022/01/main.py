import sys


def main():
    path_to_file = sys.argv[1]
    with open(path_to_file) as f:
        content = f.read()

    calories = [list(map(int, a.splitlines())) for a in content.split("\n\n")]
    calorie_totals = [sum(elf) for elf in calories]
    highest_calories = max(calorie_totals)

    top_three_highest_calories = sorted(calorie_totals)[len(calorie_totals) - 3:]

    print(highest_calories)
    print(sum(top_three_highest_calories))


if __name__ == "__main__":
    main()
