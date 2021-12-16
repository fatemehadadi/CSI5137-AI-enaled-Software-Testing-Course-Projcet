from GeneticAlgorithm import *


# test case generator based on GA
class Test_Generator_GeneticAgorithm:
    def __init__(self, n_test_data=4):
        self.n_test_data = n_test_data
        self.test_suit = [[] for _ in range(n_test_data)]
        self.covered = 0
        return

    def run_GA(self, n_generation=1000):
        self.test_suit, self.covered = GA(self.n_test_data, n_generation)
        return

    def print_result(self):
        print(self.test_suit)
        return

    def get_coverage(self):
        return self.covered
