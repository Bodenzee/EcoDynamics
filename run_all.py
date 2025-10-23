import json, os, time
from src.config_loader import load_config
from src.main import run_abm

def make_variations(base):
    combos = [
        {"grid_width":20,"grid_height":20,"pred_mortality_prob":0.01,"prey_reproduce_prob":0.05},
        {"grid_width":30,"grid_height":30,"pred_mortality_prob":0.05,"prey_reproduce_prob":0.05},
        {"grid_width":40,"grid_height":40,"pred_mortality_prob":0.10,"prey_reproduce_prob":0.05},
        {"grid_width":20,"grid_height":20,"pred_mortality_prob":0.05,"prey_reproduce_prob":0.03},
        {"grid_width":30,"grid_height":30,"pred_mortality_prob":0.01,"prey_reproduce_prob":0.08},
        {"grid_width":40,"grid_height":40,"pred_mortality_prob":0.05,"prey_reproduce_prob":0.08},
        {"grid_width":20,"grid_height":20,"pred_mortality_prob":0.10,"prey_reproduce_prob":0.03},
        {"grid_width":30,"grid_height":30,"pred_mortality_prob":0.10,"prey_reproduce_prob":0.08},
        {"grid_width":40,"grid_height":40,"pred_mortality_prob":0.01,"prey_reproduce_prob":0.03},
        {"grid_width":30,"grid_height":30,"pred_mortality_prob":0.02,"prey_reproduce_prob":0.06}
    ]
    out = []
    for i,c in enumerate(combos):
        cfg = dict(base)
        cfg.update(c)
        cfg["run_id"] = i+1
        cfg["seed"] = base.get("seed", 42) + i
        out.append(cfg)
    return out

def main():
    base = load_config("configs/default.json")
    runs = make_variations(base)
    index = []
    out_dir = base.get("out_dir","data")
    os.makedirs(out_dir, exist_ok=True)
    for cfg in runs:
        t0 = time.time()
        folder, summary = run_abm(cfg)
        elapsed = time.time() - t0
        entry = {"run_id": cfg["run_id"], "params": {"grid_width": cfg["grid_width"], "grid_height": cfg["grid_height"], "prey_reproduce_prob": cfg["prey_reproduce_prob"], "pred_mortality_prob": cfg["pred_mortality_prob"]}, "duration_seconds": elapsed, "summary": summary, "folder": folder}
        index.append(entry)
        with open(os.path.join(out_dir, "runs_index.json"), "w") as f:
            json.dump(index, f, indent=2)
    print("Batch complete. Index saved to", os.path.join(out_dir,"runs_index.json"))

if __name__ == "__main__":
    main()
