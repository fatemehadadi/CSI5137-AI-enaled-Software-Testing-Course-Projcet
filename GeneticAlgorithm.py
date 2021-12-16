from TestCase import *
from random import *


# randomly initial the first generation
def initial_population(n, min=0, max=15):
    population = []
    for i in range(n):
        a = randint(min, max)
        b = randint(min, max)
        population.append(TestCase(a, b))
    return population


# check if the new child already exist in the population
def is_new(child, population):
    for chrome in population:
        if child.a == chrome.a and child.b == chrome.b:
            return False
        elif child.b == chrome.b:
            return False
    return True


# one point crossover in inputs and mutation of some bits
def crossover_mutation(parents, crossover_probability, mutation_probability):
    r = random()
    get_bin = lambda x: [s for s in format(x, 'b').zfill(6)]
    a1, a2 = get_bin(parents[0].a), get_bin(parents[1].a)
    b1, b2 = get_bin(parents[0].b), get_bin(parents[1].b)
    a_child, b_child = a1, b1

    # crossover part
    if r < crossover_probability:
        point = randint(1, 4)
        for i in range(point):
            a_child[i], b_child[i] = a2[5 - i], b2[5 - i]

    # mutation part
    if random() < mutation_probability:
        point = np.random.choice(6, 2, replace=False)
        if point[0] > point[1]:
            point[0], point[1] = point[1], point[0]

        for i in range(point[0], point[1]):
            if a_child[i] == '0':
                a_child[i] == '1'
            else:
                a_child[i] == '0'

            if b_child[i] == '0':
                b_child[i] == '1'
            else:
                b_child[i] == '0'

    # convert bits to integer
    a = int(''.join(a_child), 2)
    b = int(''.join(b_child), 2)

    # build the new test case
    child = TestCase(a, b)
    return child


# calculate the mutant coverage of the whole test suit
def mutant_coverage(population):
    mask = np.zeros(3)
    for t in population:
        mask += t.coverage_mask
    covered = sum([1 for m in mask if m != 0]) / len(mask) * 100
    return covered


# test case generator based on genetic algorithm
def GA(n, crossover_probability=0.8, mutation_probability=0.3, n_generation=1000):
    population = initial_population(n)
    k = 0
    while mutant_coverage(population) != 100 and k < n_generation:
        # if True:
        # route wheel selection
        k += 1
        population_fitness = sum([chromosome.fitness for chromosome in population])

        # Computes for each chromosome the probability
        chromosome_probabilities = [chromosome.fitness / population_fitness for chromosome in population]

        # Making the probabilities for a minimization problem
        chromosome_probabilities = np.array(chromosome_probabilities)

        # Selects one chromosome based on the computed probabilities
        parents_index = np.random.choice(n, 2, replace=False, p=chromosome_probabilities)
        parents = [population[parents_index[0]], population[parents_index[1]]]

        # crossover mutation
        child = crossover_mutation(parents, crossover_probability, mutation_probability)
        # add to population
        if is_new(child, population):
            population[parents_index[1]] = child

    return population, mutant_coverage(population)
