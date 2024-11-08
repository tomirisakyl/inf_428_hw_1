import unittest
from main import generate_random_data, calculate_department_score, aggregate_company_score

class TestCybersecurityAggregation(unittest.TestCase):
    
    def setUp(self):
        self.uniform_data = [
            (generate_random_data(45, 5, 100), 3),
            (generate_random_data(45, 5, 100), 3),
            (generate_random_data(45, 5, 100), 3),
            (generate_random_data(45, 5, 100), 3),
            (generate_random_data(45, 5, 100), 3),
        ]
    
    def test_uniform_department_conditions(self):
        result = aggregate_company_score(self.uniform_data)
        self.assertTrue(0 <= result <= 90)
    
    def test_high_threat_in_critical_department(self):
        critical_data = [
            (generate_random_data(80, 10, 100), 5),  
            (generate_random_data(20, 5, 100), 2),
            (generate_random_data(20, 5, 100), 2),
            (generate_random_data(20, 5, 100), 2),
            (generate_random_data(20, 5, 100), 2),
        ]
        result = aggregate_company_score(critical_data)
        self.assertTrue(0 <= result <= 90)
    
    def test_varying_user_counts(self):
        varying_users_data = [
            (generate_random_data(50, 5, 10), 3),
            (generate_random_data(50, 5, 200), 3),
            (generate_random_data(50, 5, 50), 3),
            (generate_random_data(50, 5, 100), 3),
            (generate_random_data(50, 5, 150), 3),
        ]
        result = aggregate_company_score(varying_users_data)
        self.assertTrue(0 <= result <= 90)

    def test_extreme_variance(self):
        extreme_data = [
            (generate_random_data(85, 5, 50), 4),  
            (generate_random_data(10, 5, 150), 2),
            (generate_random_data(85, 5, 30), 5),
            (generate_random_data(10, 5, 80), 1),
            (generate_random_data(50, 10, 100), 3),
        ]
        result = aggregate_company_score(extreme_data)
        self.assertTrue(0 <= result <= 90)

    def test_randomized_distribution(self):
        random_data = [
            (generate_random_data(35, 15, 60), 1),
            (generate_random_data(55, 20, 80), 2),
            (generate_random_data(25, 10, 200), 4),
            (generate_random_data(75, 10, 150), 5),  
            (generate_random_data(45, 10, 100), 3),
        ]
        result = aggregate_company_score(random_data)
        self.assertTrue(0 <= result <= 90)

if __name__ == '__main__':
    unittest.main()

