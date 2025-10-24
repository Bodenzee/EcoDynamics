
import os, csv, json, time

class DataCollector:
    def __init__(self, out_dir="data"):
        self.out_dir = out_dir
        os.makedirs(self.out_dir, exist_ok=True)
        self.timeseries = [] 
        self.events = []  
        self.created = time.time()

    def record_step(self, metrics: dict):
        self.timeseries.append(metrics)

    def record_event(self, event: dict):
        self.events.append(event)

    def save(self, run_id: int, config: dict):
        folder = os.path.join(self.out_dir, f"run_{run_id:03d}")
        os.makedirs(folder, exist_ok=True)


        if self.timeseries:
            keys = list(self.timeseries[0].keys())
            with open(os.path.join(folder, "timeseries.csv"), "w", newline="") as f:
                writer = csv.DictWriter(f, fieldnames=keys)
                writer.writeheader()
                writer.writerows(self.timeseries)


        if self.events:
            keys = sorted({k for e in self.events for k in e})
            with open(os.path.join(folder, "events.csv"), "w", newline="") as f:
                writer = csv.DictWriter(f, fieldnames=keys)
                writer.writeheader()
                for e in self.events:
                    writer.writerow({k: e.get(k, "") for k in keys})

        with open(os.path.join(folder, "config.json"), "w") as f:
            json.dump(config, f, indent=2)

        summary = self._build_summary()
        with open(os.path.join(folder, "summary.json"), "w") as f:
            json.dump(summary, f, indent=2)

        return folder, summary

    def _build_summary(self):
        prey = [s["prey_count"] for s in self.timeseries] if self.timeseries else []
        pred = [s["pred_count"] for s in self.timeseries] if self.timeseries else []
        summary = {
            "steps_recorded": len(self.timeseries),
            "events_recorded": len(self.events),
            "prey_mean": sum(prey)/len(prey) if prey else 0,
            "pred_mean": sum(pred)/len(pred) if pred else 0,
            "prey_max": max(prey) if prey else 0,
            "pred_max": max(pred) if pred else 0,
            "prey_min": min(prey) if prey else 0,
            "pred_min": min(pred) if pred else 0
        }
        return summary
