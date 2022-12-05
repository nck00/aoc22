
stack_1_A = ["S", "P", "H", "V", "F", "G"]
stack_2_A = ["M", "Z", "D", "V", "B", "F", "J", "G"]
stack_3_A = ["N", "J", "L", "M", "G"]
stack_4_A = ["P", "W", "D", "V", "Z", "G", "N"]
stack_5_A = ["B", "C", "R", "V"]
stack_6_A = ["Z", "L", "W", "P", "M", "S", "R", "V"]
stack_7_A = ["P", "H", "T"]
stack_8_A = ["V", "Z", "H", "C", "N", "S", "R", "Q"]
stack_9_A = ["J", "Q", "V", "P", "G", "L", "F"]
stack_0 = [""]
stacks_A = [stack_0, stack_1_A, stack_2_A, stack_3_A, stack_4_A, stack_5_A, stack_6_A, stack_7_A,
    stack_8_A, stack_9_A]

stack_1_B = ["S", "P", "H", "V", "F", "G"]
stack_2_B = ["M", "Z", "D", "V", "B", "F", "J", "G"]
stack_3_B = ["N", "J", "L", "M", "G"]
stack_4_B = ["P", "W", "D", "V", "Z", "G", "N"]
stack_5_B = ["B", "C", "R", "V"]
stack_6_B = ["Z", "L", "W", "P", "M", "S", "R", "V"]
stack_7_B = ["P", "H", "T"]
stack_8_B = ["V", "Z", "H", "C", "N", "S", "R", "Q"]
stack_9_B = ["J", "Q", "V", "P", "G", "L", "F"]
stacks_B = [stack_0, stack_1_B, stack_2_B, stack_3_B, stack_4_B, stack_5_B, stack_6_B, stack_7_B,
    stack_8_B, stack_9_B]


def move_crates_A(count: int, start_stack_nr: int, end_stack_nr: int, stacks: list) -> list:
    start_stack = int(start_stack_nr)
    end_stack = int(end_stack_nr)
    for x in range(int(count)):
        crate = stacks[start_stack].pop(0)
        stacks[end_stack].insert(0, crate)
    return stacks

def move_crates_B(count: int, start_stack_nr: int, end_stack_nr: int, stacks: list) -> list:
    start_stack = int(start_stack_nr)
    end_stack = int(end_stack_nr)
    crates_to_move = []
    for x in range(int(count)):
        crate = stacks[start_stack].pop(0)
        crates_to_move.append(crate)
    stacks[end_stack][:0] = crates_to_move
    return stacks

with open("input.txt") as f:
    for line in f:
        if not line.startswith("move"):
            continue
        _, count, _, start_stack, _, end_stack = line.strip("\n").split(" ")
        stacks_A = move_crates_A(count, start_stack, end_stack, stacks_A)
        stacks_B = move_crates_B(count, start_stack, end_stack, stacks_B)

print(f"Part A: {stacks_A[1][0]}{stacks_A[2][0]}{stacks_A[3][0]}{stacks_A[4][0]}"
f"{stacks_A[5][0]}{stacks_A[6][0]}{stacks_A[7][0]}{stacks_A[8][0]}{stacks_A[9][0]}")
print(f"Part B: {stacks_B[1][0]}{stacks_B[2][0]}{stacks_B[3][0]}{stacks_B[4][0]}"
f"{stacks_B[5][0]}{stacks_B[6][0]}{stacks_B[7][0]}{stacks_B[8][0]}{stacks_B[9][0]}")