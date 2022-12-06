string_to_check_A = ""
A_found = False
string_to_check_B = ""
B_found = False

def check_string_all_unique(string: str) -> bool:
    for i in range(len(string)):
        for j in range(i+1, len(string)):
            if string[i] == string[j]:
                return False
    return True

with open("input.txt") as f:
    for line in f:
        for i, char in enumerate(line):
            string_to_check_A = line[i:i+4]
            string_to_check_B = line[i:i+14]
            if not A_found:
                if check_string_all_unique(string_to_check_A):
                    print("Part A:", i+4)
                    A_found = True
            if not B_found:
                if check_string_all_unique(string_to_check_B):
                    print("Part B:", i+14)
                    B_found = True