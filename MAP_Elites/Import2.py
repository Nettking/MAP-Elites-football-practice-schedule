import csv
from Activity import *

def read_exercises():
    warm_up = []
    main_exercises = []
    stretching = []

    csv_file = "./data/drills_space.csv"

    # Open the CSV file and read the data
    with open(csv_file, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            activity = Activity(str(row["Activity Type"]), str(row["Type"]), int(row["Duration"]), float(row["Score"]), float(row["Injuries"]), float(row["SkillImprovement"]))
            activity_type = str(row["Activity Type"])
            if activity_type == "Warm-up Exercises":
                warm_up.append(activity)
            elif  activity_type == "Stretching":
                stretching.append(activity)
            else:
                main_exercises.append(activity)

    return warm_up, main_exercises, stretching

if __name__ == '__main__':
    warmup, main, stretching = read_exercises()

    for a in main:
        a.print_activity_details()
