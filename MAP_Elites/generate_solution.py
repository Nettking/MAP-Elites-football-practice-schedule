import random
from MAP_Elites.mutate import *
from MAP_Elites.crossover import *
from MAP_Elites.calculate_fitness import *

def generate_solution(parents, mutation_prob, crossover_prob, num_dimensions):
    # Select a subset of the fittest parents
    sorted_parents = sorted(parents, key=lambda x: calculate_fitness(x), reverse=True)
    num_elite_parents = int(len(parents) * 0.5) # Change this value as desired
    elite_parents = sorted_parents[:num_elite_parents]

    # Generate a child from the elite parents with crossover and mutation
    if random.random() < crossover_prob:
        parent1, parent2 = random.sample(elite_parents, 2)
        child = crossover(parent1, parent2)
    else:
        child = random.choice(elite_parents)
    child = mutate(child, mutation_prob, num_dimensions)
    return child
