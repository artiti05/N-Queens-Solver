import json
import optuna
from utils import initialize_population, fitness, select, crossover, mutate


def GA(n, population_size=100, mutation_rate=0.1, max_generations=1000, crossover_method="one-point"):
    """Solve the N-Queens problem using a genetic algorithm."""
    population = initialize_population(n, population_size)

    for generation in range(max_generations):
        fitness_scores = [fitness(board) for board in population]
        best_fitness = max(fitness_scores)
        best_board = population[fitness_scores.index(best_fitness)]

        if best_fitness == n * (n - 1) // 2:
            return best_board, generation + 1, 0  # Return when solution is found

        next_generation = []
        while len(next_generation) < population_size:
            parent1 = select(population, fitness_scores)
            parent2 = select(population, fitness_scores)
            child1, child2 = crossover(parent1, parent2, method=crossover_method)
            mutate(child1, mutation_rate)
            mutate(child2, mutation_rate)
            next_generation.extend([child1, child2])

        population = next_generation

    return None, max_generations, 0  # No solution found


def objective(trial, n):
    # Define hyperparameter search space
    population_size = trial.suggest_categorical("population_size", [100, 200, 300, 400, 500])
    mutation_rate = trial.suggest_float("mutation_rate", 0.001, 0.1)
    max_generations = trial.suggest_int("max_generations", 500, 5000, step=100)
    crossover_method = trial.suggest_categorical("crossover_method", ["one-point", "uniform"])

    _, generations, _ = GA(
        n=n,  # Use the specific N-Queens size
        population_size=population_size,
        mutation_rate=mutation_rate,
        max_generations=max_generations,
        crossover_method=crossover_method
    )
    return generations  # Minimize the number of generations


if __name__ == "__main__":
    # Ask the user for the number of queens
    n = int(input("Enter the N-Queens size for optimization: "))

    # Run Optuna to optimize hyperparameters for this specific `n`
    study = optuna.create_study(direction="minimize")
    study.optimize(lambda trial: objective(trial, n), n_trials=50)

    # Load existing data or create a new dictionary
    try:
        with open("best_params.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        data = {}

    # Save the best parameters for this specific `n`
    data[str(n)] = study.best_params
    with open("best_params.json", "w") as file:
        json.dump(data, file, indent=4)

    print(f"Best parameters for N={n} saved to best_params.json:", study.best_params)
