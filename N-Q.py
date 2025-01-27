import json
from utils import save_as, initialize_population, fitness, select, crossover, mutate

import time

def GA(n, population_size=100, mutation_rate=0.1, max_generations=1000, crossover_method="one-point", log_file="log.txt"):
    """Solve the N-Queens problem using a genetic algorithm and log progress to a file."""
    # Initialize population
    population = initialize_population(n, population_size)
    start_time = time.time()  # Start timing the execution

    with open(log_file, "w") as log:
        log.write(f"Starting Genetic Algorithm for {n}-Queens\n")
        log.write(f"Population Size: {population_size}, Mutation Rate: {mutation_rate}, Max Generations: {max_generations}\n\n")
        
        for generation in range(max_generations):
            # Calculate fitness scores
            fitness_scores = [fitness(board) for board in population]
            best_fitness = max(fitness_scores)
            best_board = population[fitness_scores.index(best_fitness)]

            # Log the result of this generation
            log.write(f"Generation {generation + 1}: Best Fitness = {best_fitness}, Best Board = {best_board}\n")
            log.flush()  # Ensure the log is written to disk immediately
            
            # Check if a solution is found
            if best_fitness == n * (n - 1) // 2:
                elapsed_time = time.time() - start_time  # Calculate elapsed time
                log.write("\nSolution Found!\n")
                log.write(f"Generations: {generation + 1}, Elapsed Time: {elapsed_time:.2f} seconds\n")
                log.write(f"Solution: {best_board}\n")
                log.flush()
                return best_board, generation + 1, elapsed_time

            # Create next generation
            next_generation = []
            while len(next_generation) < population_size:
                # Selection
                parent1 = select(population, fitness_scores)
                parent2 = select(population, fitness_scores)
                # Crossover
                child1, child2 = crossover(parent1, parent2, method=crossover_method)
                # Mutation
                mutate(child1, mutation_rate)
                mutate(child2, mutation_rate)
                next_generation.extend([child1, child2])
            
            population = next_generation
        
        # No solution found
        elapsed_time = time.time() - start_time  # Calculate elapsed time
        log.write("\nNo Solution Found\n")
        log.write(f"Generations: {max_generations}, Elapsed Time: {elapsed_time:.2f} seconds\n")
        log.flush()

    print(f"No solution found. Details logged to {log_file}")
    return None, max_generations, elapsed_time

if __name__ == "__main__":
    # Load the best parameters from the JSON file
    try:
        with open("best_params.json", "r") as file:
            best_params = json.load(file)
    except FileNotFoundError:
        print("Error: best_params.json not found. Run test.py first to generate optimal parameters.")
        exit(1)

    # Ask the user for the size of the N-Queens problem
    n = int(input("Enter the N-Queens size: "))

    # Run the GA with the best parameters
    solution, generation, time_taken = GA(
        n=n,
        population_size=best_params["population_size"],
        mutation_rate=best_params["mutation_rate"],
        max_generations=best_params["max_generations"],
        crossover_method=best_params["crossover_method"]
    )

    # Save the solution to a file
    save_as(solution, generation, time_taken)
