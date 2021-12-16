from utils import *


# test case class which contain the inputs of the power program
class TestCase:
    def __init__(self, a, b):
        # each input consists of two non-negative integer
        self.a = a
        self.b = b
        self.mutant_score = self.calcualte_MS()
        self.fitness = self.calculate_fitness()
        self.coverage_mask = self.get_mask()

    def __repr__(self):
        return str([self.a, self.b, 'MS: ' + str(self.mutant_score) + '%'])

    def calcualte_MS(self):
        _, ms, _, _ = CFgraph(self.a, self.b)
        return round(ms / 3 * 100, 2)

    def calculate_fitness(self):
        f, _, _, _ = CFgraph(self.a, self.b)
        return f

    def get_mask(self):
        _, _, _, mask = CFgraph(self.a, self.b)
        return mask
