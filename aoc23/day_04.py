import dataclasses
import typing

from aoc23.util import input_lines


@dataclasses.dataclass
class Card:
    ix: int
    winning: set[int]
    got: set[int]

    def points(self) -> int:
        return 2 ** (self.wins() - 1) if self.wins() else 0

    def wins(self) -> int:
        return len(self.got.intersection(self.winning))

    @classmethod
    def parse(cls, line: str) -> 'Card':
        card_id, card_details = line.split(": ")
        card_winning, card_got = card_details.split(" | ")
        index = int(card_id.split(" ")[-1].strip())
        return cls(ix=index,
                   winning={int(n.strip()) for n in card_winning.split(" ") if n.strip()},
                   got={int(n.strip()) for n in card_got.split(" ") if n.strip()})


def day_04_pt1_answer(lines: typing.Iterable[str]) -> int:
    return sum((Card.parse(l).points() for l in lines))


if __name__ == '__main__':
    print(f"Day 04 pt1 answer: {day_04_pt1_answer(lines=input_lines('input/day_04_cards.txt'))}")
