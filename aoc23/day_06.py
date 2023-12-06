import dataclasses
import functools
import operator
import typing

from aoc23.util import input_lines


@dataclasses.dataclass
class Race:
    time: int = dataclasses.field(repr=True)
    distance: int = dataclasses.field(repr=True)

    def options_to_win(self) -> int:
        distances = [s * (self.time - s) for s in range(1, self.time)]
        return sum((d > self.distance for d in distances))


def parse_races(lines: typing.Iterable[str]) -> typing.Iterable[Race]:
    llines = list(lines)
    times = parse_line(llines[0].split(':')[1])
    distances = parse_line(llines[1].split(':')[1])
    yield from (Race(time=t, distance=d) for (t, d) in zip(times, distances))


def parse_line(line: str) -> list[int]:
    return [int(w.strip()) for w in line.split() if w.strip()]


def day_06_pt1_answer(lines: typing.Iterable[str]) -> int:
    races = list(parse_races(lines=lines))
    win_options = [r.options_to_win() for r in races]
    return functools.reduce(operator.mul, win_options)


if __name__ == '__main__':
    print(f"Day 06 pt1 answer: {day_06_pt1_answer(lines=input_lines('input/day_06_races.txt'))}")
