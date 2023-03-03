import csv

# Define the file path and name of the CSV file
csv_file = "./data/drills_space.csv"

# Create empty dictionaries to store the feature space for each activity type
running_drills_space = {}
passing_drills_space = {}
defensive_drills_space = {}
offensive_drills_space = {}
agility_drills_space = {}
warm_up_exercises_space = {}
strength_training_space = {}
stretching_space = {}
cardiovascular_training_space = {}

# Open the CSV file and read the data
with open(csv_file, mode='r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        # Parse the data for each activity type and store it in the appropriate dictionary
        if row["Activity Type"] == "Running Drills":
            running_drills_space[row["Type"]] = int(row["Duration"])
        elif row["Activity Type"] == "Passing Drills":
            passing_drills_space[row["Type"]] = int(row["Duration"])
        elif row["Activity Type"] == "Defensive Drills":
            defensive_drills_space[row["Type"]] = int(row["Duration"])
        elif row["Activity Type"] == "Offensive Drills":
            offensive_drills_space[row["Type"]] = int(row["Duration"])
        elif row["Activity Type"] == "Agility Drills":
            agility_drills_space[row["Type"]] = int(row["Duration"])
        elif row["Activity Type"] == "Warm-up Exercises":
            warm_up_exercises_space[row["Type"]] = int(row["Duration"])
        elif row["Activity Type"] == "Strength Training":
            strength_training_space[row["Type"]] = int(row["Duration"])
        elif row["Activity Type"] == "Stretching":
            stretching_space[row["Type"]] = int(row["Duration"])
        elif row["Activity Type"] == "Cardiovascular Training":
            cardiovascular_training_space[row["Type"]] = int(row["Duration"])