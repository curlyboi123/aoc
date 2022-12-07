import sys
import math
import statistics


def main():
    path_to_file = sys.argv[1]
    with open(path_to_file) as f:
        content = f.read()

    values = [int(i) for i in content.strip().split(",")]
    values.sort()
    
    # Part one
    median = statistics.median(values)
    total_fuel_used = sum([abs(median - i) for i in values])
    print(round(total_fuel_used))
    
    # Part two
    mean = statistics.mean(values)

    fuel_burn = lambda x, p: abs(x - p) * (abs(x - p) + 1) // 2
    
    total_fuel_used = min(sum([fuel_burn(mean, crab_pos) for crab_pos in values]) for mean in [math.floor(mean), math.ceil(mean)])
    print(total_fuel_used)


if __name__ == "__main__":
    main()
