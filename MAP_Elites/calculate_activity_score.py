def calculate_activity_score(selected_activities):
    activity_score = [activity['Score'] for activity in selected_activities if 'SkillImprovement' in activity]
    return sum(activity_score)