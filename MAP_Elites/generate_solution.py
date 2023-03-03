import random
from MAP_Elites.mutate import *
from MAP_Elites.crossover import *

# Define a function to generate a random solution
def generate_solution(elite_archive, mutation_prob, crossover_prob, num_dimensions):
    if random.random() < crossover_prob:
        # Select parents from the fittest solutions
        fittest_solutions = sorted(elite_archive.values(), key=lambda x: x["fitness"], reverse=True)[:2]
        parent1, parent2 = [solution["solution"] for solution in fittest_solutions]
        child = crossover(parent1, parent2, num_dimensions)
    else:
        # Select a random parent
        parents = [solution["solution"] for solution in elite_archive.values()]
        child = random.choice(parents)
    child = mutate(child, mutation_prob, num_dimensions)
    return child