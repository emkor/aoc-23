import unittest

from aoc23.day_06 import parse_races, Race, day_06_pt1_answer

TEST_INPUT = """Time:      7  15   30
Distance:  9  40  200"""


class TestAocDay06Tests(unittest.TestCase):

    def test_pt1_should_parse_races(self):
        races = list(parse_races(lines=TEST_INPUT.splitlines()))
        assert len(races) == 3
        assert races[0] == Race(time=7, distance=9)
        assert races[-1] == Race(time=30, distance=200)

    def test_pt1_options_to_win(self):
        assert Race(time=7, distance=9).options_to_win() == 4
        assert Race(time=15, distance=40).options_to_win() == 8
        assert Race(time=30, distance=200).options_to_win() == 9

    def test_pt1_answer(self):
        assert day_06_pt1_answer(lines=TEST_INPUT.splitlines()) == 288
