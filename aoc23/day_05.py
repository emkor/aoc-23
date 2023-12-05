import dataclasses
import typing
from collections import abc

from aoc23.util import input_lines


@dataclasses.dataclass(frozen=True)
class Range:
    range_start_dst: int = dataclasses.field(repr=True)
    range_start_src: int = dataclasses.field(repr=True)
    range_len: int = dataclasses.field(repr=True)

    def get_dst(self, src: int) -> int | None:
        if self.is_src_in(src):
            return (src - self.range_start_src) + self.range_start_dst
        return None

    def get_src(self, dst: int) -> int | None:
        if self.is_dst_in(dst):
            return (dst - self.range_start_dst) + self.range_start_src
        return None

    def is_src_in(self, src: int) -> bool:
        return 0 <= (src - self.range_start_src) < self.range_len

    def is_dst_in(self, dst: int) -> bool:
        return 0 <= (dst - self.range_start_dst) < self.range_len

    @classmethod
    def parse(cls, line: str) -> 'Range':
        vals = line.split(" ")
        return cls(range_start_dst=int(vals[0].strip()),
                   range_start_src=int(vals[1].strip()),
                   range_len=int(vals[2].strip()))


@dataclasses.dataclass
class Mapping(abc.Mapping):
    def __getitem__(self, __key):
        return self.get_dst(__key)

    def __len__(self):
        raise NotImplementedError

    def __iter__(self):
        raise NotImplementedError

    ranges_sort_src: list[Range]
    ranges_sort_dst: list[Range]

    @classmethod
    def parse(cls, lines: list[str]) -> 'Mapping':
        ranges = [Range.parse(line) for line in lines]
        return Mapping(ranges_sort_src=sorted(ranges, key=lambda r: r.range_start_src, reverse=True),
                       ranges_sort_dst=sorted(ranges, key=lambda r: r.range_start_dst, reverse=True))

    def get_dst(self, src: int) -> int:
        for r in self.ranges_sort_src:
            if r.range_start_src <= src:
                return r.get_dst(src) or src
        return src

    def get_src(self, dst: int) -> int:
        for r in self.ranges_sort_dst:
            if r.range_start_dst <= dst:
                return r.get_src(dst) or dst
        return dst

    def ranges_count(self) -> int:
        return len(self.ranges_sort_src)


def parse_input(lines: typing.Iterable[str], parse_seeds_func: typing.Callable) -> tuple[list[int], list[Mapping]]:
    seeds = []
    maps = []
    curr_map_lines = []
    for i, l in enumerate(lines):
        if l.startswith("seeds: "):
            seeds = parse_seeds_func(l)
            continue
        elif not l.strip():
            continue
        elif l.endswith("map:"):
            if curr_map_lines:
                maps.append(Mapping.parse(curr_map_lines))
                curr_map_lines = []
            continue
        else:
            # case with range line
            curr_map_lines.append(l)

    maps.append(Mapping.parse(curr_map_lines))
    return seeds, maps


def parse_seeds_pt1(line: str):
    return [int(seed_str.strip()) for seed_str in line.split(": ")[-1].split(" ") if seed_str.strip()]


def resolve_categories(seed: int, maps: list[Mapping]) -> list[int]:
    # first val is seed number, later -> all the mappings, last is location
    output = [seed]
    for m in maps:
        output.append(m.get_dst(output[-1]))
    return output


def day_05_pt1_answer(seeds: list[int], maps: list[Mapping]) -> int:
    locations = []
    for s in seeds:
        locations.append(resolve_categories(s, maps)[-1])
    return sorted(locations)[0]


if __name__ == '__main__':
    seeds, mappings = parse_input(lines=input_lines('input/day_05_seeds.txt'), parse_seeds_func=parse_seeds_pt1)
    print(f"Day 05 pt1 answer: {day_05_pt1_answer(seeds, mappings)}")
