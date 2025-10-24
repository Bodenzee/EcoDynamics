import os
import json
import pandas as pd
import matplotlib.pyplot as plt

def load_run_data(run_dir):
    csv_path = os.path.join(run_dir, "timeseries.csv")
    summary_path = os.path.join(run_dir, "summary.json")

    if not os.path.exists(csv_path) or not os.path.exists(summary_path):
        print(f" Skipping {run_dir}: Missing data files")
        return None, None

    df = pd.read_csv(csv_path)
    with open(summary_path) as f:
        summary = json.load(f)
    return df, summary

def plot_single_run(df, summary, output_dir):
    plt.figure(figsize=(8, 5))
    plt.plot(df["time"], df["prey"], label="Prey", linewidth=2)
    plt.plot(df["time"], df["predator"], label="Predator", linewidth=2)
    plt.xlabel("Time")
    plt.ylabel("Population")
    plt.title(f"{summary['model']} ({summary['id']})")
    plt.legend()
    plt.grid(True)

    os.makedirs(output_dir, exist_ok=True)
    file_path = os.path.join(output_dir, f"{summary['id']}.png")
    plt.savefig(file_path)
    plt.close()
    print(f" Saved: {file_path}")

def plot_combined(runs_data, output_dir):
    plt.figure(figsize=(10, 6))
    for summary, df in runs_data:
        label = f"{summary['id']} ({summary['model']})"
        plt.plot(df["time"], df["prey"], label=f"Prey – {label}", alpha=0.6)
        plt.plot(df["time"], df["predator"], linestyle="--", label=f"Pred – {label}", alpha=0.6)

    plt.xlabel("Time")
    plt.ylabel("Population")
    plt.title("EcoDynamics Batch Comparison – All Runs")
    plt.legend(fontsize=7, loc="upper right", ncol=2)
    plt.grid(True)
    os.makedirs(output_dir, exist_ok=True)
    file_path = os.path.join(output_dir, "combined_all_runs.png")
    plt.savefig(file_path)
    plt.close()
    print(f"Saved combined plot: {file_path}")


def main():
    data_dir = "data"
    plots_dir = os.path.join(data_dir, "plots")

    summaries = [f for f in os.listdir(data_dir) if f.startswith("runs_index_") and f.endswith(".json")]
    if not summaries:
        print("No batch summary files found. Please run run_all.py first.")
        return

    latest_file = sorted(summaries)[-1]
    summary_path = os.path.join(data_dir, latest_file)
    print(f"Loading batch summary: {latest_file}")

    with open(summary_path) as f:
        all_runs = json.load(f)

    runs_data = []

    for run in all_runs:
        run_dir = os.path.dirname(summary_path).replace("data", "data")
        possible_dirs = [os.path.join("data", d) for d in os.listdir("data") if run["id"].split("_")[0] in d]
        if not possible_dirs:
            continue

        df, summary = load_run_data(possible_dirs[0])
        if df is not None and summary is not None:
            plot_single_run(df, summary, plots_dir)
            runs_data.append((summary, df))

    if runs_data:
        plot_combined(runs_data, plots_dir)
        print("\n All plots generated successfully.")
    else:
        print("No valid run data found for plotting.")

if __name__ == "__main__":
    main()
