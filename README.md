# GeneticAlgorithm
> A visual representation of genetic algorithm with python Turtle. 

## How to test
1. Open mainSearch.py
2. Modify line 11 -> level = levels[3] ,  instead of 3 enter what you desire from 1-8 to change maze.
3. Run searchMain.py and after the maze is built please enter to the console number of population and the number of generations you want
4. Wait until calculations are done and the console will output "Please press q"
5. Go to the maze window and press q.

## How it works
* Initial population is generated based on the input the user entered.
* Each 'gene' runs a random visited pathfinder algorithm until the destination is found
* Parents are chosen by probability, parents with higher fitness have larger probability.
* Crossover is made by checking paths of the two parents and choosing a random point where they intersect, then two children have half the path from first parent and hald from second.
* When calculation is made after the number of generations the user has given as an input, the 'gene' with the highest fitness is chosen to be displayed by a turtle.
