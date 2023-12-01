import unittest

from aoc23.day_01_01 import day_01_pt1_parse_calibration_value, day_01_pt1_sum_calibration_values


class TestAocDay01Tests(unittest.TestCase):

    def test_day_01_should_get_first_last_digit(self):
        assert day_01_pt1_parse_calibration_value("1abc2") == 12
        assert day_01_pt1_parse_calibration_value("pqr3stu8vwx") == 38
        assert day_01_pt1_parse_calibration_value("a1b2c3d4e5f") == 15
        assert day_01_pt1_parse_calibration_value("treb7uchet") == 77

    def test_day_01_should_sum_values(self):
        assert day_01_pt1_sum_calibration_values(["1abc2", "pqr3stu8vwx", "a1b2c3d4e5f", "treb7uchet"]) == 142
