"""
Run the MAP-Elites algorithm with mutation and crossover.

The algorithm generates a set of solutions for each generation and evaluates their fitness using the
calculate_fitness function. The elite solutions are stored in the elite_archive dictionary, which is updated
every generation with the best solutions. The mutation and crossover probabilities are decreased over time
using the mutation_decay and crossover_decay parameters.

Returns:
    None
"""

import math

from MAP_Elites import *

def main():

    # Define the size of the map and the number of generations to run
    map_size = (10, 10)
    num_generations = 50

    # Set mutation and crossover rates
    mutation_prob = 0.01
    crossover_prob = 0.1

    # Set the amount of decay over time
    mutation_decay = 0.9
    crossover_decay = 0.9

    # Define the initial elite archive
    elite_archive = {}

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
        max_duration = max(list(space.values()), key=lambda x: x["Duration"])
        bin_size = math.ceil(max_duration / map_size[0])
        bin_sizes.append(bin_size)

    # Run the map elites algorithm with mutation and crossover
    for generation in range(num_generations):
        # Generate a new set of solutions
        parents = [elite_archive[key]["solution"] for key in elite_archive.keys()]
        solutions = [generate_solution(parents, mutation_prob, crossover_prob, num_dimensions, map_size) for i in range(map_size[0] * map_size[1])]

        # Evaluate the fitness of each solution
        fitnesses = [calculate_fitness(solution, num_dimensions, bin_sizes, feature_space) for solution in solutions]

        # Update the elite archive with the best solutions
        for solution, fitness in zip(solutions, fitnesses):
            update_elite_archive(solution, fitness, elite_archive, map_size, bin_sizes)

        # Print the best solution and its fitness for this generation
        best_solution = max(elite_archive.values(), key=lambda x: x["fitness"])["solution"]
        best_fitness = calculate_fitness(best_solution)
        print(f"Generation {generation+1}: Best fitness = {best_fitness:.2f}")

        # Decrease the mutation and crossover probabilities over time
        mutation_prob *= mutation_decay
        crossover_prob *= crossover_decay

    # Print the final elite archive
    print("Final Elite Archive:")
    for bin_indices, solution_data in elite_archive.items():
        solution = solution_data["solution"]
        fitness = solution_data["fitness"]
        durations = [math.ceil(solution[i] * bin_sizes[i]) for i in range(num_dimensions)]
        print(f"Bin: {bin_indices} Solution: {durations} Fitness: {fitness:.2f}")

if __name__ == '__main__':
    main()
