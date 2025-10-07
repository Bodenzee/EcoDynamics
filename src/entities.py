import random
from dataclasses import dataclass

@dataclass
class Prey:
    id: int
    x: int
    y: int
    energy: float
    reproduce_prob: float

    def step(self, env):
        dx, dy = random.choice([(0,0),(1,0),(-1,0),(0,1),(0,-1)])
        nx = (self.x + dx) % env.width
        ny = (self.y + dy) % env.height
        self.x, self.y = nx, ny

    def try_reproduce(self):
        if random.random() < self.reproduce_prob and self.energy > 1.0:
            self.energy /= 2.0
            return True
        return False

@dataclass
class Predator:
    id: int
    x: int
    y: int
    energy: float
    reproduce_prob: float
    mortality_prob: float

    def step(self, env):
        dx, dy = random.choice([(0,0),(1,0),(-1,0),(0,1),(0,-1)])
        nx = (self.x + dx) % env.width
        ny = (self.y + dy) % env.height
        self.x, self.y = nx, ny

    def try_reproduce(self):
        if random.random() < self.reproduce_prob and self.energy > 2.0:
            self.energy /= 2.0
            return True
        return False

    def try_starve(self):
        return self.energy <= 0 or random.random() < self.mortality_prob
