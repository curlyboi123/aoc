import sys


def main():
    path_to_file = sys.argv[1]
    with open(path_to_file) as f:
        content = f.read()

    values = [int(i) for i in content.strip().split(",")]
    values.sort()
    
    # Part one
    middle_pos = round(len(values) / 2)
    if len(values) % 2 == 0:
        median = (values[middle_pos] + values[middle_pos]) / 2
    else:
        median = values[middle_pos]
    total_fuel_used = sum([abs(median - i) for i in values])
    print(round(total_fuel_used))
    
    # Part two
    # Need to work out mean rounded down and up to know which fuel amount will be lower
    means = [sum(values) // len(values), round(sum(values) / len(values))]

    fuel_burn = lambda x, p: abs(x - p) * (abs(x - p) + 1) // 2
    
    total_fuel_used = min(sum([fuel_burn(mean, crab_pos) for crab_pos in values]) for mean in means)
    print(total_fuel_used)


if __name__ == "__main__":
    main()
