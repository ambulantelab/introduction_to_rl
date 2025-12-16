import numpy as np


class Bandit:
    def __init__(self, means):
        self.means = means
        self.n_actions = len(means)

    def step(self, a):
        return np.random.randn() + self.means[a]
