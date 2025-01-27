import random

def initialize_population(n, size=100):
    return [[random.randint(0, n-1) for _ in range(n)] for _ in range(size)]

def fitness(board):
    n = len(board)
    attackers = 0
    for i in range(n):
        for j in range(i+1, n):
            if board[i] == board[j] or abs(board[i] - board[j]) == abs(i - j): 
                attackers += 1
    return (n * (n - 1)) // 2 - attackers

def select(population, fitness_scores):
    total_fitness = sum(fitness_scores)
    probabilities = [f / total_fitness for f in fitness_scores]
    return population[random.choices(range(len(population)), probabilities)[0]]

def crossover(parent1, parent2, method="one-point"):
    if method == "one-point":
        cutting_point = random.randint(0, len(parent1) - 1)
        child1 = parent1[:cutting_point] + parent2[cutting_point:]
        child2 = parent2[:cutting_point] + parent1[cutting_point:]
    elif method == "uniform":
        child1 = [random.choice(g) for g in zip(parent1, parent2)]
        child2 = [random.choice(g) for g in zip(parent2, parent1)]
    return child1, child2

def mutate(board, mutation_rate):
    if random.random() < mutation_rate:
        col = random.randint(0, len(board) - 1)
        row = random.randint(0, len(board) - 1)
        board[col] = row

def save_as(solution, generation, time_taken, filename="sol.txt"):
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