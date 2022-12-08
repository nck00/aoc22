current_directory = []
directory_sizes = {}

def change_directory(directory: str, current_directory: list) -> list:
    if directory == "/":
        return ["/"]
    elif directory == "..":
        return current_directory[:-1]
    else:
        current_directory.append(directory)
        return current_directory

def update_directory_sizes(current_path: list, size: int) -> None:
    directoryKey = ""
    for directory in current_path:
        if directory != "/":
            directoryKey = directoryKey + directory + "/"
        else:
            directoryKey = directory
        try:
            directory_sizes[directoryKey]
        except KeyError:
            directory_sizes[directoryKey] = 0
        directory_sizes[directoryKey] = directory_sizes[directoryKey] + int(size)

with open("input.txt", "r") as f:
    commands = f.read().splitlines()
    
for command in commands:
    if command.startswith("$ cd"):
        _, _, directory = command.split(" ")
        current_directory = change_directory(directory, current_directory)
    elif command[0].isdigit():
        size, _ = command.split(" ")
        update_directory_sizes(current_directory, size)
print("Part A:", sum([size for _, size in directory_sizes.items() if size <= 100_000]))

total_space = 70_000_000
currently_used_space = directory_sizes["/"]
available_space = total_space - currently_used_space
space_needed_for_update = 30_000_000
extra_space_needed = space_needed_for_update - available_space
print("Part B:", min([size for _, size in directory_sizes.items() if size >= extra_space_needed]))