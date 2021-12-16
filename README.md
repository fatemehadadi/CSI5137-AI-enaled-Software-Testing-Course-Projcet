# CSI5137-AI-enaled-Software-Testing-Course-Projcet
This project is for the CSI5137 course project. 
The title of project is Replication Study of the Software Testing Efficiency Optimization using Genetic Algorithm and Mutation Analysis.
This project consist of 6 python files:
 - main.py : is the mian program which runs the test generator according to the method of the project
 - TestGeneratorGA.py : this file contains the class of Test_Generator_GeneticAgorithm. This class implement the test case generation using GA
 - GeneticAlgorithm.py : this part runs a metahueristic search algotithm based on GA to find a test suit with full mutant coverage
 - TestCase.py : this file contain the class of TestCase which play the role of indiviuals in GA. Each test case contains two integer as inputs of the power program.
 - utils.py : in order to calculate the fitness value and mutation score for each test case which is based on CFG.
 - test.py : for the second research question, we compare the average performance of the method with random search and plot the result.
 - requirement.txt : to install the package required for this project 
