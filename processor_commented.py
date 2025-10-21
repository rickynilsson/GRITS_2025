"""Streaming data processor using a fixed-size sliding window with simple anomaly detection.

An anomaly is flagged when the absolute difference between the newest value and the
current window average exceeds a fixed threshold.
"""

import collections

class DataProcessor:
    """Process numerical streams with a sliding window and flag anomalies.

    Attributes:
        window (collections.deque): Fixed-size sliding window of recent values.
        _state (list[tuple]): History aligned to the window of tuples
            (value, window_average, is_anomaly).
        _threshold (float): Absolute deviation threshold to flag anomalies.
    """

    def __init__(self, size):
        """Initialize the processor.

        Args:
            size (int): Maximum number of recent values to keep in the sliding window.
        """
        # Fixed-size window; oldest values are discarded when capacity is exceeded.
        self.window = collections.deque(maxlen=size)
        # Mirror of the window storing (value, avg, anomaly) for each ingested value.
        self._state = []
        # Absolute deviation threshold for anomaly detection.
        self._threshold = 1.5

    def ingest(self, value):
        """Ingest a new data point and update state/anomaly flag.

        Maintains _state length aligned with the window capacity.

        Args:
            value (float | int): New numeric value to process.
        """
        # If the window is at capacity, prune the oldest state entry to stay aligned.
        if len(self.window) == self.window.maxlen:
            self._prune()
        # Append the new value; deque will drop the oldest if needed.
        self.window.append(value)
        # Analyze the updated window and record the result.
        self._process_window()

    def _prune(self):
        """Drop the oldest recorded state to match the sliding window length."""
        # Remove the earliest (value, avg, anomaly) tuple.
        self._state.pop(0)

    def _get_avg(self):
        """Compute the average of the current window.

        Returns:
            float: Average of values in the window, or 0 if the window is empty.
        """
        if not self.window:
            return 0
        return sum(self.window) / len(self.window)

    def _process_window(self):
        """Compute anomaly status for the latest value and record it.

        Returns:
            bool: True if the latest value is an anomaly, otherwise False.
        """
        current_avg = self._get_avg()
        # Absolute deviation of the latest value from the window average.
        diff = abs(self.window[-1] - current_avg)
        anomaly = diff > self._threshold
        # Store (latest value, current average, anomaly flag).
        self._state.append((self.window[-1], current_avg, anomaly))
        return anomaly

    def get_anomalies(self):
        """Retrieve all recorded anomalies in the current state.

        Returns:
            list[tuple]: Tuples of (value, window_average, is_anomaly=True).
        """
        return [t for t in self._state if t[2]]

# Example Usage:
# Create a processor with a window size of 3.
processor = DataProcessor(size=3)
# Simulated data stream.
data_points = [10, 11, 10, 50, 12, 11]

for point in data_points:
    processor.ingest(point)

# Print anomalies detected within the current window-aligned state.
print(processor.get_anomalies())