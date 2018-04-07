from copy import deepcopy
from my_2048_operation import *

# monotonicity
weight = [[1,  1,  1,  1],
          [3,  3,  3,  3],
          [pow(3, 4),     pow(3, 4) - 1, pow(3, 3),  pow(3, 2)],
          [pow(3, 4) + 1, pow(3, 6),     pow(3, 7),  pow(3, 8)]]

# smoothness
k = 1


# heuristic function
def heuristic(state):
    reward = 0
    max_tile = 0
    for i in range(4):
        for j in range(4):
            # monotonicity
            reward += weight[i][j] * state[i][j]
            # smoothness
            if i - 1 >= 0:
                reward -= k * abs(state[i][j] - state[i - 1][j])
            if i + 1 < 4:
                reward -= k * abs(state[i][j] - state[i + 1][j])
            if j - 1 >= 0:
                reward -= k * abs(state[i][j] - state[i][j - 1])
            if j + 1 < 4:
                reward -= k * abs(state[i][j] - state[i][j + 1])
            # empty tiles
            if state[i][j] == 0:
                reward += 2
            # find max tile
            if state[i][j] > max_tile:
                max_tile = state[i][j]
    # avoid max tile leaving
    if state[3][3] != max_tile and state[3][3] != 0:
        reward -= state[3][3] * weight[3][3]

    return reward


# minimax search with alpha beta pruning
def minimax(state, depth, alpha, beta, is_max):
    if depth == 0:
        return heuristic(state)
    if is_max:
        v = float('-inf')
        for i in range(4):
            new_state = deepcopy(state)
            if move(new_state, i):
                v = max(v, minimax(new_state, depth-1, alpha, beta, False))
                alpha = max(alpha, v)
                if beta < alpha:
                    break
        return v
    else:
        v = float('inf')
        for cell in find_empty(state):
            new_state = deepcopy(state)
            new_state[cell[0]][cell[1]] = 2
            v = min(v, minimax(new_state, depth-1, alpha, beta, True))
            beta = min(beta, v)
            if beta < alpha:
                break
        return v


# expectimax search
def expectimax(state, depth, is_max):
    if depth == 0:
        return heuristic(state)
    if is_max:
        v = float('-inf')
        for i in range(4):
            new_state = deepcopy(state)
            if move(new_state, i):
                v = max(v, expectimax(new_state, depth-1, False))
        return v
    else:
        total = 0
        cnt = 0
        for cell in find_empty(state):
            new_state = deepcopy(state)
            new_state[cell[0]][cell[1]] = 2
            v = expectimax(new_state, depth-1, True)
            total += v
            cnt += 1
        avr = total/cnt
        return avr
