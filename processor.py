import collections

class DataProcessor:

    def __init__(self, size):
        self.window = collections.deque(maxlen=size)
        self._state = []
        self._threshold = 1.5

    def ingest(self, value):
        if len(self.window) == self.window.maxlen:
            self._prune()
        self.window.append(value)
        self._process_window()

    def _prune(self):
        self._state.pop(0)

    def _get_avg(self):
        if not self.window:
            return 0
        return sum(self.window) / len(self.window)

    def _process_window(self):
        current_avg = self._get_avg()
        diff = abs(self.window[-1] - current_avg)
        anomaly = diff > self._threshold
        self._state.append((self.window[-1], current_avg, anomaly))
        return anomaly

    def get_anomalies(self):
        return [t for t in self._state if t[2]]

# Example Usage:
processor = DataProcessor(size=3)
data_points = [10, 11, 10, 50, 12, 11]

for point in data_points:
    processor.ingest(point)

print(processor.get_anomalies())