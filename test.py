from TestCaseGeneratorGA import *
import matplotlib.pyplot as plt

# test case generator to find a test suit with full mutant coverage based on random search
def random_search(n, n_generation=1000):
    # initial the first generation randomly
    population = initial_population(n, min=0, max=63)
    k = 0
    min = 0
    max = 63
    while mutant_coverage(population) != 100 and k < n_generation:
        k += 1
        # randomly build the next test case
        a = randint(min, max)
        b = randint(min, max)
        population.append(TestCase(a, b))
        population.pop(0)
    return population, mutant_coverage(population)


if __name__ == '__main__':
    # store the results of average mutant coverage in the histories
    history_ga = []
    history_random = []
    # limits are the fitness evaluation numbers used as the evaluation limitation as a fair comparison between GA and
    # Random search
    limits = [10, 20, 30, 40, 50, 70, 80, 90, 100, 200, 300, 400, 500]

    # at first step the GA generator is tested
    for l in limits:
        print('in stage of', l)
        s = 0
        for i in range(1000):
            ga = Test_Generator_GeneticAgorithm()
            ga.run_GA(n_generation=l)
            s += ga.get_coverage()
        history_ga.append(s / 1000)

    # after that the random test is going to run
    for l in limits:
        print('in stage of', l)
        s = 0
        for i in range(1000):
            _, coverage = random_search(4, n_generation=l)
            s += coverage
        history_random.append(s / 1000)

    # Define data values
    x = [str(l) for l in limits]
    y = history_random
    z = history_ga

    # Plot a the results of averaged coverage by random test case generator
    plt.plot(x, y, label='Random', linestyle='-', marker='^', color='#FF00FF')

    # Plot a the results of averaged coverage by GA test case generator in the same plot
    plt.plot(x, z, label='GA', linestyle='-', marker='s', color='#15B01A')
    plt.xticks(rotation=90)
    plt.ylim([0, 100])
    plt.ylabel('averaged mutation coverage percentage')
    plt.xlabel('fitness evaluation')
    plt.legend(loc='lower right')
    # plt.show()
    plt.savefig('RQ2.png')
