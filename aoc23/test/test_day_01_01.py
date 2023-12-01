import unittest

from aoc23.day_01_01 import day_01_first_last_digit


class TestAocDay01Tests(unittest.TestCase):

    def test_day_01_should_get_first_last_digit(self):
        assert day_01_first_last_digit("1abc2") == "12"
        assert day_01_first_last_digit("pqr3stu8vwx") == "38"
        assert day_01_first_last_digit("a1b2c3d4e5f") == "15"
        assert day_01_first_last_digit("treb7uchet") == "77"
