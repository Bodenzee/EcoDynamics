import json, argparse

def load_config(path="configs/default.json", overrides=None):
    with open(path, "r") as f:
        cfg = json.load(f)
    if overrides:
        cfg.update(overrides)
    return cfg

def parse_cli_args():
    p = argparse.ArgumentParser(description="EcoDynamics ABM Runner")
    p.add_argument("--config", default="configs/default.json")
    p.add_argument("--steps", type=int)
    p.add_argument("--grid", type=str)
    p.add_argument("--initial_prey", type=int)
    p.add_argument("--initial_predators", type=int)
    p.add_argument("--seed", type=int)
    p.add_argument("--out_dir", type=str)
    p.add_argument("--run_id", type=int)
    a = p.parse_args()
    o = {}
    if a.steps: o["steps"] = a.steps
    if a.grid:
        try: w,h = map(int, a.grid.split("x")); o.update({"grid_width":w,"grid_height":h})
        except: pass
    if a.initial_prey is not None: o["initial_prey"] = a.initial_prey
    if a.initial_predators is not None: o["initial_predators"] = a.initial_predators
    if a.seed is not None: o["seed"] = a.seed
    if a.out_dir: o["out_dir"] = a.out_dir
    if a.run_id: o["run_id"] = a.run_id
    return a, o
