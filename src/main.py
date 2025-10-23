import time
from src.config_loader import load_config, parse_cli_args
from src.data_collector import DataCollector
from src.abm import ABMSimulation

def run_single(config):
    dc = DataCollector(config.get("out_dir", "data"))
    sim = ABMSimulation(config, dc, seed=config.get("seed", None))
    t0 = time.time()
    summary = sim.run(config.get("steps", 200))
    dur = time.time() - t0
    config["duration"] = dur
    folder, result = dc.save_run(config.get("run_id", 1), config)
    result.update({"run_id": config.get("run_id", 1), "duration": dur})
    print(f"Run {config.get('run_id')} complete: {result}")
    return folder, result

def main():
    args, overrides = parse_cli_args()
    cfg = load_config(args.config, overrides)
    run_single(cfg)

if __name__ == "__main__":
    main()
