def calculate_skill_level_improvement(selected_activities):
    skill_improvements = [activity['SkillImprovement'] for activity in selected_activities if 'SkillImprovement' in activity]
    return sum(skill_improvements)