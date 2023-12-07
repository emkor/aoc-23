from __future__ import annotations
import dataclasses
import functools
import typing
from collections import Counter

from aoc23.util import input_lines

CARDS = "AKQJT98765432"
STRENGTHS = {ch: len(CARDS) - i for i, ch in enumerate(CARDS)}


def compare_lists(a: list[int], b: list[int]) -> int:
    """1 = a > b, -1 = a < b, 0 = a==b"""
    for ia, ib in zip(a, b):
        if ia > ib:
            return 1
        elif ia < ib:
            return -1
        else:
            continue
    return 0


@functools.total_ordering
@dataclasses.dataclass
class Hand:
    bid: int
    cards: list[str]
    _c: list[tuple[str, int]] = dataclasses.field(default=None)

    def __post_init__(self):
        self._c = sorted([(ch, n) for ch, n in
                          Counter(sorted(self.cards, key=lambda ch: STRENGTHS[ch], reverse=True)).items()],
                         key=lambda elem: elem[1], reverse=True)
        assert len(self.cards) == 5
        assert 0 <= self.bid <= 1000

    @classmethod
    def parse(cls, line: str) -> Hand:
        cards_txt, bid_txt = line.split(' ')
        return Hand(bid=int(bid_txt.strip()), cards=list(cards_txt))

    def __eq__(self, other: Hand) -> bool:
        return compare_lists(self.fig_and_strengths(), other.fig_and_strengths()) == 0

    def __lt__(self, other: Hand) -> bool:
        return compare_lists(self.fig_and_strengths(), other.fig_and_strengths()) == -1

    def fig_and_strengths(self) -> list[int]:
        if self.is_five_of_a_kind():
            return [6] + self._strengths()
        elif self.is_four_of_a_kind():
            return [5] + self._strengths()
        elif self.is_full_house():
            return [4] + self._strengths()
        elif self.is_three_of_a_kind():
            return [3] + self._strengths()
        elif self.is_two_pair():
            return [2] + self._strengths()
        elif self.is_one_pair():
            return [1] + self._strengths()
        elif self.is_high_card():
            return [0] + self._strengths()
        else:
            raise ValueError(f"Can not classify hand: {self.cards}")

    def is_five_of_a_kind(self) -> bool:
        return self._counts() == [5]

    def is_four_of_a_kind(self) -> bool:
        return self._counts() == [4, 1]

    def is_full_house(self) -> bool:
        return self._counts() == [3, 2]

    def is_three_of_a_kind(self) -> bool:
        return self._counts() == [3, 1, 1]

    def is_two_pair(self) -> bool:
        return self._counts() == [2, 2, 1]

    def is_one_pair(self) -> bool:
        return self._counts() == [2, 1, 1, 1]

    def is_high_card(self) -> bool:
        return self._counts() == [1, 1, 1, 1, 1]

    def _counts(self) -> list[int]:
        return [count for strength, count in self._c]

    def _strengths(self) -> list[int]:
        return [STRENGTHS[ch] for ch in self.cards]


def parse_hands(lines: typing.Iterable[str]) -> typing.Iterable[Hand]:
    yield from (Hand.parse(l) for l in lines)


def rank_times_bid(hands: typing.Iterable[Hand]) -> typing.Iterable[int]:
    yield from (i * h.bid for i, h in enumerate(sorted(hands), start=1))


def day_07_pt1_answer(lines: typing.Iterable[str]) -> int:
    return sum(rank_times_bid(parse_hands(lines=lines)))


if __name__ == '__main__':
    print(f"Day 07 pt1 answer: {day_07_pt1_answer(lines=input_lines('input/day_07_hands.txt'))}")
