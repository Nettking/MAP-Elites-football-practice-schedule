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
        activity_data = {
            "Type": str(row["Type"]),
            "Duration": int(row["Duration"]),
            "Score": float(row["Score"]),
            "Injury": float(row["Injuries"]),
            "SkillImprovement": float(row["SkillImprovement"])
        }
        if row["Activity Type"] == "Running Drills":
            if row["Type"] not in running_drills_space:
                running_drills_space[row["Type"]] = []
            running_drills_space[row["Type"]].append(activity_data)
        elif row["Activity Type"] == "Passing Drills":
            if row["Type"] not in passing_drills_space:
                passing_drills_space[row["Type"]] = []
            passing_drills_space[row["Type"]].append(activity_data)
        elif row["Activity Type"] == "Defensive Drills":
            if row["Type"] not in defensive_drills_space:
                defensive_drills_space[row["Type"]] = []
            defensive_drills_space[row["Type"]].append(activity_data)
        elif row["Activity Type"] == "Offensive Drills":
            if row["Type"] not in offensive_drills_space:
                offensive_drills_space[row["Type"]] = []
            offensive_drills_space[row["Type"]].append(activity_data)
        elif row["Activity Type"] == "Agility Drills":
            if row["Type"] not in agility_drills_space:
                agility_drills_space[row["Type"]] = []
            agility_drills_space[row["Type"]].append(activity_data)
        elif row["Activity Type"] == "Warm-up Exercises":
            if row["Type"] not in warm_up_exercises_space:
                warm_up_exercises_space[row["Type"]] = []
            warm_up_exercises_space[row["Type"]].append(activity_data)
        elif row["Activity Type"] == "Strength Training":
            if row["Type"] not in strength_training_space:
                strength_training_space[row["Type"]] = []
            strength_training_space[row["Type"]].append(activity_data)
        elif row["Activity Type"] == "Stretching":
            if row["Type"] not in stretching_space:
                stretching_space[row["Type"]] = []
            stretching_space[row["Type"]].append(activity_data)
        elif row["Activity Type"] == "Cardiovascular Training":
            if row["Type"] not in cardiovascular_training_space:
                cardiovascular_training_space[row["Type"]] = []
            cardiovascular_training_space[row["Type"]].append(activity_data)
print(running_drills_space)