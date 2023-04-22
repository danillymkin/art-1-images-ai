from Neuron import Neuron
import numpy as np


class NetworkART:
    def __init__(self, first_vector, P, L):
        self.L = L
        self.P = P

        self.vector_length = len(first_vector)
        self.neurons = [Neuron(np.ones((self.vector_length,), dtype=int), self.L), Neuron(first_vector, self.L)]

    def recognition(self, input_vectors):
        S = []

        for neuron in self.neurons:
            S.append(neuron.exit_S(input_vectors))

        winner = S.index(max(S))

        if winner == 0:
            self.learning_memorization(input_vectors)
            return len(self.neurons)
        else:
            C = self.neurons[winner].T * input_vectors
            comparison_result = (self.vector_length - np.sum(np.logical_xor(C, input_vectors))) / self.vector_length

            if comparison_result > self.P:
                self.neurons[winner].T = C
                self.neurons[winner].B = self.L * C / (self.L - 1 + np.sum(C > 0))
                return winner + 1
            else:
                self.learning_memorization(input_vectors)
                return len(self.neurons)

    def learning_memorization(self, input_vectors):
        self.neurons.append(Neuron(input_vectors, self.L))
