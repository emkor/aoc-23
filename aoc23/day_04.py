import dataclasses
import typing

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

    deck: dict[int, Card] = {c.ix: c for c in (Card.parse(l) for l in lines)}
    not_winning_ids = set()
    hand: list[int] = sorted(list(deck.keys()))
    i = 0

    while set(hand[i:]) != not_winning_ids and i < len(hand):
        print(f"#{i} hand len={len(hand)} not_winning_ids={not_winning_ids}")
        curr_card = deck[hand[i]]
        new_hand = _resolve_new_hand(curr_card, not_winning_ids)
        hand.extend(new_hand)
        i += 1
    return len(hand)


def _resolve_new_hand(curr_card: Card, not_winning_ids: set[int]):
    new_hand = []
    for next_card_ix in range(curr_card.ix + 1, curr_card.ix + 1 + curr_card.wins()):
        new_hand.append(next_card_ix)
    if not len(new_hand):
        not_winning_ids.add(curr_card.ix)
    return new_hand


if __name__ == '__main__':
    print(f"Day 04 pt1 answer: {day_04_pt1_answer(lines=input_lines('input/day_04_cards.txt'))}")
    print(f"Day 04 pt2 answer: {day_04_pt2_answer(lines=input_lines('input/day_04_cards.txt'))}")
