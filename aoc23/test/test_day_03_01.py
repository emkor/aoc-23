import unittest

from aoc23.day_03_01 import Schematics, day_03_pt1_answer, day_03_pt2_answer, _gear_ratios

TEST_SCHEMATICS = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598.."""


class TestAocDay03Tests(unittest.TestCase):

    def test_day_03_pt1_should_get_adjacents(self):
        schema = Schematics.from_multiline(text=TEST_SCHEMATICS)
        assert schema.get_adjacents(0, 0) == {(0, 1), (1, 0), (1, 1)}
        assert schema.get_adjacents(9, 9) == {(8, 9), (9, 8), (8, 8)}
        assert schema.get_adjacents(1, 3) == {(0, 2), (1, 2), (2, 2), (0, 3), (2, 3), (0, 4), (1, 4), (2, 4)}
        assert schema.get_adjacents(0, 1) == {(0, 0), (1, 0), (1, 1), (0, 2), (1, 2)}

    def test_day_03_pt1_symbol_iterator(self):
        schema = Schematics.from_multiline(text=TEST_SCHEMATICS)
        symbols = list(schema.symbols())
        assert len(symbols) == 6
        assert symbols[0] == (3, 1)

    def test_day_03_pt1_line_numbers_iter(self):
        schema = Schematics.from_multiline(text=TEST_SCHEMATICS)
        vals = list(schema._numbers(line="467..114.."))
        assert vals == [(0, 2, 467), (5, 7, 114)]

    def test_day_03_pt1_all_numbers_iter(self):
        schema = Schematics.from_multiline(text=TEST_SCHEMATICS)
        vals = list(schema.all_numbers())
        assert len(vals) == 10

    def test_day_03_pt1_part_numbers_iter(self):
        schema = Schematics.from_multiline(text=TEST_SCHEMATICS)
        vals = list(schema.part_numbers())
        assert len(vals) == 8

    def test_day_03_pt1_answer(self):
        assert day_03_pt1_answer(lines=TEST_SCHEMATICS.split()) == 4361

    def test_day_03_pt2_gear_ratios(self):
        assert set(_gear_ratios(lines=TEST_SCHEMATICS.split())) == {16345, 451490}

    def test_day_03_pt2_answer(self):
        assert day_03_pt2_answer(lines=TEST_SCHEMATICS.split()) == 467835
