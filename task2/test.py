import unittest
import numpy as np
import csv
import os
import pandas as pd
from main import generate_random_data, aggregate_company_score

def save_to_csv(file_path, data):
    rows = []
    for department_id, department_data in data.items():  
        for user_id, score in enumerate(department_data):
            rows.append([department_id, user_id, score])
    
    df = pd.DataFrame(rows, columns=['department_id', 'user_id', 'score'])
    df.to_csv(file_path, index=False)  

def load_from_csv(file_path):
    df = pd.read_csv(file_path)
    data = {}
    for _, row in df.iterrows():
        department_id = row['department_id']
        score = row['score']
        if department_id not in data:
            data[department_id] = []
        data[department_id].append(score)
    return data


    

class TestCybersecurityAggregation(unittest.TestCase):
    CSV_DIR = "test_case_data"

    def setUp(self):
        os.makedirs(self.CSV_DIR, exist_ok=True)

    def load_or_generate_data(self, file_name, generate_function):
        file_path = os.path.join(self.CSV_DIR, file_name)
        if os.path.exists(file_path):
            return load_from_csv(file_path)
        else:
            data = generate_function()
            save_to_csv(file_path, data)
            return data

    def test_all_departments_same_mean(self):
        data = self.load_or_generate_data(
            "data_all_same.csv",
            lambda: [
                generate_random_data(50, 5, 100),
                generate_random_data(50, 5, 100),
                generate_random_data(50, 5, 100),
            ]
        )
        result = aggregate_company_score(data)
        self.assertTrue(0 <= result <= 90)

    def test_one_department_high_mean(self):
        data = self.load_or_generate_data(
            "data_one_high.csv",
            lambda: [
                generate_random_data(85, 10, 100),
                generate_random_data(20, 5, 100),
                generate_random_data(20, 5, 100),
            ]
        )
        result = aggregate_company_score(data)
        self.assertTrue(0 <= result <= 90)

    def test_high_variance_in_one_department(self):
        data = self.load_or_generate_data(
            "data_high_variance.csv",
            lambda: [
                generate_random_data(50, 5, 100),
                generate_random_data(50, 25, 100),
                generate_random_data(50, 5, 100),
            ]
        )
        result = aggregate_company_score(data)
        self.assertTrue(0 <= result <= 90)

    def test_different_user_counts(self):
        data = self.load_or_generate_data(
            "data_different_users.csv",
            lambda: [
                generate_random_data(50, 5, 10),
                generate_random_data(50, 5, 200),
                generate_random_data(50, 5, 50),
            ]
        )
        result = aggregate_company_score(data)
        self.assertTrue(0 <= result <= 90)

    def test_empty_department(self):
        data = self.load_or_generate_data("data_empty_department.csv", lambda: [])
        result = aggregate_company_score(data)
        self.assertEqual(result, 0)

    def test_single_department(self):
        data = self.load_or_generate_data(
            "data_single_department.csv",
            lambda: [generate_random_data(50, 5, 100)],
        )
        result = aggregate_company_score(data)
        self.assertTrue(0 <= result <= 90)
    
    def test_all_maximum_scores(self):
        data = self.load_or_generate_data(
            "data_all_maximum_scores.csv",
            lambda: [np.full(100, 90) for _ in range(5)],
        )
        result = aggregate_company_score(data)
        self.assertEqual(result, 90)

    def test_all_minimum_scores(self):
        data = self.load_or_generate_data(
            "data_all_minimum_scores.csv",
            lambda: [np.full(100, 0) for _ in range(5)],
        )
        result = aggregate_company_score(data)
        self.assertEqual(result, 0)

    def test_extreme_variance_across_departments(self):
        data = self.load_or_generate_data(
            "data_extreme_variance.csv",
            lambda: [
                generate_random_data(80, 5, 50),
                generate_random_data(20, 5, 150),
                generate_random_data(90, 5, 10),
            ],
        )
        result = aggregate_company_score(data)
        self.assertTrue(0 <= result <= 90)





    def test_one_high_scoring_user(self):
        data =  self.load_or_generate_data(
            "data_one_highscoring_user.csv",
            lambda:[
                np.append(generate_random_data(20, 5, 99), [90]),  
                generate_random_data(20, 5, 100),
                generate_random_data(20, 5, 100),
            ],
        )
        result = aggregate_company_score(data)
        self.assertTrue(0 <= result <= 90)

    def test_one_empty_department(self):
        data =  self.load_or_generate_data(
            "data_one_empty_department.csv",
            lambda: [
            [],
                generate_random_data(50, 5, 100),
                generate_random_data(50, 5, 100),
            ],
        )
        result = aggregate_company_score(data)
        self.assertTrue(0 <= result <= 90)

    def test_large_user_count(self):
        data =  self.load_or_generate_data(
            "data_large_user_count.csv",
            lambda: [
                generate_random_data(50, 5, 1000), 
                generate_random_data(50, 5, 100),
            ],
        )
        result = aggregate_company_score(data)
        self.assertTrue(0 <= result <= 90)

    def test_small_user_count(self):
        data = self.load_or_generate_data(
            "data_small_user_count.csv",
            lambda: [
                generate_random_data(50, 5, 5), 
                generate_random_data(50, 5, 5),
            ],
        )
        result = aggregate_company_score(data)
        self.assertTrue(0 <= result <= 90)

    def test_mixed_distributions(self):
        data =  self.load_or_generate_data(
            "data_mixed_distribution.csv",
            lambda: [
                generate_random_data(20, 5, 50),
                generate_random_data(70, 5, 150),
                generate_random_data(40, 5, 200),
                generate_random_data(60, 5, 10),
            ],
        )
        result = aggregate_company_score(data)
        self.assertTrue(0 <= result <= 90)

    def test_highest_possible_variance(self):
        data =  self.load_or_generate_data(
            "data_highest_possible_variance.csv",
            lambda: [
                generate_random_data(45, 45, 100),  
                generate_random_data(45, 45, 100),
            ],
        )
        result = aggregate_company_score(data)
        self.assertTrue(0 <= result <= 90)

    def test_extreme_low_mean(self):
        data =  self.load_or_generate_data(
            "data_extreme_low_mean.csv",
            lambda: [
                generate_random_data(10, 2, 100),
                generate_random_data(15, 3, 100),
                generate_random_data(12, 1, 100),
            ],
        )
        result = aggregate_company_score(data)
        self.assertTrue(0 <= result <= 90)

    def test_extreme_high_mean(self):
        data = self.load_or_generate_data(
            "data_extreme_high_mean.csv",
            lambda: [
                generate_random_data(85, 2, 100),
                generate_random_data(88, 3, 100),
                generate_random_data(89, 1, 100),
            ],
        )
        result = aggregate_company_score(data)
        self.assertTrue(0 <= result <= 90)

    def test_two_departments_identical_high_variance(self):
        data = self.load_or_generate_data(
            "data_two_identical_high_variance.csv",
            lambda: [
                generate_random_data(45, 40, 100),
                generate_random_data(45, 40, 100),
                generate_random_data(45, 5, 100),
            ],
        )
        result = aggregate_company_score(data)
        self.assertTrue(0 <= result <= 90)

    def test_high_and_low_variance_combined(self):
        data = self.load_or_generate_data(
            "data_high_and_low_variance.csv",
            lambda: [
                generate_random_data(50, 2, 100),
                generate_random_data(50, 20, 100),
            ],
        )
        result = aggregate_company_score(data)
        self.assertTrue(0 <= result <= 90)

    def test_one_department_all_max_scores(self):
        data = self.load_or_generate_data(
            "data_onedep_all_maxscores.csv",
            lambda:[
                np.full(100, 90),
                generate_random_data(50, 5, 100),
                generate_random_data(50, 5, 100),
            ],
        )
        result = aggregate_company_score(data)
        self.assertTrue(0 <= result <= 90)

    def test_one_department_all_min_scores(self):
        data = self.load_or_generate_data(
            "data_onedep_all_minscores.csv",
            lambda:[
                np.full(100, 0),
                generate_random_data(50, 5, 100),
                generate_random_data(50, 5, 100),
            ],
        )
        result = aggregate_company_score(data)
        self.assertTrue(0 <= result <= 90)

    def test_one_department_many_users_high_mean(self):
        data = self.load_or_generate_data(
            "data_onedep_manyusers_highmean.csv",
            lambda: [
                generate_random_data(85, 5, 500),
                generate_random_data(30, 5, 100),
                generate_random_data(30, 5, 100),
            ],
        )
        result = aggregate_company_score(data)
        self.assertTrue(0 <= result <= 90)

    def test_high_scores_fewer_users(self):
        data = self.load_or_generate_data(
            "data_high_scores_fewerusers.csv",
            lambda: [
                generate_random_data(85, 5, 10),
                generate_random_data(20, 5, 200),
                generate_random_data(50, 5, 100),
            ],
        )
        result = aggregate_company_score(data)
        self.assertTrue(0 <= result <= 90)

    def test_low_scores_fewer_users(self):
        data = self.load_or_generate_data(
            "data_low_scores_fewerusers.csv",
            lambda:[
                generate_random_data(15, 5, 10),
                generate_random_data(50, 5, 200),
                generate_random_data(50, 5, 100),
            ],
        )
        result = aggregate_company_score(data)
        self.assertTrue(0 <= result <= 90)


if __name__ == '__main__':
    unittest.main()
