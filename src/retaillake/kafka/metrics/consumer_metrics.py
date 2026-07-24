import time


class ConsumerMetrics:

    def __init__(self):

        self.messages = 0

        self.started = time.time()

    def increment(self):

        self.messages += 1

    def report(self):

        elapsed = time.time() - self.started

        rate = self.messages / elapsed if elapsed else 0

        print(

            f"[Metrics] "

            f"Messages={self.messages} "

            f"Elapsed={elapsed:.2f}s "

            f"Rate={rate:.2f} msg/sec"

        )