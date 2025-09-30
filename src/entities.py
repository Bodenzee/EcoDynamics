class Prey:
    def __init__(self, growth_rate: float, carrying_capacity: float):
        self.growth_rate = growth_rate
        self.carrying_capacity = carrying_capacity

class Predator:
    def __init__(self, mortality_rate: float, efficiency: float):
        self.mortality_rate = mortality_rate
        self.efficiency = efficiency

class Environment:
    def __init__(self, carrying_capacity: float):
        self.carrying_capacity = carrying_capacity
