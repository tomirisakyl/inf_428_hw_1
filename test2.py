import math
import unittest

def cyclic_time_difference(time1: int, time2: int):
    angle1 = 2 * math.pi * time1 / 24
    angle2 = 2 * math.pi * time2 / 24
    
    angle_diff = abs(angle2 - angle1)
    
    if angle_diff > math.pi:
        angle_diff = 2 * math.pi - angle_diff
    
    cyclic_diff_hours = (angle_diff * 24) / (2 * math.pi)
    return round(cyclic_diff_hours, 2)

class TestCyclicTimeDifference(unittest.TestCase):
    
    def test_same_time(self):
        self.assertEqual(cyclic_time_difference(0, 0), 0.0)
        self.assertEqual(cyclic_time_difference(12, 12), 0.0)
        self.assertEqual(cyclic_time_difference(23, 23), 0.0)

    def test_adjacent_times(self):
        self.assertAlmostEqual(cyclic_time_difference(23, 0), 1.0, places=2)
        self.assertAlmostEqual(cyclic_time_difference(0, 23), 1.0, places=2)
        self.assertAlmostEqual(cyclic_time_difference(1, 0), 1.0, places=2)

    def test_opposite_times(self):
        self.assertAlmostEqual(cyclic_time_difference(0, 12), 12.0, places=2)
        self.assertAlmostEqual(cyclic_time_difference(12, 0), 12.0, places=2)
        
    def test_two_hour_cross_midnight(self):
        self.assertAlmostEqual(cyclic_time_difference(23, 1), 2.0, places=2)
        self.assertAlmostEqual(cyclic_time_difference(1, 23), 2.0, places=2)
    
    def test_four_hour_cross_midnight(self):
        self.assertAlmostEqual(cyclic_time_difference(21, 1), 4.0, places=2)
        self.assertAlmostEqual(cyclic_time_difference(22, 2), 4.0, places=2)

    def test_six_hour_cross_midnight(self):
        self.assertAlmostEqual(cyclic_time_difference(20, 2), 6.0, places=2)
        self.assertAlmostEqual(cyclic_time_difference(19, 1), 6.0, places=2)

    def test_eight_hour_cross_midnight(self):
        self.assertAlmostEqual(cyclic_time_difference(18, 2), 8.0, places=2)
        self.assertAlmostEqual(cyclic_time_difference(19, 3), 8.0, places=2)

    def test_ten_hour_cross_midnight(self):
        self.assertAlmostEqual(cyclic_time_difference(16, 2), 10.0, places=2)
        self.assertAlmostEqual(cyclic_time_difference(17, 3), 10.0, places=2)

    def test_two_hour_difference(self):
        self.assertAlmostEqual(cyclic_time_difference(15, 17), 2.0, places=2)
        self.assertAlmostEqual(cyclic_time_difference(9, 11), 2.0, places=2)
        self.assertAlmostEqual(cyclic_time_difference(6, 8), 2.0, places=2)

    def test_three_hour_difference(self):
        self.assertAlmostEqual(cyclic_time_difference(11, 14), 3.0, places=2)
        self.assertAlmostEqual(cyclic_time_difference(10, 13), 3.0, places=2)
        self.assertAlmostEqual(cyclic_time_difference(5, 8), 3.0, places=2)
    
    def test_four_hour_difference(self):
        self.assertAlmostEqual(cyclic_time_difference(9, 13), 4.0, places=2)
        self.assertAlmostEqual(cyclic_time_difference(7, 11), 4.0, places=2)
    
    def test_five_hour_difference(self):
        self.assertAlmostEqual(cyclic_time_difference(6, 11), 5.0, places=2)
        self.assertAlmostEqual(cyclic_time_difference(9, 14), 5.0, places=2)
       
    def test_six_hour_difference(self):
        self.assertAlmostEqual(cyclic_time_difference(6, 12), 6.0, places=2)
        self.assertAlmostEqual(cyclic_time_difference(9, 15), 6.0, places=2)
    
    def test_seven_hour_difference(self):
        self.assertAlmostEqual(cyclic_time_difference(6, 13), 7.0, places=2)
        self.assertAlmostEqual(cyclic_time_difference(9, 16), 7.0, places=2)
    
    def test_eight_hour_difference(self):
        self.assertAlmostEqual(cyclic_time_difference(6, 14), 8.0, places=2)
        self.assertAlmostEqual(cyclic_time_difference(9, 17), 8.0, places=2)

    def test_nine_hour_difference(self):
        self.assertAlmostEqual(cyclic_time_difference(6, 15), 9.0, places=2)
        self.assertAlmostEqual(cyclic_time_difference(9, 18), 9.0, places=2)

    def test_ten_hour_difference(self):
        self.assertAlmostEqual(cyclic_time_difference(6, 16), 10.0, places=2)
        self.assertAlmostEqual(cyclic_time_difference(9, 19), 10.0, places=2)

if __name__ == '__main__':
    unittest.main()

