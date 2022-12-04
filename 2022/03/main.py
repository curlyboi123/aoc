import sys


def main():
    path_to_file = sys.argv[1]
    with open(path_to_file) as f:
        lines = [l.strip() for l in f.readlines()]

    priority_total = 0
    for line in lines:
        first_rucksack = line[:len(line)//2]
        second_rucksack = line[len(line)//2:]
        common_element = ''.join(set(first_rucksack).intersection(second_rucksack))

        if common_element.islower():
            priority = ord(common_element) - 96
        else:
            priority = ord(common_element) - 38
        priority_total += priority
    
    print(priority_total)


if __name__ == "__main__":
    main()
