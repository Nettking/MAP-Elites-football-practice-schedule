from calculate_player_satisfaction import *
from calculate_skill_level_improvement import *

def calculate_fitness(solution, num_dimensions, bin_sizes, feature_space):
    # Convert the solution to a list of durations for each activity type
    durations = []
    for i in range(num_dimensions):
        durations.append(math.ceil(solution[i] * bin_sizes[i]))

    # Calculate the total duration of the practice session
    total_duration = sum(durations)

    # Calculate the score for each feature space based on the selected activities
    scores = []
    for i in range(num_dimensions):
        space = feature_space[i]
        selected_activities = [k for k, v in space.items() if v <= durations[i]]
        score = len(selected_activities) / len(space)
        scores.append(score)
    
    
    high_risk_activities = ["tackling", "heading", "sliding"]

    # Calculate the estimated injury rate based on the selected activities
    injury_rate = 0
    for activity in selected_activities:
        if activity in high_risk_activities:
            injury_rate += 1
    injury_rate /= total_duration

    # Calculate the player satisfaction score based on feedback
    player_satisfaction = calculate_player_satisfaction(selected_activities)

    # Calculate the skill level improvement based on pre- and post-practice assessments
    skill_level_improvement = calculate_skill_level_improvement(selected_activities)
    w1 = 3
    w2 = 2
    w3 = 1
    # Calculate the final fitness score as a weighted sum of the different metrics
    fitness = w1 * (1 - injury_rate) + w2 * player_satisfaction + w3 * skill_level_improvement

    return fitness
