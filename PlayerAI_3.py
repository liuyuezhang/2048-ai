from BaseAI_3 import BaseAI
from search import policy
import time


class PlayerAI(BaseAI):
    def getMove(self, grid):
        t = time.time()
        action = policy(grid.map)
        print(str(time.time() - t))

        return action
