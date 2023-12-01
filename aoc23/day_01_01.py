import collections
import typing

from aoc23.util import day_01_input_lines

WORD_DIGITS = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}


def day_01_pt1_parse_calibration_value(text: str) -> int:
    digits = list(filter(lambda c: c.isdigit(), text))
    return int(f"{digits[0]}{digits[-1]}")


def day_01_pt1_calibration_sum(texts: typing.Iterable[str]) -> int:
    return sum((day_01_pt1_parse_calibration_value(t) for t in texts))


def day_01_pt2_parse_valibartion_value(text: str) -> int:
    digit_position_to_val = {p: int(ch) for p, ch in enumerate(text) if ch.isdigit()}
    word_digit_pos_to_val = {text.find(w): v for w, v in WORD_DIGITS.items() if text.find(w) != -1}
    merged = collections.OrderedDict(sorted({**digit_position_to_val, **word_digit_pos_to_val}.items()))
    first_digit, last_digit = merged[min(merged.keys())], merged[max(merged.keys())]
    return int(f"{first_digit}{last_digit}")


def day_01_pt2_calibration_sum(texts: typing.Iterable[str]) -> int:
    return sum((day_01_pt2_parse_valibartion_value(t) for t in texts))


if __name__ == '__main__':
    print(f"Day 01, part 1 answer: {day_01_pt1_calibration_sum(texts=day_01_input_lines())}")
    print(f"Day 01, part 2 answer: {day_01_pt2_calibration_sum(texts=day_01_input_lines())}")
