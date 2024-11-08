import numpy as np

def generate_random_data(mean, variance, num_samples):
    return np.random.randint(max(mean - variance, 0), min(mean + variance + 1, 90), num_samples)

def calculate_department_score(threat_scores, importance):
    average_score = np.mean(threat_scores)
    weighted_score = average_score * importance
    return weighted_score

def aggregate_company_score(department_data):
    total_weighted_score = 0
    total_importance = 0
    for scores, importance in department_data:
        department_score = calculate_department_score(scores, importance)
        total_weighted_score += department_score
        total_importance += importance
    return min(90, max(0, total_weighted_score / total_importance))



