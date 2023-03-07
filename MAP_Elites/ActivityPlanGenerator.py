import random
import copy
from Activity import *
from Workout import *
from ActivityPlan import *

class ActivityPlanGenerator:

    def __init__(self, all_warmup_excercises, all_main_excercises, all_stretching_excercises):
        self.all_warmup_excercises = all_warmup_excercises
        self.all_main_excercises = all_main_excercises
        self.all_stretching_excercises = all_stretching_excercises

    def is_not_added(self, exercises, new_exercise):
        for exercise in exercises:
            if exercise.activity_type == new_exercise.activity_type and exercise.activity_name == new_exercise.activity_name:
                return False
        return True

    def get_exercise_not_already_added(self, exercises, all_excercises):
        done = False
        while done==False:
            new_exercise = random.choice([x for x in all_excercises if x not in exercises])
            if self.is_not_added(exercises, new_exercise):
                done = True
        return(new_exercise)

    def calculate_duration(self, exercises):
        duration = 0
        for exercise in exercises:
            duration += exercise.duration
        return duration

    def generate_random_warmup_excercises(self):
        exercises = []
        while self.calculate_duration(exercises) < 15:
            exercises.append(self.get_exercise_not_already_added(exercises, self.all_warmup_excercises))
        return exercises

    def generate_random_main_exercises(self):
        exercises = []
        while self.calculate_duration(exercises) < 60:
            exercises.append(self.get_exercise_not_already_added(exercises, self.all_main_excercises))
        return exercises

    def generate_random_stretching_exercises(self):
        exercises = []
        while self.calculate_duration(exercises) < 15:
            exercises.append(self.get_exercise_not_already_added(exercises, self.all_stretching_excercises)) 
        return exercises

    def generate_random_workout(self):
        warmup_excercises = self.generate_random_warmup_excercises()
        main_exercises = self.generate_random_main_exercises()
        stretching_exercises = self.generate_random_stretching_exercises()
        return Workout(warmup_excercises, main_exercises, stretching_exercises)

    def generate_random_activity_plan(self):
        monday_workout = self.generate_random_workout()
        wednesday_workout = self.generate_random_workout()
        saturday_workout = self.generate_random_workout()
        return ActivityPlan(monday_workout, wednesday_workout, saturday_workout)

    @staticmethod
    def activities_not_in_list(dominent_activities, recessive_activities):
        result = recessive_activities.copy()
        for activity in result:
            for dominent_activity in dominent_activities:
                if (activity.activity_type == dominent_activity.activity_type and activity.activity_name == dominent_activity.activity_name):
                    try:
                        result.remove(activity)
                    except:
                        pass
        return result

    @staticmethod
    def crossover_activity_list(dominent_activities, recessive_activities):
        result = dominent_activities.copy()
        activity_index_to_remove = random.randrange(len(result))
        print("FJERNER " + result[activity_index_to_remove].activity_type + " - " + result[activity_index_to_remove].activity_name) 
        removed_element = result.pop(activity_index_to_remove)
        candidate_activities = ActivityPlanGenerator.activities_not_in_list(dominent_activities, recessive_activities)
        if (len(candidate_activities) == 0):
            return dominent_activities.copy()
        activity_index_to_add = random.randrange(len(candidate_activities))
        print("LEGGER TIL " + candidate_activities[activity_index_to_add].activity_type + " - " + candidate_activities[activity_index_to_add].activity_name) 
        result.append(recessive_activities[activity_index_to_add])
        return result

    @staticmethod
    def crossover_day(dominent_day, recessive_day):
        result = copy.deepcopy(dominent_day)
        parts = ['warmup', 'main', 'stretching']
        random_part = random.choice(parts)
        setattr(result, f'{random_part}_exercises', ActivityPlanGenerator.crossover_activity_list(getattr(dominent_day, f'{random_part}_exercises'), getattr(recessive_day, f'{random_part}_exercises')))
        return result

    @staticmethod
    def crossover(activity_plan1, activity_plan2):

        if (activity_plan1.total_score > activity_plan2.total_score):
            dominent = activity_plan1
            rescesive = activity_plan2
        else:
            dominent = activity_plan2
            rescesive = activity_plan1

        result = copy.deepcopy(dominent)

        random_day = random.randint(1, 3)

        workout_dict = {
            1: ('Monday', 'monday_workout'),
            2: ('Wednesday', 'wednesday_workout'),
            3: ('Saturday', 'saturday_workout')
        }

        day, attr_name = workout_dict[random_day]
        workout = ActivityPlanGenerator.crossover_day(getattr(dominent, attr_name), getattr(rescesive, attr_name))
        setattr(result, attr_name, workout)

        print("Changed workout plan for", day)
 

        return result
    