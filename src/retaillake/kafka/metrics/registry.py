class MetricsRegistry:

    def __init__(self):

        self.metrics = {}

    def increment(self, metric):

        self.metrics[metric] = self.metrics.get(metric, 0) + 1

    def get(self, metric):

        return self.metrics.get(metric, 0)

    def snapshot(self):

        return dict(self.metrics)