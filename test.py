import random
import time
import optuna

# def initialize_population(n, size=100):
#     """Generate an initial population, retrying if fitness is 0."""
#     population = []
#     max_attempts = size * 10  # Limit to avoid infinite loops
#     attempts = 0
#     while len(population) < size and attempts < max_attempts:
#         board = [random.randint(0, n - 1) for _ in range(n)]
#         if fitness(board) > 0:  # Include only boards with non-zero fitness
#             population.append(board)
#         attempts += 1
    
#     # If population is still smaller, pad with random boards
#     while len(population) < size:
#         population.append([random.randint(0, n - 1) for _ in range(n)])
    
#     return population

def initialize_population(n, size=100):
    return [[random.randint(0, n-1) for _ in range(n)] for _ in range(size)]

def fitness(board):
    
    n = len(board)
    attackers = 0
    for i in range(n):
        for j in range(i+1, n):
            if board[i] == board[j] or abs(board[i] - board[j]) == abs(i - j): # according to the slope theorem abs(+1 or -1) means on the same diagonal
                attackers += 1
    return (n*(n-1))//2 - attackers

def select(population, fitness_scores):
    total_fitness = sum(fitness_scores)
    probabilities = [f/total_fitness for f in fitness_scores]

    return population[random.choices(range(len(population)), probabilities)[0]]

def crossover(parent1, parent2, methodd = "one-point"):
    
    if methodd == "one-point":
        cutting_point = random.randint(0, len(parent1)-1)
        child1 = parent1[:cutting_point] + parent2[cutting_point:]
        child2 = parent2[:cutting_point] + parent1[cutting_point:]
    
    elif methodd == "uniform":
        child1 = [random.choice(g) for g in zip(parent1, parent2)]
        child2 = [random.choice(g) for g in zip(parent2, parent1)]
    return child1, child2

def mutate(board, mutaion_rate):
    if random.random() < mutaion_rate:
        col = random.randint(0, len(board)-1)
        row = random.randint(0, len(board)-1)
        board[col]= row
def GA(n, population_size=100, mutation_rate=0.1, max_generations=1000, crossover_method = "one-point", log_file="log.txt"):
    """Solve the N-Queens problem using a genetic algorithm, logging the best result of each generation to a file dynamically."""
    # Initialize population
    population = initialize_population(n, population_size)
    start_time = time.time()
    
    with open(log_file, "w") as log:
        log.write(f"Starting Genetic Algorithm for {n}-Queens\n")
        log.write(f"Population Size: {population_size}, Mutation Rate: {mutation_rate}, Max Generations: {max_generations}\n\n")
        
        best_fitness_over_time = []
        for generation in range(max_generations):
            # Calculate fitness scores
            fitness_scores = [fitness(board) for board in population]
            best_fitness = max(fitness_scores)
            best_board = population[fitness_scores.index(best_fitness)]
            
            # Log the result of this generation
            log.write(f"Generation {generation + 1}: Best Fitness = {best_fitness}, Best Board = {best_board}\n")
            log.flush()  # Ensure the log is written to disk immediately
            
            # Optionally print to console at milestones
            # if (generation + 1) % 50 == 0:
            #     print(f"Generation {generation + 1}: Best Fitness = {best_fitness}")
            
            # Check if a solution is found
            if best_fitness == n * (n - 1) // 2:
                elapsed_time = time.time() - start_time
                log.write("\nSolution Found!\n")
                log.write(f"Generations: {generation + 1}, Elapsed Time: {elapsed_time:.2f} seconds\n")
                log.write(f"Solution: {best_board}\n")
                log.flush()
                print(f"Solution saved to {log_file}")
                return best_board, generation + 1, elapsed_time
            
            best_fitness_over_time.append(best_fitness)
            if generation > 0 and generation % 100 == 0:
                # Check for stagnation
                if len(set(best_fitness_over_time[-10:])) == 1:  # No improvement in last 10 generations
                    mutation_rate = min(mutation_rate + 0.01, 0.3)  # Increase mutation rate up to 0.3
                    log.write(f"Generation {generation + 1}: Mutation rate increased to {mutation_rate:.2f}\n")
                    log.flush()
            
            # Create next generation
            next_generation = []
            while len(next_generation) < population_size:
                # Selection
                parent1 = select(population, fitness_scores)
                parent2 = select(population, fitness_scores)
                # Crossover
                child1, child2 = crossover(parent1, parent2, methodd=crossover_method)
                # Mutation
                mutate(child1, mutation_rate)
                mutate(child2, mutation_rate)
                next_generation.extend([child1, child2])
            
            population = next_generation
        
        # No solution found
        elapsed_time = time.time() - start_time
        log.write("\nNo Solution Found\n")
        log.write(f"Generations: {max_generations}, Elapsed Time: {elapsed_time:.2f} seconds\n")
        log.flush()
    
    print(f"No solution found. Details logged to {log_file}")
    return None, max_generations, elapsed_time

def save_as(solution, generation, time_taken, filename = "sol.txt"):
    with open(filename, "w") as file:
        if solution:
            file.write("N-Queens Solution Found\n")
            file.write(f"Generations: {generation}\n")
            file.write(f"Elapsed Time: {time_taken:.2f} seconds\n")
            file.write("Solution (1D Array Representation):\n")
            file.write(str(solution) + "\n\n")
            file.write("Chessboard Representation:\n")
            n = len(solution)
            for row in range(n):
                line = "".join("Q" if solution[col] == row else "." for col in range(n))
                file.write(line + "\n")
        else:
            file.write("No solution found.\n")
            file.write(f"Generations: {generation}\n")
            file.write(f"Elapsed Time: {time_taken:.2f} seconds\n")
    print(f"Solution saved to {filename}")

def objective(trial):
    # Hyperparameter search space
    population_size = trial.suggest_categorical("population_size", [100, 200, 300, 400, 500])
    mutation_rate = trial.suggest_float("mutation_rate", 0.001, 0.1)
    max_generations = trial.suggest_int("max_generations", 500, 5000, step=100)
    crossover_method = trial.suggest_categorical("crossover_method", ["one-point", "uniform"])

    # Run GA with suggested parameters
    _, generations, time_taken = GA(
        n=8,  # N-Queens size
        population_size=population_size,
        mutation_rate=mutation_rate,
        max_generations=max_generations,
        crossover_method=crossover_method
    )
    return generations  # Minimize the number of generations

n_q = int(input("Enter the n queens: "))

# Running the optimization with Optuna
study = optuna.create_study(direction="minimize")
study.optimize(objective, n_trials=50)

# Print the best parameters
best_params = study.best_params
print("Best Parameters:", best_params)

# Now, use the best parameters to run GA again
best_solution, best_generation, best_time_taken = GA(
    n=n_q,  # N-Queens size
    population_size=best_params['population_size'],
    mutation_rate=best_params['mutation_rate'],
    max_generations=best_params['max_generations'],
    crossover_method=best_params['crossover_method']
)

# solution, generation, time_taken = GA(n, population_size=600, mutation_rate= 0.035, max_generations=2200, crossover_method='uniform')# you can put the size of population and muatation rate and max gens

# Save the final solution
save_as(best_solution, best_generation, best_time_taken)
# save_as(solution, generation, time_taken)