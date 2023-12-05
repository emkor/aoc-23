import unittest

from aoc23.day_05 import Range, Mapping, parse_input, day_05_pt1_answer, resolve_categories, parse_seeds_pt1
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
        map_range = Range.parse("50 98 2")
        assert map_range.is_src_in(95) is False
        assert map_range.is_src_in(102) is False
        assert map_range.is_src_in(98) is True
        assert map_range.is_src_in(99) is True
        assert map_range.is_dst_in(2) is False
        assert map_range.is_dst_in(57) is False
        assert map_range.is_dst_in(50) is True
        assert map_range.is_dst_in(51) is True

        assert map_range.get_dst(99) == 51
        assert map_range.get_src(50) == 98
        assert map_range.get_src(4) is None
        assert map_range.get_dst(106) is None

    def test_pt1_should_parse_map(self):
        mapping = Mapping.parse(lines=SINGLE_MAP_INPUT.splitlines())
        assert mapping.ranges_sort_src[-1] == Range(39, 0, 15)
        assert mapping.ranges_sort_dst[-1] == Range(0, 15, 37)
        assert mapping.get_dst(53) == 38
        assert mapping.get_src(36) == 51

    def test_pt1_should_parse_full_input(self):
        seeds, maps = parse_input(lines=FULL_TEST_INPUT.splitlines(), parse_seeds_func=parse_seeds_pt1)
        assert seeds == [79, 14, 55, 13]
        assert len(maps) == 7
        assert len(maps[0].ranges_sort_src) == 2
        assert len(maps[-1].ranges_sort_src) == 2

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
