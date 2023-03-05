import math

# Define the function to update the elite archive
def update_elite_archive(solution, fitness, elite_archive, map_size, bin_sizes):
    # Calculate the bin indices for the solution
    bin_indices = tuple([math.floor(solution[i] * map_size[1] / (max_duration + 1)) for i, max_duration in enumerate(bin_sizes)])

    # If the bin is empty or the new solution dominates the current solution in the bin, update the bin
    if bin_indices not in elite_archive or fitness > elite_archive[bin_indices]["fitness"]:
        elite_archive[bin_indices] = {"solution": solution, "fitness": fitness}
