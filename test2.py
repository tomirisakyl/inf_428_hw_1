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
        
    def test_cross_midnight(self):
        self.assertAlmostEqual(cyclic_time_difference(23, 1), 2.0, places=2)
        self.assertAlmostEqual(cyclic_time_difference(1, 23), 2.0, places=2)
    
    def test_various_times(self):
        self.assertAlmostEqual(cyclic_time_difference(3, 15), 12.0, places=2)
        self.assertAlmostEqual(cyclic_time_difference(9, 21), 12.0, places=2)
        self.assertAlmostEqual(cyclic_time_difference(6, 18), 12.0, places=2)

    def test_large_cross_boundary_difference(self):
        self.assertAlmostEqual(cyclic_time_difference(22, 2), 4.0, places=2)
        self.assertAlmostEqual(cyclic_time_difference(1, 20), 5.0, places=2)

if __name__ == '__main__':
    unittest.main()

