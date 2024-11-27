import numpy as np

def generate_random_data(mean, variance, num_samples):
    return np.random.randint(max(mean - variance, 0), min(mean + variance + 1, 90), num_samples)

def aggregate_company_score(department_data):
    median_scores = [np.median(scores) for scores in department_data.values() if len(scores) > 0]
    if not median_scores:
        return 0  
    company_score = np.mean(median_scores)
    return min(90, max(0, company_score)) 


  




