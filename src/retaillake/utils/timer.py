import time


class Timer:

    def __init__(self):

        self.start = None

    def __enter__(self):

        self.start = time.time()

        return self

    def __exit__(self, *args):

        self.elapsed = time.time() - self.start