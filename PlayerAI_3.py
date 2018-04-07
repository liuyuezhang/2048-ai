from BaseAI_3 import BaseAI
from search import *
import time


class PlayerAI(BaseAI):
    def getMove(self, grid):
        t = time.time()
        state = grid.map

        # be aware of deepcopy and []*4
        states = [deepcopy(state), deepcopy(state), deepcopy(state), deepcopy(state)]
        moved = [False]*4
        rewards = [-float("inf")]*4

        # 0: UP, 1:DOWN, 2:LEFT, 3:RIGHT
        for i in range(4):
            moved[i] = move(states[i], i)
            if moved[i]:
                rewards[i] = expectimax(states[i], 3, False)
        print(str(time.time() - t))
        return rewards.index(max(rewards))
