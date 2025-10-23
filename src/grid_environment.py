# EcoDynamics/grid_environment.py
from collections import defaultdict

class GridEnvironment:

    def __init__(self, width: int, height: int):
        self.width = int(width)
        self.height = int(height)
        self.cells = defaultdict(list)

    def clear(self):
        self.cells.clear()

    def place(self, agent):
        self.cells[(agent.x, agent.y)].append(agent)

    def agents_at(self, x, y):
        return list(self.cells.get((x, y), []))
