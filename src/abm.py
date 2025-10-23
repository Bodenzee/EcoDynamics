
import random
import time
from src.entities import Prey, Predator
from src.grid_environment import GridEnvironment

class ABMSimulation:
    def __init__(self, config: dict, data_collector, seed=None):
        if seed is not None:
            random.seed(seed)
        self.config = config
        self.dc = data_collector
        self.step_count = 0
        self.grid = GridEnvironment(config.get("grid_width", 20), config.get("grid_height", 20))
        self.prey = []
        self.preds = []
        self.next_id = 1

        self.prey_reproduce_prob = config.get("prey_reproduce_prob", 0.05)
        self.pred_reproduce_prob = config.get("pred_reproduce_prob", 0.02)
        self.pred_mortality_prob = config.get("pred_mortality_prob", 0.01)
        self.pred_energy_gain = config.get("pred_energy_gain", 3.0)
        self.prey_energy_gain = config.get("prey_energy_gain", 0.5)

        self._spawn_initial_agents(config.get("initial_prey", 100), config.get("initial_predators", 20))

    def _spawn_initial_agents(self, n_prey: int, n_pred: int):
        for _ in range(int(n_prey)):
            x = random.randrange(self.grid.width)
            y = random.randrange(self.grid.height)
            p = Prey(self.next_id, x, y, energy=1.0, reproduce_prob=self.prey_reproduce_prob)
            self.next_id += 1
            self.prey.append(p)
        for _ in range(int(n_pred)):
            x = random.randrange(self.grid.width)
            y = random.randrange(self.grid.height)
            pr = Predator(self.next_id, x, y, energy=2.0,
                          reproduce_prob=self.pred_reproduce_prob, mortality_prob=self.pred_mortality_prob)
            self.next_id += 1
            self.preds.append(pr)

    def step(self):
        self.step_count += 1
        self.grid.clear()
        for a in self.prey + self.preds:
            self.grid.place(a)

        events = []
        
        new_prey = []
        
        for p in list(self.prey):
            p.step(self.grid)
            p.energy += self.prey_energy_gain
            if p.try_reproduce():
                child = Prey(self.next_id, p.x, p.y, energy=p.energy/2.0, reproduce_prob=self.prey_reproduce_prob)
                self.next_id += 1
                new_prey.append(child)
                events.append({"type":"birth","species":"prey","agent":child.id,"time":self.step_count})
        self.prey.extend(new_prey)

        new_preds = []
        dead_preds = []
        for pr in list(self.preds):
            pr.step(self.grid)
            victims = [a for a in self.prey if (a.x, a.y) == (pr.x, pr.y)]
            if victims:
                victim = random.choice(victims)
                pr.energy += self.pred_energy_gain
                try:
                    self.prey.remove(victim)
                    events.append({"type":"predation","predator":pr.id,"prey":victim.id,"time":self.step_count})
                except ValueError:
                    pass
            else:
                pr.energy -= 0.5

            if pr.try_reproduce():
                child = Predator(self.next_id, pr.x, pr.y, energy=pr.energy/2.0,
                                 reproduce_prob=self.pred_reproduce_prob, mortality_prob=self.pred_mortality_prob)
                self.next_id += 1
                new_preds.append(child)
                events.append({"type":"birth","species":"predator","agent":child.id,"time":self.step_count})

            if pr.should_die():
                dead_preds.append(pr)
                events.append({"type":"death","species":"predator","agent":pr.id,"time":self.step_count})

        for d in dead_preds:
            try:
                self.preds.remove(d)
            except ValueError:
                pass
        self.preds.extend(new_preds)

        metrics = {"step": self.step_count, "prey_count": len(self.prey), "pred_count": len(self.preds)}
        self.dc.record_step(metrics)
        for e in events:
            self.dc.record_event(e)

        return len(self.prey) == 0 and len(self.preds) == 0

    def run(self, steps: int, realtime_log=False):
        t0 = time.time()
        for _ in range(int(steps)):
            extinct = self.step()
            if realtime_log and self.step_count % 20 == 0:
                print(f"Step {self.step_count}: prey={len(self.prey)} pred={len(self.preds)}")
            if extinct:
                break
        duration = time.time() - t0
        summary = {"steps": self.step_count, "duration_seconds": duration,
                   "final_prey": len(self.prey), "final_predators": len(self.preds)}
        return summary


