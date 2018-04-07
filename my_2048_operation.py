from random import randint

directionVectors = (UP_VEC, DOWN_VEC, LEFT_VEC, RIGHT_VEC) = ((-1, 0), (1, 0), (0, -1), (0, 1))
vecIndex = [UP, DOWN, LEFT, RIGHT] = range(4)


# Move
# Merge Tiles
def merge(cells):
    if len(cells) <= 1:
        return cells

    i = 0

    while i < len(cells) - 1:
        if cells[i] == cells[i+1]:
            cells[i] *= 2

            del cells[i+1]

        i += 1


def move_up(state):
    r = range(4)

    moved = False

    for j in range(4):
        cells = []

        for i in r:
            cell = state[i][j]

            if cell != 0:
                cells.append(cell)

        merge(cells)

        for i in r:
            value = cells.pop(0) if cells else 0

            if state[i][j] != value:
                moved = True

            state[i][j] = value

    return moved


def move_down(state):
    r = range(3, -1, -1)

    moved = False

    for j in range(4):
        cells = []

        for i in r:
            cell = state[i][j]

            if cell != 0:
                cells.append(cell)

        merge(cells)

        for i in r:
            value = cells.pop(0) if cells else 0

            if state[i][j] != value:
                moved = True

            state[i][j] = value

    return moved


def move_left(state):
    r = range(4)

    moved = False

    for i in range(4):
        cells = []

        for j in r:
            cell = state[i][j]

            if cell != 0:
                cells.append(cell)

        merge(cells)

        for j in r:
            value = cells.pop(0) if cells else 0

            if state[i][j] != value:
                moved = True

            state[i][j] = value

    return moved


def move_right(state):
    r = range(3, -1, -1)

    moved = False

    for i in range(4):
        cells = []

        for j in r:
            cell = state[i][j]

            if cell != 0:
                cells.append(cell)

        merge(cells)

        for j in r:
            value = cells.pop(0) if cells else 0

            if state[i][j] != value:
                moved = True

            state[i][j] = value

    return moved


def move(state, i):
    if i == 0:
        return move_up(state)
    if i == 1:
        return move_down(state)
    if i == 2:
        return move_left(state)
    if i == 3:
        return move_right(state)


# Put
# Return All the Empty Cells
def find_empty(state):
    cells = []

    for x in range(4):
        for y in range(4):
            if state[x][y] == 0:
                cells.append((x, y))

    return cells


def put(state):
    cells = find_empty(state)
    if len(cells) == 0:
        return state, False
    cells[randint(0, len(cells) - 1)]