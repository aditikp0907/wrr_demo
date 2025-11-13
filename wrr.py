class WRR:
    def __init__(self):
        self.workers = [("w1", 5), ("w2", 3), ("w3", 1)]
        self.current = 0

    def next(self):
        w, weight = self.workers[self.current]
        self.current = (self.current + 1) % len(self.workers)
        return w
