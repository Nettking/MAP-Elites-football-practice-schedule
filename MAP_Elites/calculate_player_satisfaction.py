def calculate_player_satisfaction(selected_activities):
    
    # Calculate the total score for all the activities in the list
    total_score = sum([activity_scores.get(activity, 0) for activity in selected_activities])
    
    # Calculate the average score per activity
    num_activities = len(selected_activities)
    if num_activities > 0:
        average_score = total_score / num_activities
    else:
        average_score = 0
    
    # Normalize the average score to a range of [0, 1]
    normalized_score = (average_score - 1) / 4
    
    # Clamp the normalized score to the range [0, 1]
    normalized_score = max(0, min(1, normalized_score))
    
    return normalized_score