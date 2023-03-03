import math
import random
import numpy as np

from import_drills import *
from calculate_player_satisfaction import *
from calculate_fitness import *

# Define the size of the map and the number of generations to run
map_size = (10, 10)
num_generations = 50

# Define the number of dimensions and the feature space for the solution space
num_dimensions = 9
feature_space = [
    running_drills_space,
    passing_drills_space,
    defensive_drills_space,
    offensive_drills_space,
    agility_drills_space,
    warm_up_exercises_space,
    strength_training_space,
    stretching_space,
    cardiovascular_training_space
]

# Define the bin size for each dimension
bin_sizes = []
for space in feature_space:
    max_duration = max(space.values())
    bin_size = math.ceil(max_duration / map_size[0])
    bin_sizes.append(bin_size)



# Define a function to generate a random solution
def generate_solution():
    solution = []
    for i in range(num_dimensions):
        solution.append(random.randint(0, map_size[0] - 1))
    return solution

# Define the initial elite archive
elite_archive = {}

# Define the function to update the elite archive
def update_elite_archive(solution, fitness):
    # Calculate the bin indices for the solution
    bin_indices = tuple([math.floor(solution[i] * map_size[1] / (max_duration + 1)) for i, max_duration in enumerate(bin_sizes)])

    # If the bin is empty or the new solution dominates the current solution in the bin, update the bin
    if bin_indices not in elite_archive or fitness > elite_archive[bin_indices]["fitness"]:
        elite_archive[bin_indices] = {"solution": solution, "fitness": fitness}

# Run the map elites algorithm
for generation in range(num_generations):
    # Generate a new set of solutions
    solutions = [generate_solution() for i in range(map_size[0] * map_size[1])]

    # Evaluate the fitness of each solution
    fitnesses = [calculate_fitness(solution, num_dimensions, bin_sizes, feature_space) for solution in solutions]

    # Update the elite archive with the best solutions
    for solution, fitness in zip(solutions, fitnesses):
        update_elite_archive(solution, fitness)

    # Print the best solution and its fitness for this generation
    best_solution = max(elite_archive.values(), key=lambda x: x["fitness"])["solution"]
    best_fitness = calculate_fitness(best_solution, num_dimensions, bin_sizes, feature_space)
    print(f"Generation {generation+1}: Best fitness = {best_fitness:.2f}")

# Print the final elite archive
print("Final Elite Archive:")
for bin_indices, solution_data in elite_archive.items():
    solution = solution_data["solution"]
    fitness = solution_data["fitness"]
    durations = [math.ceil(solution[i] * bin_sizes[i]) for i in range(num_dimensions)]
    print(f"Bin: {bin_indices} Solution: {durations} Fitness: {fitness:.2f}")
