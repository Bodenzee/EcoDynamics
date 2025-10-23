import os
import json
from datetime import datetime
from src.simulation import Simulation
from src.models import lotka_volterra, logistic_hollingII

CONFIGS = [
    {
        "id": "run01_lv_baseline",
        "model": lotka_volterra,
        "params": {"alpha": 1.0, "beta": 0.1, "gamma": 1.5, "delta": 0.075},
        "initial_state": (40, 9),
        "t_span": (0, 50)
    },
    {
        "id": "run02_lv_high_predation",
        "model": lotka_volterra,
        "params": {"alpha": 1.0, "beta": 0.15, "gamma": 1.5, "delta": 0.075},
        "initial_state": (40, 9),
        "t_span": (0, 50)
    },
    {
        "id": "run03_lv_fast_growth",
        "model": lotka_volterra,
        "params": {"alpha": 1.2, "beta": 0.1, "gamma": 1.5, "delta": 0.075},
        "initial_state": (40, 9),
        "t_span": (0, 50)
    },
    {
        "id": "run04_lv_longer_span",
        "model": lotka_volterra,
        "params": {"alpha": 1.0, "beta": 0.1, "gamma": 1.5, "delta": 0.075},
        "initial_state": (40, 9),
        "t_span": (0, 100)
    },
    {
        "id": "run05_log_baseline",
        "model": logistic_hollingII,
        "params": {"r": 1.0, "K": 50, "a": 0.5, "h": 0.1, "gamma": 0.5, "e": 0.75},
        "initial_state": (40, 9),
        "t_span": (0, 50)
    },
    {
        "id": "run06_log_high_capacity",
        "model": logistic_hollingII,
        "params": {"r": 1.0, "K": 80, "a": 0.5, "h": 0.1, "gamma": 0.5, "e": 0.75},
        "initial_state": (40, 9),
        "t_span": (0, 50)
    },
    {
        "id": "run07_log_low_predation",
        "model": logistic_hollingII,
        "params": {"r": 1.0, "K": 50, "a": 0.3, "h": 0.1, "gamma": 0.5, "e": 0.75},
        "initial_state": (40, 9),
        "t_span": (0, 50)
    },
    {
        "id": "run08_log_high_efficiency",
        "model": logistic_hollingII,
        "params": {"r": 1.0, "K": 50, "a": 0.5, "h": 0.1, "gamma": 0.5, "e": 0.95},
        "initial_state": (40, 9),
        "t_span": (0, 50)
    },
    {
        "id": "run09_log_long_span",
        "model": logistic_hollingII,
        "params": {"r": 1.0, "K": 50, "a": 0.5, "h": 0.1, "gamma": 0.5, "e": 0.75},
        "initial_state": (40, 9),
        "t_span": (0, 100)
    },
    {
        "id": "run10_log_fast_growth",
        "model": logistic_hollingII,
        "params": {"r": 1.5, "K": 50, "a": 0.5, "h": 0.1, "gamma": 0.5, "e": 0.75},
        "initial_state": (40, 9),
        "t_span": (0, 50)
    }
]

def run_single(cfg):
    sim = Simulation(
        model=cfg["model"],
        params=cfg["params"],
        t_span=cfg["t_span"],
        initial_state=cfg["initial_state"]
    )
    data = sim.run()

    summary_path = os.path.join(sim.output_dir, "summary.json")
    with open(summary_path) as f:
        summary = json.load(f)

    summary["id"] = cfg["id"]
    return summary

def main():
    print("\n🔁 Running batch simulations for EcoDynamics...\n")
    os.makedirs("data", exist_ok=True)
    summaries = []

    for cfg in CONFIGS:
        print(f"--- Starting {cfg['id']} ---")
        result = run_single(cfg)
        summaries.append(result)

    index_file = os.path.join("data", f"runs_index_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json")
    with open(index_file, "w") as f:
        json.dump(summaries, f, indent=4)

    print(f"\n✅ Batch complete. {len(summaries)} runs saved in {index_file}\n")

if __name__ == "__main__":
    main()

