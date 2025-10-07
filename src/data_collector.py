import csv, json, os, time

class DataCollector:
    def __init__(self, out_dir):
        self.out_dir = out_dir
        os.makedirs(out_dir, exist_ok=True)
        self.timeseries = []
        self.events = []

    def record_step(self, metrics):
        self.timeseries.append(metrics)

    def record_event(self, event):
        self.events.append(event)

    def save_run(self, run_id, config):
        folder = os.path.join(self.out_dir, f"run_{run_id:03d}")
        os.makedirs(folder, exist_ok=True)

        if self.timeseries:
            keys = self.timeseries[0].keys()
            with open(os.path.join(folder, "timeseries.csv"), "w", newline="") as f:
                w = csv.DictWriter(f, fieldnames=keys)
                w.writeheader(); w.writerows(self.timeseries)

        if self.events:
            keys = sorted({k for e in self.events for k in e})
            with open(os.path.join(folder, "events.csv"), "w", newline="") as f:
                w = csv.DictWriter(f, fieldnames=keys)
                w.writeheader(); w.writerows(self.events)

        with open(os.path.join(folder, "config.json"), "w") as f:
            json.dump(config, f, indent=2)

        summary = {
            "steps_recorded": len(self.timeseries),
            "events_recorded": len(self.events)
        }
        with open(os.path.join(folder, "summary.json"), "w") as f:
            json.dump(summary, f, indent=2)
        return folder, summary
