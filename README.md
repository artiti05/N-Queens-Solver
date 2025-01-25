# N-Queens-Solver
N Queens Solver using the genetic algorithms (GA)
Solving N-Queens in GA

To solve the problem we need to find the best hyperparameter for The GA
after running the test.py file and inputing the n size a 50 tests will be done 
showing on the log.txt the best population size, mutation rate, max generations, crossover method

those outputs are put as parameters for the N-Q.py and therefore the problem is solved for 
this n size input in the least time taken

for example for n = 4:
Population Size: 200, Mutation Rate: 0.05843236813767189, Max Generations: 1300, crossover method: one-point
Solution (1D Array Representation):
[2, 0, 3, 1]

Chessboard Representation:
.Q..
...Q
Q...
..Q.
in less than a second is shown on sol.txt file.

and for n = 8 is: Population Size: 300, Mutation Rate: 0.025542997380196827, Max Generations: 2400, crossover method: uniform
Solution (1D Array Representation):
[3, 0, 4, 7, 5, 2, 6, 1]

Chessboard Representation:
.Q......
.......Q
.....Q..
Q.......
..Q.....
....Q...
......Q.
...Q....
and for n=12: Population Size: 300, Mutation Rate: 0.011494393577002205, Max Generations: 2400, crossover method: one-point
Solution (1D Array Representation):
[4, 8, 3, 11, 2, 7, 9, 0, 5, 1, 10, 6]

Chessboard Representation:
.......Q....
.........Q..
....Q.......
..Q.........
Q...........
........Q...
...........Q
.....Q......
.Q..........
......Q.....
..........Q.
...Q........
and so on for n when it gets larger and larger like n=16, 32....
