from Import2 import *
from ActivityPlanGenerator import *


def generate_activity_plans(generator, number_of_plans):
    activity_plans = []
    for i in range(0, number_of_plans):
        activity_plans.append(generator.generate_random_activity_plan())
    return activity_plans

def get_best_plans(plans, number_of_plans_to_get):
    sorted_plans = sorted(plans, key=lambda plan: plan.total_score, reverse=True)
    return sorted_plans[:int(number_of_plans_to_get)]

if __name__ == '__main__':
    warmup, main, stretching = read_exercises()

    generator = ActivityPlanGenerator(warmup, main, stretching) 
    plan = generator.generate_random_activity_plan()

    # Generate 1000 random activity plans
    plans = generate_activity_plans(generator, 1000)

    # Get the 100 best plans
    best = get_best_plans(plans, 100)

    # Perform crossover on the 100 best plans to create the next generation of plans
    next_generation = []
    for i in range(50):
        plan1 = best[i]
        plan2 = best[i+1]
        crossover = ActivityPlanGenerator.crossover(plan1, plan2)
        next_generation.append(crossover)

    # Generate 950 random activity plans to fill up the rest of the next generation
    next_generation += generate_activity_plans(generator, 950)

    # Get the 2 best plans from the next generation
    best_next_generation = get_best_plans(next_generation, 2)

    plan1 = best_next_generation[0]
    plan2 = best_next_generation[1]
    print("SCORE PLAN1: " + str(plan1.total_score))
    print("SCORE PLAN2: " + str(plan2.total_score))
    crossover = ActivityPlanGenerator.crossover(plan1, plan2)
    print("SCORE CROSSOVER: " + str(crossover.total_score))

    variables = {'Plan 1': plan1.total_score, 'Plan 2': plan2.total_score, 'Crossover': crossover.total_score}
    highest_variable = max(variables, key=variables.get)

    print(highest_variable, "has the highest score with a value of", variables[highest_variable])