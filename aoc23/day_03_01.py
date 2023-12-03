import dataclasses
import itertools
import typing

from aoc23.util import input_lines


@dataclasses.dataclass(frozen=True)
class PartNo:
    y: int = dataclasses.field(hash=True, compare=True)
    x: int = dataclasses.field(hash=True, compare=True)
    x_end: int
    val: int

    def has(self, x: int, y: int) -> bool:
        return y == self.y and self.x_end >= x >= self.x


@dataclasses.dataclass
class Schematics:
    lines: list[str] = dataclasses.field(default_factory=list)

    @classmethod
    def from_multiline(cls, text: str) -> 'Schematics':
        return cls(lines=text.splitlines())

    def get_adjacents(self, x: int, y: int) -> set[tuple[int, int]]:
        bounded_x = set(max(0, min(v, len(self.lines[0]) - 1)) for v in [x - 1, x, x + 1])
        bounded_y = set(max(0, min(v, len(self.lines) - 1)) for v in [y - 1, y, y + 1])
        return set(itertools.product(bounded_x, bounded_y)) - {(x, y)}

    def all_numbers(self) -> typing.Iterable[PartNo]:
        for y, line in enumerate(self.lines):
            for (x, x_end, val) in self._numbers(line):
                yield PartNo(y=y, x=x, x_end=x_end, val=val)

    def part_numbers(self) -> typing.Iterable[PartNo]:
        part_numbers_set = set()
        all_numbers = set(self.all_numbers())
        for symbol_x, symbol_y in self.symbols():
            for adj_x, adj_y in self.get_adjacents(symbol_x, symbol_y):
                for n in all_numbers:
                    if n.has(adj_x, adj_y):
                        part_numbers_set.add(n)
        return part_numbers_set

    def symbols(self) -> typing.Iterable[tuple[int, int]]:
        for y, l in enumerate(self.lines):
            for x, ch in enumerate(l):
                if not ch.isdigit() and ch != '.':
                    yield x, y

    def _numbers(self, line: str) -> typing.Iterable[tuple[int, int, int]]:
        end = -1
        for x, ch in enumerate(line):
            if x > end and ch.isdigit():
                end = x
                try:
                    while len(line) > end and line[end + 1].isdigit():
                        end += 1
                except IndexError:
                    pass
                yield x, end, int(line[x:end + 1])


def day_03_pt1_answer(lines: typing.Iterable[str]) -> int:
    schematics = Schematics(lines=list(lines))
    part_numbers = schematics.part_numbers()
    return sum((p.val for p in part_numbers))


if __name__ == '__main__':
    day02pt1_answer = day_03_pt1_answer(lines=input_lines('input/day_03_gear_ratios.txt'))
    print(f"Day 02 pt1 answer is: {day02pt1_answer}")
