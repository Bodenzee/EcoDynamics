import argparse
import os
import pandas as pd
import matplotlib.pyplot as plt

def plot_single(run_folder, show=True, save=None):
    path = os.path.join(run_folder, "timeseries.csv")
    if not os.path.exists(path):
        raise FileNotFoundError(path)
    df = pd.read_csv(path)
    plt.figure(figsize=(8,4))
    plt.plot(df["step"], df["prey_count"], label="Prey")
    plt.plot(df["step"], df["pred_count"], label="Predator")
    plt.xlabel("Step")
    plt.ylabel("Population")
    plt.title(f"Run {os.path.basename(run_folder)}")
    plt.legend()
    plt.tight_layout()
    if save:
        plt.savefig(save)
    if show:
        plt.show()

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--run", default="data/run_001", help="Run folder (e.g. data/run_001)")
    p.add_argument("--save", help="Save plot to file")
    args = p.parse_args()
    plot_single(args.run, show=True, save=args.save)

if __name__ == "__main__":
    main()
