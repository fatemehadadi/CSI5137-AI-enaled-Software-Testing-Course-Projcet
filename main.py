from TestCaseGeneratorGA import *

if __name__ == '__main__':
    # build an instance of the test generator
    ga = Test_Generator_GeneticAgorithm()
    # run the generator which is based on GA
    ga.run_GA()
    # print the test cases with their mutation score
    ga.print_result()
    # print the mutant coverage of the whole test suit
    print(ga.get_coverage())
