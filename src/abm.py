import random
import time
import json
from collections import defaultdict
from src.entities import Prey, Predator

class GridEnvironment:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.cells = defaultdict(list)

    def clear_cells(self):
        self.cells = defaultdict(list)

    def place_agent(self, agent):
        self.cells[(agent.x, agent.y)].append(agent)

class ABMSimulation:
    def __init__(self, config, data_collector, seed=None):
        if seed is not None:
            random.seed(seed)
        self.config = config
        self.dc = data_collector
        self.step_count = 0
        self.grid = GridEnvironment(config["grid_width"], config["grid_height"])
        self.prey_list = []
        self.pred_list = []
        self.next_agent_id = 1
        self._spawn_initial_agents(config["initial_prey"], config["initial_predators"])

        self.prey_reproduce_prob = config["prey_reproduce_prob"]
        self.pred_reproduce_prob = config["pred_reproduce_prob"]
        self.pred_mortality_prob = config["pred_mortality_prob"]
        self.pred_energy_gain = config["pred_energy_gain"]
        self.prey_energy_gain = config["prey_energy_gain"]

    def _spawn_initial_agents(self, n_prey, n_pred):
        for _ in range(n_prey):
            x = random.randrange(self.grid.width)
            y = random.randrange(self.grid.height)
            prey = Prey(self.next_agent_id, x, y, 1.0, self.prey_reproduce_prob)
            self.next_agent_id += 1
            self.prey_list.append(prey)
        for _ in range(n_pred):
            x = random.randrange(self.grid.width)
            y = random.randrange(self.grid.height)
            pred = Predator(self.next_agent_id, x, y, 2.0,
                            self.pred_reproduce_prob, self.pred_mortality_prob)
            self.next_agent_id += 1
            self.pred_list.append(pred)

    def step(self):
        self.step_count += 1
        self.grid.clear_cells()
        for a in self.prey_list + self.pred_list:
            self.grid.place_agent(a)

        new_prey = []
        events = []
        for prey in list(self.prey_list):
            prey.step(self.grid)
            prey.energy += self.prey_energy_gain
            if prey.try_reproduce():
                child = Prey(self.next_agent_id, prey.x, prey.y,
                             prey.energy/2.0, self.prey_reproduce_prob)
                self.next_agent_id += 1
                new_prey.append(child)
                events.append({"type": "birth", "species": "prey", "time": self.step_count})
        self.prey_list.extend(new_prey)

        new_preds = []
        dead_preds = []
        for pred in list(self.pred_list):
            pred.step(self.grid)
            same = [p for p in self.prey_list if (p.x, p.y) == (pred.x, pred.y)]
            if same:
                victim = random.choice(same)
                pred.energy += self.pred_energy_gain
                try:
                    self.prey_list.remove(victim)
                    events.append({"type": "predation", "predator": pred.id, "time": self.step_count})
                except ValueError:
                    pass
            else:
                pred.energy -= 0.5
            if pred.try_reproduce():
                child = Predator(self.next_agent_id, pred.x, pred.y,
                                 pred.energy/2.0, self.pred_reproduce_prob, self.pred_mortality_prob)
                self.next_agent_id += 1
                new_preds.append(child)
                events.append({"type": "birth", "species": "predator", "time": self.step_count})
            if pred.try_starve():
                dead_preds.append(pred)
                events.append({"type": "death", "species": "predator", "time": self.step_count})
        for d in dead_preds:
            if d in self.pred_list:
                self.pred_list.remove(d)
        self.pred_list.extend(new_preds)

        metrics = {"step": self.step_count,
                   "prey_count": len(self.prey_list),
                   "pred_count": len(self.pred_list)}
        self.dc.record_step(metrics)
        for e in events:
            self.dc.record_event(e)

    def run(self, steps):
        t0 = time.time()
        for _ in range(steps):
            self.step()
            if len(self.prey_list) == 0 and len(self.pred_list) == 0:
                break
        duration = time.time() - t0
        return {"steps": self.step_count, "duration_seconds": duration,
                "final_prey": len(self.prey_list), "final_predators": len(self.pred_list)}
