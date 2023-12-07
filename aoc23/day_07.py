from __future__ import annotations
import dataclasses
import functools
import typing
from collections import Counter

from aoc23.util import input_lines


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
    flag_pt2: bool = dataclasses.field(default=False)

    _c: list[tuple[str, int]] = dataclasses.field(default=None)
    _deck: str = dataclasses.field(default="AKQJT98765432")
    _deck_strengths: dict[str, int] = dataclasses.field(default=None)

    def __post_init__(self):
        if not self.flag_pt2:
            self._deck_strengths = {ch: len(self._deck) - i for i, ch in enumerate(self._deck)}
            _couter = Counter(sorted(self.cards, key=lambda ch: self._deck_strengths[ch], reverse=True))
            self._c = sorted([(ch, n) for ch, n in _couter.items()], key=lambda elem: elem[1], reverse=True)
        else:
            self._deck = "AKQT98765432J"
            self._deck_strengths = {ch: len(self._deck) - i for i, ch in enumerate(self._deck)}
            _couter = Counter(sorted(self.cards, key=lambda ch: self._deck_strengths[ch], reverse=True))
            j_count = _couter.pop("J", 0)
            self._c = sorted([(ch, n) for ch, n in _couter.items()], key=lambda elem: elem[1], reverse=True)
            if len(self._c):
                self._c[0] = (self._c[0][0], self._c[0][1] + j_count)
            else:
                self._c = [('J', j_count)]

        assert len(self.cards) == 5
        assert 0 <= self.bid <= 1000

    @classmethod
    def parse(cls, line: str, flag_pt2: bool = False) -> Hand:
        cards_txt, bid_txt = line.split(' ')
        return Hand(bid=int(bid_txt.strip()), cards=list(cards_txt), flag_pt2=flag_pt2)

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
        return [self._deck_strengths[ch] for ch in self.cards]


def parse_hands(lines: typing.Iterable[str], flag_pt2: bool = False) -> typing.Iterable[Hand]:
    yield from (Hand.parse(l, flag_pt2=flag_pt2) for l in lines)


def rank_times_bid(hands: typing.Iterable[Hand]) -> typing.Iterable[int]:
    yield from (i * h.bid for i, h in enumerate(sorted(hands), start=1))


def day_07_pt1_answer(lines: typing.Iterable[str]) -> int:
    return sum(rank_times_bid(parse_hands(lines=lines)))


def day_07_pt2_answer(lines: typing.Iterable[str]) -> int:
    return sum(rank_times_bid(parse_hands(lines=lines, flag_pt2=True)))


if __name__ == '__main__':
    print(f"Day 07 pt1 answer: {day_07_pt1_answer(lines=input_lines('input/day_07_hands.txt'))}")
    print(f"Day 07 pt2 answer: {day_07_pt2_answer(lines=input_lines('input/day_07_hands.txt'))}")
