import random

# Function to generate random department data
def generate_department_data(num_users_min=10, num_users_max=200, importance_min=1, importance_max=5):
    num_users = random.randint(num_users_min, num_users_max)
    importance = random.randint(importance_min, importance_max)
    threat_scores = [random.randint(0, 90) for _ in range(num_users)]
    return threat_scores, importance

# Function to calculate aggregated threat score
def calculate_aggregated_threat_score(department_data):
    total_weighted_score = 0
    total_importance = 0
    for threat_scores, importance in department_data:
        avg_threat_score = sum(threat_scores) / len(threat_scores)
        # Further amplify importance weight
        weighted_importance = importance ** 3
        total_weighted_score += avg_threat_score * weighted_importance
        total_importance += weighted_importance
    
    aggregated_score = total_weighted_score / total_importance
    return min(max(aggregated_score, 0), 90)


