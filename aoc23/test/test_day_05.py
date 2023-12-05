import unittest

from aoc23.day_05 import MapRange, Mapping, parse_input, day_05_pt1_answer, resolve_categories, parse_seeds_pt1, \
    parse_seeds_pt2, Range
from aoc23.util import input_lines

SINGLE_MAP_INPUT = """0 15 37
37 52 2
39 0 15"""

FULL_TEST_INPUT = """seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4"""


class TestAocDay05Tests(unittest.TestCase):

    def test_pt1_should_parse_ranges(self):
        map_range = MapRange.parse("50 98 2")
        assert (95 in map_range.src) is False
        assert (102 in map_range.src) is False
        assert (98 in map_range.src) is True
        assert (99 in map_range.src) is True
        assert (2 in map_range.dst) is False
        assert (57 in map_range.dst) is False
        assert (50 in map_range.dst) is True
        assert (51 in map_range.dst) is True

        assert map_range.get_dst(99) == 51
        assert map_range.get_src(50) == 98
        assert map_range.get_src(4) is None
        assert map_range.get_dst(106) is None

    def test_pt1_should_parse_map(self):
        mapping = Mapping.parse(label="soil-to-fertilizer", lines=SINGLE_MAP_INPUT.splitlines())
        assert mapping.ranges_src[-1] == MapRange(dst=Range(39, 15), src=Range(0, 15))
        assert mapping.ranges_dst[-1] == MapRange(dst=Range(0, 37), src=Range(15, 37))
        assert mapping.get_dst(53) == 38
        assert mapping.get_src(36) == 51

    def test_pt1_should_parse_full_input(self):
        seeds, maps = parse_input(lines=FULL_TEST_INPUT.splitlines(), parse_seeds_func=parse_seeds_pt1)
        assert seeds == [79, 14, 55, 13]
        assert len(maps) == 7
        assert len(maps[0].ranges_src) == 2
        assert len(maps[-1].ranges_src) == 2

    def test_pt1_should_resolve_all_categories(self):
        seeds, maps = parse_input(lines=FULL_TEST_INPUT.splitlines(), parse_seeds_func=parse_seeds_pt1)
        seed_to_categories = {
            s: resolve_categories(seed=s, maps=maps) for s in seeds
        }
        assert seed_to_categories[79] == [79, 81, 81, 81, 74, 78, 78, 82]
        assert seed_to_categories[14] == [14, 14, 53, 49, 42, 42, 43, 43]
        assert seed_to_categories[55] == [55, 57, 57, 53, 46, 82, 82, 86]
        assert seed_to_categories[13] == [13, 13, 52, 41, 34, 34, 35, 35]

    def test_pt1_should_get_answer(self):
        seeds, maps = parse_input(lines=FULL_TEST_INPUT.splitlines(), parse_seeds_func=parse_seeds_pt1)
        assert day_05_pt1_answer(seeds, maps) == 35

    def test_pt1_parsing_input(self):
        seeds, mappings = parse_input(lines=input_lines('input/day_05_seeds.txt'), parse_seeds_func=parse_seeds_pt1)
        assert len(seeds) == 20
        assert len(mappings) == 7

    def test_pt2_range_resolve(self):
        test_range = Range(4, 7)

        assert len(test_range) == 3
        assert test_range.resolve(Range(1, 3)) == (None, Range(1, 3), None)
        assert test_range.resolve(Range(2, 5)) == (Range(4, 5), Range(2, 3), None)
        assert test_range.resolve(Range(4, 6)) == (Range(4, 6), None, None)
        assert test_range.resolve(Range(6, 9)) == (Range(6, 7), None, Range(8, 9))
        assert test_range.resolve(Range(8, 10)) == (None, None, Range(8, 10))
        assert test_range.resolve(Range(1, 10)) == (Range(4, 7), Range(1, 3), Range(8, 10))

    def test_pt2_parse_seeds(self):
        seeds_ranges = list(parse_seeds_pt2("seeds: 79 14 55 13"))
        assert sum((s.len for s in seeds_ranges)) == 27
        assert seeds_ranges[0] == Range(start=79, len=14)
        assert seeds_ranges[-1] == Range(start=55, len=13)
