import unittest

from aoc23.day_03_01 import Schematics, day_03_pt1_answer, day_03_pt2_answer, _gear_ratios
from aoc23.day_04 import Card, day_04_pt1_answer, day_04_pt2_answer

TEST_INPUT = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"""

TEST_INPUT_PT2 = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"""


class TestAocDay04Tests(unittest.TestCase):

    def test_pt1_should_parse_cards(self):
        card = Card.parse("Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53")
        assert card == Card(ix=1, winning={41, 48, 83, 86, 17}, got={83, 86, 6, 31, 17, 9, 48, 53})
        assert card.wins() == 4
        assert card.points() == 8

        card2 = Card.parse("Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19")
        assert card2 == Card(ix=2, winning={13, 32, 20, 16, 61}, got={61, 30, 68, 82, 17, 32, 24, 19})
        assert card2.wins() == 2
        assert card2.points() == 2

        card3 = Card.parse("Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1")
        assert card3 == Card(ix=3, winning={1, 21, 53, 59, 44}, got={69, 82, 63, 72, 16, 21, 14, 1})
        assert card3.wins() == 2
        assert card3.points() == 2

        card4 = Card.parse("Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83")
        assert card4 == Card(ix=4, winning={41, 92, 73, 84, 69}, got={59, 84, 76, 51, 58, 5, 54, 83})
        assert card4.wins() == 1
        assert card4.points() == 1

        card5 = Card.parse("Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36")
        assert card5 == Card(ix=5, winning={87, 83, 26, 28, 32}, got={88, 30, 70, 12, 93, 22, 82, 36})
        assert card5.wins() == 0
        assert card5.points() == 0

    def test_pt1_should_sum_points(self):
        points = day_04_pt1_answer(lines=TEST_INPUT.splitlines())
        assert points == 13

    def test_pt2_should_sum_points(self):
        points = day_04_pt2_answer(lines=TEST_INPUT_PT2.splitlines())
        assert points == 30
