import unittest
import numpy as np
from main import generate_random_data, aggregate_company_score

class TestCybersecurityAggregation(unittest.TestCase):
    def setUp(self):
        self.data_all_same = [
            generate_random_data(50, 5, 100),  
            generate_random_data(50, 5, 100),  
            generate_random_data(50, 5, 100),  
        ]

        self.data_one_high = [
            generate_random_data(85, 10, 100),  
            generate_random_data(20, 5, 100),   
            generate_random_data(20, 5, 100),  
        ]

        self.data_high_variance = [
            generate_random_data(50, 5, 100),   
            generate_random_data(50, 25, 100),  
            generate_random_data(50, 5, 100),   
        ]

        self.data_different_users = [
            generate_random_data(50, 5, 10),    
            generate_random_data(50, 5, 200), 
            generate_random_data(50, 5, 50),   
        ]

    def test_all_departments_same_mean(self):
        result = aggregate_company_score(self.data_all_same)
        self.assertTrue(0 <= result <= 90)

    def test_one_department_high_mean(self):
        result = aggregate_company_score(self.data_one_high)
        self.assertTrue(0 <= result <= 90)

    def test_high_variance_in_one_department(self):
        result = aggregate_company_score(self.data_high_variance)
        self.assertTrue(0 <= result <= 90)

    def test_different_user_counts(self):
        result = aggregate_company_score(self.data_different_users)
        self.assertTrue(0 <= result <= 90)

    def test_empty_department(self):
        data = []
        result = aggregate_company_score(data)
        self.assertEqual(result, 0)

    def test_single_department(self):
        data = [generate_random_data(50, 5, 100)]
        result = aggregate_company_score(data)
        self.assertTrue(0 <= result <= 90)

    def test_all_maximum_scores(self):
        data = [np.full(100, 90) for _ in range(5)]
        result = aggregate_company_score(data)
        self.assertEqual(result, 90)

    def test_all_minimum_scores(self):
        data = [np.full(100, 0) for _ in range(5)]
        result = aggregate_company_score(data)
        self.assertEqual(result, 0)

    def test_extreme_variance_across_departments(self):
        data = [
            generate_random_data(80, 5, 50),
            generate_random_data(20, 5, 150),
            generate_random_data(90, 5, 10),
        ]
        result = aggregate_company_score(data)
        self.assertTrue(0 <= result <= 90)

    def test_realistic_distribution(self):
        data = [
            generate_random_data(35, 15, 60),
            generate_random_data(55, 20, 80),
            generate_random_data(25, 10, 200),
            generate_random_data(75, 10, 150),
            generate_random_data(45, 10, 100),
        ]
        result = aggregate_company_score(data)
        self.assertTrue(0 <= result <= 90)

    def test_randomized_scores(self):
        np.random.seed(42)  
        data = [
            generate_random_data(np.random.randint(20, 70), 10, np.random.randint(50, 200))
            for _ in range(5)
        ]
        result = aggregate_company_score(data)
        self.assertTrue(0 <= result <= 90)

    def test_one_high_scoring_user(self):
        data = [
            np.append(generate_random_data(20, 5, 99), [90]),  
            generate_random_data(20, 5, 100),
            generate_random_data(20, 5, 100),
        ]
        result = aggregate_company_score(data)
        self.assertTrue(0 <= result <= 90)

    def test_one_empty_department(self):
        data = [
            [],
            generate_random_data(50, 5, 100),
            generate_random_data(50, 5, 100),
        ]
        result = aggregate_company_score(data)
        self.assertTrue(0 <= result <= 90)

    def test_large_user_count(self):
        data = [
            generate_random_data(50, 5, 1000), 
            generate_random_data(50, 5, 100),
        ]
        result = aggregate_company_score(data)
        self.assertTrue(0 <= result <= 90)

    def test_small_user_count(self):
        data = [
            generate_random_data(50, 5, 5), 
            generate_random_data(50, 5, 5),
        ]
        result = aggregate_company_score(data)
        self.assertTrue(0 <= result <= 90)

    def test_mixed_distributions(self):
        data = [
            generate_random_data(20, 5, 50),
            generate_random_data(70, 5, 150),
            generate_random_data(40, 5, 200),
            generate_random_data(60, 5, 10),
        ]
        result = aggregate_company_score(data)
        self.assertTrue(0 <= result <= 90)

    def test_highest_possible_variance(self):
        data = [
            generate_random_data(45, 45, 100),  
            generate_random_data(45, 45, 100),
        ]
        result = aggregate_company_score(data)
        self.assertTrue(0 <= result <= 90)

    def test_duplicate_departments(self):
        data = [
            generate_random_data(50, 5, 100),
            generate_random_data(50, 5, 100),
            generate_random_data(50, 5, 100),
        ]
        result = aggregate_company_score(data)
        self.assertTrue(0 <= result <= 90)


if __name__ == '__main__':
    unittest.main()
