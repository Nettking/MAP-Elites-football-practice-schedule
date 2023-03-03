import random

# Define a crossover function that exchanges genes between two solutions
def crossover(parent1, parent2):
    child = []
    for i in range(num_dimensions):
        if random.random() < 0.5:
            child.append(parent1[i])
        else:
            child.append(parent2[i])
    return child
