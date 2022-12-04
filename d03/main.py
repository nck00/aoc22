total_priority_A = 0
total_priority_B = 0

def get_priority(char: str) -> int:
    priority_dict = {
    "a": 1,
    "b": 2,
    "c": 3,
    "d": 4,
    "e": 5,
    "f": 6,
    "g": 7,
    "h": 8,
    "i": 9,
    "j": 10,
    "k": 11,
    "l": 12,
    "m": 13,
    "n": 14,
    "o": 15,
    "p": 16,
    "q": 17,
    "r": 18,
    "s": 19,
    "t": 20,
    "u": 21,
    "v": 22,
    "w": 23,
    "x": 24,
    "y": 25,
    "z": 26,
    "A": 27,
    "B": 28,
    "C": 29,
    "D": 30,
    "E": 31,
    "F": 32,
    "G": 33,
    "H": 34,
    "I": 35,
    "J": 36,
    "K": 37,
    "L": 38,
    "M": 39,
    "N": 40,
    "O": 41,
    "P": 42,
    "Q": 43,
    "R": 44,
    "S": 45,
    "T": 46,
    "U": 47,
    "V": 48,
    "W": 49,
    "X": 50,
    "Y": 51,
    "Z": 52
    }
    return priority_dict[char]

groups = []
group_of_3 = []
with open("input.txt") as f:
    for line in f:
        line = line.strip("\n")
        group_of_3.append(line)
        if len(group_of_3) == 3:
            groups.append(group_of_3)
            group_of_3 = []
        first, second = line[:len(line)//2], line[len(line)//2:]
        seen = []
        for char in first:
            if char in second and char not in seen:
                seen.append(char)
                total_priority_A += get_priority(char)
print("Part A:", total_priority_A)

for first, second, third in groups:
    seen = []
    for char in first:
        if char in second and char in third and char not in seen:
            seen.append(char)
            total_priority_B += get_priority(char)
print("Part B:", total_priority_B)
