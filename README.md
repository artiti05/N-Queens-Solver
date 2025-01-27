# N-Queens Solver using Genetic Algorithms (GA)

This project demonstrates solving the N-Queens problem using Genetic Algorithms (GA). The goal is to find the best hyperparameters for the GA to efficiently solve the problem, with the ability to run the hyperparameter tuning and solving phases independently.

---

## How It Works

1. **Hyperparameter Tuning (`test.py`)**  
   - Run the `test.py` file and input the desired `n` (size of the chessboard).  
   - 50 trials are conducted using Optuna to identify the optimal values for:  
     - **Population Size**  
     - **Mutation Rate**  
     - **Maximum Generations**  
     - **Crossover Method**  
   - The best hyperparameters are saved dynamically into a `best_params.json` file for later use.  

2. **Solving the Problem (`N-Q.py`)**  
   - Run the `N-Q.py` file, which reads the saved hyperparameters from `best_params.json`.  
   - The N-Queens problem is solved for the given `n` size using the tuned hyperparameters.  
   - The solution, time taken, and generations required are recorded in `sol.txt`.
   - Progress is logged in `log.txt`, which records the performance of each trial.

---

### Example Outputs

#### For n = 4
- **Optimal Parameters** (saved in `best_params.json`):  
  - Population Size: 200  
  - Mutation Rate: 0.0584  
  - Max Generations: 1300  
  - Crossover Method: One-point  

- **Solution (1D Array Representation)**:  
  `[2, 0, 3, 1]`

- **Chessboard Representation**:  

- **Time Taken**: Less than a second.

---

#### For n = 8
- **Optimal Parameters** (saved in `best_params.json`):  
- Population Size: 300  
- Mutation Rate: 0.0255  
- Max Generations: 2400  
- Crossover Method: Uniform  

- **Solution (1D Array Representation)**:  
`[3, 0, 4, 7, 5, 2, 6, 1]`

- **Chessboard Representation**:  

- **Time Taken**: Approximately 2 seconds.

---

### Larger Board Sizes
For larger board sizes (e.g., 16, 32), the genetic algorithm remains efficient due to the use of tuned hyperparameters. However, the execution time may increase as `n` grows.

---

### Files
- **`test.py`**:  
- Conducts hyperparameter tuning using Optuna.  
- Saves the best hyperparameters in `best_params.json`.  
- Logs all trial results in `log.txt`.  

- **`N-Q.py`**:  
- Solves the N-Queens problem using the best hyperparameters from `best_params.json`.  
- Logs the solution, time taken, and generation details in `sol.txt`.  

- **`log.txt`**: Logs the progress and results of each trial during hyperparameter tuning.  

- **`sol.txt`**: Stores the final solution, the chessboard representation, time taken, and generations required.  

- **`best_params.json`**: Contains the optimal hyperparameters identified during tuning.

---

### Key Features
1. **Independent Execution**:  
 - The tuning (`test.py`) and solving (`N-Q.py`) phases are completely independent.  
 - Hyperparameters are seamlessly shared using the `best_params.json` file.  

2. **Real-Time Logging**:  
 - Both tuning and solving progress are logged dynamically to track performance and execution details.  

3. **Scalability**:  
 - The framework supports various chessboard sizes and efficiently adapts through optimized hyperparameters.  

--- 

### Future Improvements
- Add support for distributed execution to handle larger `n` more efficiently.  
- Visualize the evolution of fitness scores across generations.  
- Extend the GA implementation to tackle other combinatorial optimization problems.

---
