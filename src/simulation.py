from scipy.integrate import solve_ivp
import numpy as np

class ODESimulation:
    def __init__(self, model_func, params: dict, t_span=(0,50), initial=(10,5), n_steps=500):
        self.model = model_func
        self.params = params
        self.t_span = t_span
        self.initial = initial
        self.n_steps = n_steps

    def run(self):
        t0, t1 = self.t_span
        t_eval = np.linspace(t0, t1, self.n_steps)
        sol = solve_ivp(lambda t, y: self.model(t, y, **self.params), (t0, t1), list(self.initial), t_eval=t_eval)
        data = {"time": sol.t.tolist(), "prey": sol.y[0].tolist(), "predator": sol.y[1].tolist()}
        return data
