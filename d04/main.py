assignment_pairs_fully_contained = 0
assignment_pairs_overlap = 0

def get_list(range_string: str) -> list:
    start, end = range_string.split("-")
    return [x for x in  range(int(start), int(end)+1)]

with open("input.txt") as f:
    for line in f:
        first, second = line.strip("\n").split(",")
        first_list = get_list(first)
        second_list = get_list(second)
        if (all(x in first_list for x in second_list) or
            all(y in second_list for y in first_list)):
            assignment_pairs_fully_contained += 1
        if (any(x in first_list for x in second_list) or
            any(y in second_list for y in first_list)):
            assignment_pairs_overlap += 1
print("Part A:", assignment_pairs_fully_contained)
print("Part B:", assignment_pairs_overlap)