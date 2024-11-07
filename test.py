import unittest
from main import generate_department_data, calculate_aggregated_threat_score

class TestCyberSecurityScore(unittest.TestCase):
    def test_generate_department_data(self):
        # Test that the generated data is within expected ranges
        threat_scores, importance = generate_department_data()
        self.assertGreaterEqual(len(threat_scores), 10)
        self.assertLessEqual(len(threat_scores), 200)
        self.assertGreaterEqual(importance, 1)
        self.assertLessEqual(importance, 5)

    def test_balanced_case(self):
        department_data = [
            ([20, 25, 30], 3),
            ([20, 22, 18], 3),
            ([22, 25, 21], 3),
            ([24, 26, 23], 3),
            ([20, 20, 22], 3),
        ]
        score = calculate_aggregated_threat_score(department_data)
        self.assertAlmostEqual(score, 22, delta=1)

    def test_outlier_case(self):
        department_data = [
            ([5, 10, 5], 2),
            ([90, 88, 92], 5),
            ([20, 22, 18], 3),
            ([5, 5, 5], 2),
            ([20, 22, 18], 3),
        ]
        score = calculate_aggregated_threat_score(department_data)
        self.assertGreater(score, 40)

    def test_varying_importance(self):
        department_data = [
            ([30, 35, 40], 1),
            ([50, 55, 60], 2),
            ([10, 15, 20], 3),
            ([25, 30, 35], 4),
            ([45, 50, 55], 5),
        ]
        score = calculate_aggregated_threat_score(department_data)
        self.assertTrue(0 <= score <= 90)

    def test_high_risk_department(self):
        department_data = [
            ([5, 5, 5], 2),
            ([90, 90, 90], 3),
            ([10, 10, 10], 4),
            ([5, 5, 5], 2),
            ([15, 15, 15], 3),
        ]
        score = calculate_aggregated_threat_score(department_data)
        # Adjust threshold if necessary
        self.assertGreater(score, 30)  # Adjusted threshold if needed


if __name__ == '__main__':
    unittest.main()
