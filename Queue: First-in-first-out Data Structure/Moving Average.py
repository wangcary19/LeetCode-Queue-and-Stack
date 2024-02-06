# February 4th, 2024
def __init__(self, size: int):
    self.l = []
    self.window = size


def next(self, val: int) -> float:
    self.l.append(val)

    if len(self.l) < self.window:
        return float(sum(self.l) / len(self.l))
    else:
        return float(sum(self.l[len(self.l) - self.window:]) / self.window)