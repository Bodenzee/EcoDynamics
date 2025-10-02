class DataCollector:
    def __init__(self):
        self.data = {"time": [], "prey": [], "predator": []}

    def record(self, t, prey, predator):
        self.data["time"].append(t)
        self.data["prey"].append(prey)
        self.data["predator"].append(predator)

    def get_data(self):
        return self.data
