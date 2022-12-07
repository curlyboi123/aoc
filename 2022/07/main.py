import sys


def main():
    path_to_file = sys.argv[1]
    with open(path_to_file) as f:
        content = f.read()
    actions = [i.strip().splitlines() for i in content.split("$") if i]

    system_dir = {"/": 0}  # Map where keys are directory names and the values are the size of the files within them
    current_dir = ""  # Var to track current position e.g. '/dir_a/dir_b/'
    for action in actions:
        if "cd" in action[0]:
            destination_dir = action[0].split("cd")[-1].strip()
            # Go to the root of the file system
            if destination_dir == "/":
                current_dir = "/"
            # Go up one directory
            elif destination_dir == "..":
                current_dir = f'/{"/".join([i for i in current_dir.split("/") if i][:-1])}/'
                if current_dir == "//":
                    current_dir = "/"
            else:
                current_dir += f"{destination_dir}/"
        if action[0] == "ls":
            files = []
            for move in action[1:]:
                if move.startswith("dir"):
                    new_dir = move.split(" ")[1]
                    system_dir[f"{current_dir}{new_dir}/"] = 0
                else:
                    files.append(int(move.split(" ")[0]))
                    system_dir[current_dir] = sum(files)

    dirs_total_size = {}  # Dictionary to hold the total size of each directory
    for k in system_dir.keys():
        # For each directory get the total size of the files in itself and the directories nested under it
        dir_size_total = sum([file_size_total for dir_name, file_size_total in system_dir.items() if dir_name.startswith(k)])
        dirs_total_size[k] = dir_size_total
    # Get sum of all dirs with size below 100,000
    all_dirs_size = sum([i for i in dirs_total_size.values() if i <= 100000])
    print(all_dirs_size)

    total_available_space = 70000000
    desired_unused_space = 30000000
    used_space = dirs_total_size["/"]
    unused_space = total_available_space - used_space
    min_size_dir_to_delete = desired_unused_space - unused_space

    potential_dirs_to_delete = {dir_name: dir_size for dir_name, dir_size in dirs_total_size.items() if dir_size >= min_size_dir_to_delete}
    smallest_dir_to_delete = min([dir_size for dir_size in potential_dirs_to_delete.values()])
    print(smallest_dir_to_delete)


if __name__ == "__main__":
    main()
