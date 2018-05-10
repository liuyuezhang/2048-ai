from BaseAI_3 import BaseAI
from search import policy


class PlayerAI(BaseAI):
    def getMove(self, grid):
        return policy(grid.map)
