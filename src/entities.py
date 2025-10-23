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
        # random move (4-neighborhood + stay)
        dx, dy = random.choice([(0,0),(1,0),(-1,0),(0,1),(0,-1)])
        self.x = (self.x + dx) % env.width
        self.y = (self.y + dy) % env.height

    def try_reproduce(self):
        if self.energy > 1.0 and random.random() < self.reproduce_prob:
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
        self.x = (self.x + dx) % env.width
        self.y = (self.y + dy) % env.height

    def try_reproduce(self):
        if self.energy > 2.0 and random.random() < self.reproduce_prob:
            self.energy /= 2.0
            return True
        return False

    def should_die(self):
        return self.energy <= 0 or random.random() < self.mortality_prob
