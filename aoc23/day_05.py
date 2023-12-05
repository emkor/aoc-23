from __future__ import annotations
import dataclasses
import time
import typing

from aoc23.util import input_lines


@dataclasses.dataclass(frozen=True)
class Range:
    start: int = dataclasses.field(repr=True, hash=True, compare=True)  # inclusive
    len: int = dataclasses.field(repr=True, hash=True, compare=True)  # inclusive

    def __len__(self) -> int:
        return self.len

    @property
    def end(self) -> int:
        return self.start + self.len

    def __lt__(self, other: Range):
        return self.start < other.start

    def __contains__(self, other: Range | int) -> bool:
        if isinstance(other, int):
            return self.start <= other <= self.end
        elif isinstance(other, Range):
            return self.start <= other.start and self.end >= other.end

    def __getitem__(self, n: int) -> int:
        if n < self.len:
            return self.start + n
        else:
            raise IndexError(f"Can not get element {n} from {str(self)}")

    def pos(self, val: int) -> int | None:
        return (val - self.start) if val in self else None

    def resolve(self, o: Range) -> tuple[Range | None, Range | None, Range | None]:
        if o.end < self.start:
            return None, Range(o.start, o.end), None
        elif o.start < self.start and o.end <= self.end:
            return Range(self.start, o.end), Range(o.start, self.start - 1), None
        elif o.start >= self.start and o.end <= self.end:
            return Range(o.start, o.end), None, None
        elif self.end >= o.start >= self.start and o.end > self.end:
            return Range(o.start, self.end), None, Range(self.end + 1, o.end)
        elif o.start > self.end:
            return None, None, Range(o.start, o.end)
        elif o.start < self.start and o.end > self.end:
            return Range(self.start, self.end), Range(o.start, self.start - 1), Range(self.end + 1, o.end)


@dataclasses.dataclass(frozen=True)
class MapRange:
    src: Range = dataclasses.field(repr=True)
    dst: Range = dataclasses.field(repr=True)

    @property
    def range_len(self) -> int:
        return len(self.src)

    def get_dst(self, src: int) -> int:
        if src in self.src:
            return self.dst[self.src.pos(src)]

    def get_src(self, dst: int) -> int:
        if dst in self.dst:
            return self.src[self.dst.pos(dst)]

    def resolve_dst(self, other: Range) -> tuple[Range | None, Range | None, Range | None]:
        return self.dst.resolve(other)

    def resolve_src(self, other: Range) -> tuple[Range | None, Range | None, Range | None]:
        return self.src.resolve(other)

    @classmethod
    def parse(cls, line: str) -> MapRange:
        vals = line.split(" ")
        src_start = int(vals[1].strip())
        dst_start = int(vals[0].strip())
        src_len = int(vals[2].strip())
        return cls(src=Range(src_start, src_len),
                   dst=Range(dst_start, src_len))


@dataclasses.dataclass
class Mapping:
    ranges_src: list[MapRange]
    ranges_dst: list[MapRange]

    @classmethod
    def parse(cls, lines: list[str]) -> 'Mapping':
        ranges: list[MapRange] = [MapRange.parse(line) for line in lines]
        return Mapping(ranges_src=sorted(ranges, key=lambda r: r.src.start, reverse=True),
                       ranges_dst=sorted(ranges, key=lambda r: r.dst.start, reverse=True))

    def get_dst(self, src: int) -> int:
        for r in self.ranges_src:
            if r.src.start <= src:
                return r.get_dst(src) or src
        return src

    def get_src(self, dst: int) -> int:
        for r in self.ranges_dst:
            if r.dst.start <= dst:
                return r.get_src(dst) or dst
        return dst

    def ranges_count(self) -> int:
        return len(self.ranges_src)


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


def parse_seeds_pt1(line: str) -> typing.Iterable[int]:
    return [int(seed_str.strip()) for seed_str in line.split(": ")[-1].split(" ") if seed_str.strip()]


def resolve_categories(seed: int, maps: list[Mapping]) -> list[int]:
    # first val is seed number, later -> all the mappings, last is location
    output = [seed]
    for m in maps:
        output.append(m.get_dst(output[-1]))
    return output


def day_05_pt1_answer(seeds: list[int], maps: list[Mapping]) -> int:
    print(f"Resolving categories for {len(seeds)}")
    start_time = time.time()
    locations = []
    for i, s in enumerate(seeds):
        print(f"#{i}/{len(seeds)} ({time.time() - start_time:.2f}s) Resolving categories for seed #{s}")
        locations.append(resolve_categories(s, maps)[-1])
    end_time = time.time()
    print(f"Done resolving categories for {len(seeds)} in {end_time - start_time:.2f}seconds")
    return sorted(locations)[0]


if __name__ == '__main__':
    seeds, mappings = parse_input(lines=input_lines('input/day_05_seeds.txt'), parse_seeds_func=parse_seeds_pt1)
    print(f"Day 05 pt1 answer: {day_05_pt1_answer(seeds, mappings)}")
