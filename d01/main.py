calories_per_elf = []
current = 0
with open("input.txt") as f:
    for line in f:
        if line == "\n":
            calories_per_elf.append(current)
            current = 0
        else:
            current += int(line)
print(f"Part A: {max(calories_per_elf)}")
calories_per_elf.sort()
print(f"Part B: {sum(calories_per_elf[-3:])}")
