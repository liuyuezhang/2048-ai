from BaseAI_3 import BaseAI
from copy import deepcopy
from my_2048_operation import *

# monotonicity
weight = [[pow(3, 3),  pow(3, 2),  pow(3, 1),  pow(3, 0)],
          [pow(3, 4),  pow(3, 5),  pow(3, 6),  pow(3, 7)],
          [pow(3, 11), pow(3, 10), pow(3, 9),  pow(3, 8)],
          [pow(3, 12), pow(3, 13), pow(3, 14), pow(3, 15)]]

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


# expect-minimax search
def expect_minimax(state, depth, is_max):
    if depth == 0:
        return heuristic(state)
    if is_max:
        v = float('-inf')
        for i in range(4):
            new_state = deepcopy(state)
            if move(new_state, i):
                v = max(v, expect_minimax(new_state, depth-1, False))
        return v
    else:
        total = 0
        cnt = 0
        minimum = float('inf')
        alpha = 1.0
        for cell in find_empty(state):
            new_state = deepcopy(state)
            new_state[cell[0]][cell[1]] = 2
            v = expect_minimax(new_state, depth-1, True)
            total += v
            cnt += 0.6
            minimum = min(minimum, v)
        avr = total/cnt
        res = alpha * avr + (1-alpha) * minimum
        return res


class PlayerAI(BaseAI):
    def getMove(self, grid):
        state = grid.map

        # be aware of deepcopy and []*4
        states = [deepcopy(state), deepcopy(state), deepcopy(state), deepcopy(state)]
        moved = [False]*4
        rewards = [-float("inf")]*4

        # 0: UP, 1:DOWN, 2:LEFT, 3:RIGHT
        for i in range(4):
            moved[i] = move(states[i], i)
            if moved[i]:
                rewards[i] = expect_minimax(states[i], 3, False)

        return rewards.index(max(rewards))
