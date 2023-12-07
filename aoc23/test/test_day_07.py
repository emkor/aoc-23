import unittest

from aoc23.day_07 import compare_lists, Hand, parse_hands, day_07_pt1_answer, rank_times_bid, day_07_pt2_answer
from aoc23.util import input_lines

TEST_INPUT = """32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483
"""


class TestAocDay07Tests(unittest.TestCase):

    def test_pt1_should_compare_strengths(self):
        assert compare_lists([1, 1, 3, 4], [1, 5, 1, 1]) == -1
        assert compare_lists([10, 10, 10], [10, 10, 10]) == 0
        assert compare_lists([10, 10, 11], [10, 10, 10]) == 1

    def test_pt1_should_parse_hand(self):
        h = Hand.parse("32T3K 765")
        assert h.cards == ["3", "2", "T", "3", "K"]
        assert h.bid == 765
        assert h.is_five_of_a_kind() is False
        assert h.is_four_of_a_kind() is False
        assert h.is_three_of_a_kind() is False
        assert h.is_two_pair() is False
        assert h.is_one_pair() is True

    def test_pt1_should_calc_strength(self):
        h = Hand.parse("32T3K 765")
        assert h.fig_and_strengths() == [1, 2, 1, 9, 2, 12]

    def test_pt1_should_compare_hands(self):
        hands = list(parse_hands(TEST_INPUT.splitlines()))
        assert (hands[0] == hands[0]) is True
        assert (hands[1] > hands[0]) is True
        assert (hands[1] > hands[2]) is True
        assert (hands[2] > hands[0]) is True
        assert (hands[0] < hands[1]) is True
        assert (hands[2] < hands[1]) is True

    def test_pt1_should_sort_hands(self):
        hands = list(parse_hands(TEST_INPUT.splitlines()))
        hands_cards_sorted = ["".join(h.cards) for h in sorted(hands)]
        assert hands_cards_sorted == ['32T3K', 'KTJJT', 'KK677', 'T55J5', 'QQQJA']

    def test_pt1_recognize_higher_types(self):
        assert Hand.parse("QTTTT 115").is_four_of_a_kind() is True
        assert Hand.parse("77727 509").is_four_of_a_kind() is True
        assert Hand.parse("KK9K9 860").is_full_house() is True
        assert Hand.parse("78878 431").is_full_house() is True
        assert Hand.parse("99999 1").is_five_of_a_kind() is True
        assert Hand.parse("6K4T9 583").fig_and_strengths() == [0, 5, 12, 3, 9, 8]

    def test_pt1_sort_higher_types(self):
        hands = [
            Hand.parse("QTTTT 115"),
            Hand.parse("77727 509"),
            Hand.parse("KK9K9 860"),
            Hand.parse("78878 431"),
            Hand.parse("99999 1"),
            Hand.parse("6K4T9 583")
        ]
        hands_cards_sorted = ["".join(h.cards) for h in sorted(hands)]
        assert hands_cards_sorted == ['6K4T9', '78878', 'KK9K9', '77727', 'QTTTT', '99999']

        assert list(rank_times_bid(hands)) == [583, 431 * 2, 860 * 3, 509 * 4, 115 * 5, 1 * 6]
        assert sum(rank_times_bid(hands)) == 583 * 1 + 431 * 2 + 860 * 3 + 509 * 4 + 115 * 5 + 1 * 6

    def test_pt1_another_set_sorted(self):
        hands = [
            Hand.parse("8K56A 619"),
            Hand.parse("TTT4T 826"),
            Hand.parse("K88Q8 542"),
            Hand.parse("AQAA6 200"),
            Hand.parse("QQQKT 116"),
            Hand.parse("Q47Q9 859"),
            Hand.parse("2626J 909"),
            Hand.parse("6JTJJ 249"),
        ]
        hands_cards_sorted = ["".join(h.cards) for h in sorted(hands)]
        assert hands_cards_sorted == ['8K56A', 'Q47Q9', '2626J', '6JTJJ', 'QQQKT', 'K88Q8', 'AQAA6', 'TTT4T']

    def test_pt1_should_parse_full_input(self):
        hands = list(parse_hands(lines=input_lines('input/day_07_hands.txt')))
        assert len(hands) == 1000
        assert hands[0].bid == 252
        assert hands[0].cards == list("486AA")
        assert hands[-1].bid == 32
        assert hands[-1].cards == list("6646T")

    def test_pt1_should_get_answer(self):
        hands = list(parse_hands(TEST_INPUT.splitlines()))
        assert list(rank_times_bid(hands)) == [765 * 1, 220 * 2, 28 * 3, 684 * 4, 483 * 5]

        assert day_07_pt1_answer(lines=TEST_INPUT.splitlines()) == 6440

    def test_pt2_should_parse_hand(self):
        h = Hand.parse("T55J5 684", flag_pt2=True)
        assert h.cards == ["T", "5", "5", "J", "5"]
        assert h.bid == 684
        assert h.is_five_of_a_kind() is False
        assert h.is_four_of_a_kind() is True
        assert h.is_three_of_a_kind() is False
        assert h.is_two_pair() is False
        assert h.is_one_pair() is False

    def test_pt2_should_calc_strength(self):
        h = Hand.parse("KTJJT 220", flag_pt2=True)
        assert h.fig_and_strengths() == [5, 12, 10, 1, 1, 10]

    def test_pt2_should_get_answer(self):
        assert day_07_pt2_answer(lines=TEST_INPUT.splitlines()) == 5905
