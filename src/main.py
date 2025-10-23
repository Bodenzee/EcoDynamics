import time
import os
from src.config_loader import load_config, parse_args
from src.data_collector import DataCollector
from src.abm import ABMSimulation
from src.simulation import ODESimulation
from src.models.lotka_volterra import lotka_volterra
from src.models.logistic_hollingII import logistic_hollingII
import matplotlib.pyplot as plt
import json

def run_abm(cfg):
    dc = DataCollector(cfg.get("out_dir","data"))
    sim = ABMSimulation(cfg, dc, seed=cfg.get("seed", None))
    t0 = time.time()
    summary = sim.run(cfg.get("steps", 200))
    duration = time.time() - t0
    cfg_copy = dict(cfg); cfg_copy["actual_duration_seconds"] = duration
    folder, summ = dc.save(cfg.get("run_id",1), cfg_copy)
    summ.update({"duration_seconds": duration, "run_id": cfg.get("run_id",1)})
    print(f"ABM run complete: {summ}")
    return folder, summ

def run_ode(model_key, cfg):
    if model_key == "lv":
        params = cfg.get("lv_params", {"alpha":1.0,"beta":0.1,"gamma":1.5,"delta":0.075})
        initial = cfg.get("lv_initial", (40,9))
        sim = ODESimulation(lotka_volterra, params, t_span=(0,50), initial=initial, n_steps=500)
        data = sim.run()
        return data
    else:
        params = cfg.get("holling_params", {"r":1.0,"K":50,"a":0.5,"h":0.1,"gamma":0.5,"e":0.75})
        initial = cfg.get("holling_initial", (40,9))
        sim = ODESimulation(logistic_hollingII, params, t_span=(0,50), initial=initial, n_steps=500)
        data = sim.run()
        return data

def plot_timeseries(data, title="Simulation"):
    plt.figure(figsize=(8,4))
    plt.plot(data["time"], data["prey"], label="Prey")
    plt.plot(data["time"], data["predator"], label="Predator")
    plt.xlabel("Time")
    plt.ylabel("Population")
    plt.title(title)
    plt.legend()
    plt.tight_layout()
    plt.show()

def main():
    args = parse_args()
    cfg = load_config(args.config)
    # apply CLI overrides
    overrides = {}
    if args.steps: overrides["steps"] = args.steps
    if args.grid:
        try:
            w,h = args.grid.split("x"); overrides["grid_width"]=int(w); overrides["grid_height"]=int(h)
        except: pass
    if args.initial_prey is not None: overrides["initial_prey"]=args.initial_prey
    if args.initial_predators is not None: overrides["initial_predators"]=args.initial_predators
    if args.seed is not None: overrides["seed"]=args.seed
    if args.out_dir: overrides["out_dir"]=args.out_dir
    if args.run_id: overrides["run_id"]=args.run_id
    cfg.update(overrides)

    model = args.model or cfg.get("model","abm")
    if model == "abm":
        run_abm(cfg)
    elif model in ("lv","holling"):
        data = run_ode(model, cfg)
        if model == "lv":
            plot_timeseries(data, "Lotka-Volterra")
        else:
            plot_timeseries(data, "Logistic + Holling II")

if __name__ == "__main__":
    main()
