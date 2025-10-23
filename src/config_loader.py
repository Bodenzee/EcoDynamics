import json
import argparse

def load_config(path="configs/default.json", overrides=None):
    with open(path, "r") as f:
        cfg = json.load(f)
    if overrides:
        cfg.update(overrides)
    return cfg

def parse_args():
    p = argparse.ArgumentParser(description="EcoDynamics runner")
    p.add_argument("--config", default="configs/default.json")
    p.add_argument("--model", choices=["abm","lv","holling"], help="Which model to run")
    p.add_argument("--steps", type=int)
    p.add_argument("--grid", type=str, help="WIDTHxHEIGHT")
    p.add_argument("--initial_prey", type=int)
    p.add_argument("--initial_predators", type=int)
    p.add_argument("--seed", type=int)
    p.add_argument("--out_dir", type=str)
    p.add_argument("--run_id", type=int)
    return p.parse_args()

