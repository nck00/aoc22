import numpy as np

def update_visibility_row(line: np.ndarray, row: int) -> None:
    highest_tree = -1
    for col, tree in enumerate(line):
        if tree > highest_tree:
            visible[row][col] = True
            highest_tree = tree
        else:
            continue

def update_visibility_col(line: np.ndarray, col: int) -> None:
    highest_tree = -1
    for row, tree in enumerate(line):
        if tree > highest_tree:
            visible[row][col] = True
            highest_tree = tree
        else:
            continue

def update_visibility_row_flipped(line: np.ndarray, row: int) -> None:
    highest_tree = -1
    for col, tree in enumerate(line):
        if tree > highest_tree:
            visible[row][len(line)-1-col] = True
            highest_tree = tree
        else:
            continue

def update_visibility_col_flipped(line: np.ndarray, col: int) -> None:
    highest_tree = -1
    for row, tree in enumerate(line):
        if tree > highest_tree:
            visible[len(line)-1-row][col] = True
            highest_tree = tree
        else:
            continue

def update_scenic_score(row: int, col: int) -> None:
    initial_height = trees[row][col]
    max_row, max_col = (x - 1 for x in trees.shape)
    # top
    visible_top = 0
    if row != 0:
        for row_x in reversed(range(0, row)):
            if initial_height > trees[row_x][col] or row_x == row-1:
                visible_top += 1
            else:
                visible_top += 1
                break
    # down
    visible_down = 0
    if row != max_row:
        visible_down += 1
        if initial_height > trees[row+1][col]:
            for row_x in range(row+2, max_row):
                if not (initial_height > trees[row_x][col] or row_x == row+1):
                    visible_down += 1
                else:
                    visible_down += 1
                    break
    # right
    visible_right = 0
    if col != max_col:
        visible_right += 1
        if initial_height > trees[row][col+1]:
            for col_x in range(col+1, max_col):
                if initial_height > trees[row][col_x] or col_x == col+1:
                    visible_right += 1
                else:
                    visible_right += 1
                    break
    # left
    visible_left = 0
    if col != 0:
        visible_left += 1
        if initial_height > trees[row][col-1]:
            for col_x in reversed(range(0, col-1)):
                if initial_height > trees[row][col_x] or col_x == col-1:
                    visible_left += 1
                else:
                    visible_left += 1
                    break
    scenic_score = visible_top * visible_down * visible_right * visible_left
    scenic_scores[row][col] = scenic_score

trees = np.genfromtxt("input.txt", delimiter=1, dtype=int)
visible = np.zeros_like(trees, dtype=bool)
for i, row in enumerate(trees):
    update_visibility_row(row, i)
for i, col in enumerate(trees.T):
    update_visibility_col(col, i)
trees_flipped = np.flip(trees)
for i, row in enumerate(trees_flipped):
    update_visibility_row_flipped(row, len(row)-1-i)
for i, col in enumerate(trees_flipped.T):
    update_visibility_col_flipped(col, len(col)-1-i)
print("Part A:", visible.astype(int).sum())

scenic_scores = np.zeros_like(trees)
for i, row in enumerate(trees):
    for j, col in enumerate(row):
        update_scenic_score(i, j)
print("Part B:", scenic_scores.max())