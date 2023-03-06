class ActivityPlan:

    def __init__(self, monday_workout, wednesday_workout, saturday_workout):
        self.monday_workout = monday_workout
        self.wednesday_workout = wednesday_workout
        self.saturday_workout = saturday_workout


    @property
    def main_activity_types(self):
        distinct_list = []
        for activity_type in self.monday_workout.main_activity_types:
            if activity_type not in distinct_list:
                distinct_list.append(activity_type)
        for activity_type in self.wednesday_workout.main_activity_types:
            if activity_type not in distinct_list:
                distinct_list.append(activity_type)
        for activity_type in self.saturday_workout.main_activity_types:
            if activity_type not in distinct_list:
                distinct_list.append(activity_type)
        return distinct_list

    _total_score = -1

    @property
    def total_score(self):
        if (self._total_score >= 0):
            return self._total_score

        number_of_activity_types = len(self.main_activity_types)
        weigth_number_of_activity_types = 1
        weighted_number_of_activity_types_score = weigth_number_of_activity_types * number_of_activity_types

        activity_score = self.monday_workout.activity_score + self.wednesday_workout.activity_score + self.saturday_workout.activity_score
        weigth_activity_score = 2
        weighted_activity_score = weigth_activity_score * activity_score

        activity_injury = self.monday_workout.activity_injury + self.wednesday_workout.activity_injury + self.saturday_workout.activity_injury
        weigth_activity_injury = 10
        weighted_activity_injury = weigth_activity_injury * activity_injury

        skill_improvement = self.monday_workout.activity_skill_improvement + self.wednesday_workout.activity_skill_improvement + self.saturday_workout.activity_skill_improvement
        weigth_skill_improvement = 3
        weighted_skill_improvement = weigth_skill_improvement * skill_improvement
        
        duration_deviation = self.monday_workout.duration_deviation + self.wednesday_workout.duration_deviation + self.saturday_workout.duration_deviation
        weigth_duration_deviation = 5
        weighted_duration_deviation = weigth_duration_deviation * duration_deviation

        _total_score = weighted_number_of_activity_types_score + weighted_activity_score - weighted_activity_injury + weighted_skill_improvement - weighted_duration_deviation

        return _total_score

        
    def print_details(self):
        print("Monday:")
        self.monday_workout.print_details()
        print("Wednesday:")
        self.wednesday_workout.print_details()
        print("Saturday:")
        self.saturday_workout.print_details()
        print("Score: " + str(self.total_score))
