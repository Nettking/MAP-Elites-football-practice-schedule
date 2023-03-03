import csv
import random

# Define the file path and name of the CSV file
csv_file = "drills_space.csv"

# Define the range of possible values for the new fields
min_score = 0
max_score = 30
min_injuries = 0
max_injuries = 10
min_skill_improvement = 0
max_skill_improvement = 10

# Open the CSV file and read the data
with open(csv_file, mode='r') as file:
    reader = csv.DictReader(file)
    rows = []
    for row in reader:
        # Generate random values for the new fields
        row["Score"] = random.randint(min_score, max_score)
        row["Injuries"] = random.randint(min_injuries, max_injuries)
        row["SkillImprovement"] = random.randint(min_skill_improvement, max_skill_improvement)
        rows.append(row)

# Write the updated data back to the CSV file
with open(csv_file, mode='w', newline='') as file:
    fieldnames = ["Activity Type", "Type", "Duration", "Score", "Injuries", "SkillImprovement"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)

print("CSV file updated successfully!")