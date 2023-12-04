import dataclasses
import time
import typing
from functools import lru_cache

from aoc23.util import input_lines


@dataclasses.dataclass(frozen=True)
class Card:
    ix: int = dataclasses.field(compare=True, hash=True)
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


def day_04_pt2_answer(lines: typing.Iterable[str]) -> int:
    @lru_cache(maxsize=256)
    def _resolve_new_hand(card_ix: int) -> list[int]:
        return list(range(card_ix + 1, card_ix + 1 + deck[card_ix].wins()))

    deck: dict[int, Card] = {c.ix: c for c in (Card.parse(l) for l in lines)}
    queue: list[int] = sorted(list(deck.keys()))
    processed: int = 0
    start_time = time.time()

    while queue:
        curr_card_ix = queue.pop(0)
        print(f"card_ix={curr_card_ix} processed={processed} queue={len(queue)}")
        queue = _resolve_new_hand(curr_card_ix) + queue
        processed += 1

    end_time = time.time()
    print(f"Processed {processed} items in {end_time - start_time:.3f}s ({processed / (end_time - start_time) / 1000:.1f}kop/s)")
    return processed


if __name__ == '__main__':
    print(f"Day 04 pt1 answer: {day_04_pt1_answer(lines=input_lines('input/day_04_cards.txt'))}")
    print(f"Day 04 pt2 answer: {day_04_pt2_answer(lines=input_lines('input/day_04_cards.txt'))}")
