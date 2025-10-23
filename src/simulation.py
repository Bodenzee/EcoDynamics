import numpy as np
from scipy.integrate import solve_ivp
import pandas as pd
import json
import os
import datetime

class Simulation:

    def __init__(self, model, params, t_span, initial_state, t_eval=None):
        self.model = model
        self.params = params
        self.t_span = t_span
        self.initial_state = initial_state
        self.t_eval = t_eval if t_eval is not None else np.linspace(t_span[0], t_span[1], 500)

        # Create timestamped folder for data output
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        self.output_dir = os.path.join("data", f"run_{timestamp}")
        os.makedirs(self.output_dir, exist_ok=True)

    def run(self):
        """Executes the ODE simulation and returns structured results."""
        print(f"Running simulation: {self.model.__name__}")
        print(f"Parameters: {self.params}")

        # Integrate using SciPy's ODE solver
        sol = solve_ivp(
            fun=lambda t, y: self.model(t, y, **self.params),
            t_span=self.t_span,
            y0=self.initial_state,
            t_eval=self.t_eval,
            vectorized=False
        )

        if not sol.success:
            raise RuntimeError("Simulation failed to converge.")

        prey = sol.y[0]
        pred = sol.y[1]

        data = {
            "time": sol.t,
            "prey": prey,
            "predator": pred
        }

        df = pd.DataFrame(data)
        df.to_csv(os.path.join(self.output_dir, "timeseries.csv"), index=False)

        # Save metadata and summary
        summary = {
            "model": self.model.__name__,
            "params": self.params,
            "duration": float(self.t_span[1] - self.t_span[0]),
            "prey_final": float(prey[-1]),
            "pred_final": float(pred[-1]),
            "prey_mean": float(np.mean(prey)),
            "pred_mean": float(np.mean(pred))
        }
        with open(os.path.join(self.output_dir, "summary.json"), "w") as f:
            json.dump(summary, f, indent=4)

        print(f"✔ Simulation complete. Results saved to {self.output_dir}")
        return data
