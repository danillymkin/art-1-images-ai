import numpy as np


class Neuron:
    def __init__(self, X, L):
        self.T = np.array(X)
        self.R = np.zeros((10), dtype=int)
        self.m = np.sum(self.T > 0)
        self.L = L
        self.B = self.T * self.L / (self.L - 1 + self.m)

    def exit_S(self, similarity):
        return np.sum(np.array(similarity) * self.B)
