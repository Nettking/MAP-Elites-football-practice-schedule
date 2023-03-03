import random
from MAP_Elites.mutate import *
from MAP_Elites.crossover import *

# Define a function to generate a random solution
def generate_solution(parents, mutation_prob, crossover_prob, num_dimensions):
    if random.random() < crossover_prob:
        parent1, parent2 = random.sample(parents, 2)
        child = crossover(parent1, parent2)
    else:
        child = random.choice(parents)
    child = mutate(child, mutation_prob, num_dimensions)
    return child