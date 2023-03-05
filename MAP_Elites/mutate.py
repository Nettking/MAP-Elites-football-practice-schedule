import random

# Define a mutation function that randomly changes one or more genes in a solution
def mutate(solution, mutation_prob, num_dimensions, map_size):
    for i in range(num_dimensions):
        if random.random() < mutation_prob:
            solution[i] = random.randint(0, map_size[0] - 1)
    return solution
