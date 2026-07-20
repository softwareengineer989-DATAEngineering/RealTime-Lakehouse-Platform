import time


class ProducerMetrics:

    def __init__(self):

        self.start_time = time.time()

        self.messages_sent = 0

    def increment(self):

        self.messages_sent += 1

    def report(self):

        elapsed = time.time() - self.start_time

        if elapsed == 0:
            return

        throughput = self.messages_sent / elapsed

        print(
            f"[Metrics] "
            f"Messages={self.messages_sent} "
            f"Elapsed={elapsed:.2f}s "
            f"Rate={throughput:.2f} msg/sec"
        )