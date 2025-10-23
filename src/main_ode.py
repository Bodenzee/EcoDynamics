import matplotlib.pyplot as plt
from models import lotka_volterra, logistic_hollingII
from simulation import Simulation

def run_lotka_volterra():
    params = {"alpha": 1.0, "beta": 0.1, "gamma": 1.5, "delta": 0.075}
    sim = Simulation(model=lotka_volterra, params=params, t_span=(0, 50), initial_state=(40, 9))
    data = sim.run()
    plot_results(data, "Lotka-Volterra")

def run_logistic_hollingII():
    params = {"r": 1.0, "K": 50, "a": 0.5, "h": 0.1, "gamma": 0.5, "e": 0.75}
    sim = Simulation(model=logistic_hollingII, params=params, t_span=(0, 50), initial_state=(40, 9))
    data = sim.run()
    plot_results(data, "Logistic + Holling II")

def plot_results(data, title):
    plt.plot(data["time"], data["prey"], label="Prey")
    plt.plot(data["time"], data["predator"], label="Predator")
    plt.xlabel("Time")
    plt.ylabel("Population")
    plt.title(title)
    plt.legend()
    plt.show()

if __name__ == "__main__":
    run_lotka_volterra()
    run_logistic_hollingII()
