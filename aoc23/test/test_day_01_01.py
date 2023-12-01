import unittest

from aoc23.day_01_01 import day_01_pt1_parse_calibration_value, day_01_pt1_calibration_sum, \
    day_01_pt2_parse_valibartion_value, day_01_pt2_calibration_sum


class TestAocDay01Tests(unittest.TestCase):


    def test_day_01_pt1_should_get_first_last_digit(self):
        assert day_01_pt1_parse_calibration_value("1abc2") == 12
        assert day_01_pt1_parse_calibration_value("pqr3stu8vwx") == 38
        assert day_01_pt1_parse_calibration_value("a1b2c3d4e5f") == 15
        assert day_01_pt1_parse_calibration_value("treb7uchet") == 77

    def test_day_01_pt1_should_sum_values(self):
        assert day_01_pt1_calibration_sum(["1abc2", "pqr3stu8vwx", "a1b2c3d4e5f", "treb7uchet"]) == 142

    def test_day_01_pt2_should_get_first_last_digit(self):
        assert day_01_pt2_parse_valibartion_value("two1nine") == 29
        assert day_01_pt2_parse_valibartion_value("eightwothree") == 83
        assert day_01_pt2_parse_valibartion_value("abcone2threexyz") == 13
        assert day_01_pt2_parse_valibartion_value("xtwone3four") == 24
        assert day_01_pt2_parse_valibartion_value("4nineeightseven2") == 42
        assert day_01_pt2_parse_valibartion_value("zoneight234") == 14
        assert day_01_pt2_parse_valibartion_value("7pqrstsixteen") == 76

    def test_day_01_pt2_should_sum_values(self):
        assert day_01_pt2_calibration_sum(["two1nine", "eightwothree", "abcone2threexyz", "xtwone3four", "4nineeightseven2", "zoneight234", "7pqrstsixteen"]) == 281
