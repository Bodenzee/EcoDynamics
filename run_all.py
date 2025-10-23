import json, time, os
from src.config_loader import load_config
from src.main import run_single

def variations(base):
    combos = [
        {"grid_width":20,"grid_height":20,"prey_reproduce_prob":0.05,"pred_mortality_prob":0.01},
        {"grid_width":30,"grid_height":30,"prey_reproduce_prob":0.05,"pred_mortality_prob":0.05},
        {"grid_width":40,"grid_height":40,"prey_reproduce_prob":0.05,"pred_mortality_prob":0.1},
        {"grid_width":20,"grid_height":20,"prey_reproduce_prob":0.03,"pred_mortality_prob":0.05},
        {"grid_width":30,"grid_height":30,"prey_reproduce_prob":0.08,"pred_mortality_prob":0.01},
        {"grid_width":40,"grid_height":40,"prey_reproduce_prob":0.08,"pred_mortality_prob":0.05},
        {"grid_width":20,"grid_height":20,"prey_reproduce_prob":0.03,"pred_mortality_prob":0.1},
        {"grid_width":30,"grid_height":30,"prey_reproduce_prob":0.08,"pred_mortality_prob":0.1},
        {"grid_width":40,"grid_height":40,"prey_reproduce_prob":0.03,"pred_mortality_prob":0.01},
        {"grid_width":30,"grid_height":30,"prey_reproduce_prob":0.06,"pred_mortality_prob":0.02}
    ]
    vars = []
    for i, c in enumerate(combos):
        v = dict(base); v.update(c)
        v["run_id"] = i+1; v["seed"] = base.get("seed",1)+i
        vars.append(v)
    return vars

def main():
    base = load_config("configs/default.json")
    vars = variations(base)
    index = []
    for cfg in vars:
        folder, summary = run_single(cfg)
        summary["params"] = {k:cfg[k] for k in ["grid_width","grid_height","prey_reproduce_prob","pred_mortality_prob"]}
        index.append(summary)
        with open(os.path.join(base["out_dir"],"runs_index.json"),"w") as f:
            json.dump(index,f,indent=2)
    print("All runs completed.")

if __name__ == "__main__":
    main()
