# N-Queens Solver using Genetic Algorithms (GA)

This project demonstrates solving the N-Queens problem using Genetic Algorithms (GA). The goal is to find the best hyperparameters for the GA to efficiently solve the problem.

## How It Works

1. **Hyperparameter Tuning**:  
   - Run the `test.py` file and input the desired `n` (size of the chessboard).  
   - 50 tests are conducted to identify the optimal values for:
     - Population Size
     - Mutation Rate
     - Maximum Generations
     - Crossover Method  
   - The results are logged in the `log.txt` file.

2. **Solving the Problem**:  
   - The identified hyperparameters are used as inputs for `N-Q.py`.  
   - The N-Queens problem is solved for the given `n` size, with the solution and time taken recorded in the `sol.txt` file.

---

### Example Outputs

#### For n = 4
- **Optimal Parameters**:  
  - Population Size: 200  
  - Mutation Rate: 0.05843236813767189  
  - Max Generations: 1300  
  - Crossover Method: One-point  

- **Solution (1D Array Representation)**:  
  `[2, 0, 3, 1]`

- **Chessboard Representation**:
- **Time Taken**: Less than a second.

---

#### For n = 8
- **Optimal Parameters**:  
- Population Size: 300  
- Mutation Rate: 0.025542997380196827  
- Max Generations: 2400  
- Crossover Method: Uniform  

- **Solution (1D Array Representation)**:  
`[3, 0, 4, 7, 5, 2, 6, 1]`

- **Chessboard Representation**:

---

#### For n = 12
- **Optimal Parameters**:  
- Population Size: 300  
- Mutation Rate: 0.011494393577002205  
- Max Generations: 2400  
- Crossover Method: One-point  

- **Solution (1D Array Representation)**:  
`[4, 8, 3, 11, 2, 7, 9, 0, 5, 1, 10, 6]`

- **Chessboard Representation**:

---

### Larger Board Sizes
As `n` increases (e.g., 16, 32, ...), the algorithm continues to find solutions efficiently by leveraging the tuned hyperparameters.

--- 

### Files
- **`test.py`**: Conducts hyperparameter tuning.  
- **`log.txt`**: Logs the results of the tests.  
- **`N-Q.py`**: Solves the N-Queens problem using the identified hyperparameters.  
- **`sol.txt`**: Stores the final solution and time taken.

---
