import numpy as np
from scipy.integrate import solve_ivp
from data_collector import DataCollector

class Simulation:
    def __init__(self, model, params, t_span=(0, 50), initial_state=(10, 5)):
        self.model = model
        self.params = params
        self.t_span = t_span
        self.initial_state = initial_state
        self.data_collector = DataCollector()

    def run(self):
        def wrapped_model(t, state):
            return self.model(t, state, **self.params)

        sol = solve_ivp(wrapped_model, self.t_span, self.initial_state, dense_output=True)

        for t, prey, pred in zip(sol.t, sol.y[0], sol.y[1]):
            self.data_collector.record(t, prey, pred)

        return self.data_collector.get_data()
