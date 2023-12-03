import collections
import typing

from aoc23.util import input_lines

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
    word_digits_forward = {text.find(w): v for w, v in WORD_DIGITS.items() if text.find(w) != -1}
    word_digits_reverse = {len(text) - 1 - (text[::-1].find(w[::-1]) + len(w) - 1): v
                           for w, v in WORD_DIGITS.items() if text.find(w) != -1}
    merged = collections.OrderedDict(
        sorted({**digit_position_to_val, **word_digits_forward, **word_digits_reverse}.items()))
    first_digit, last_digit = merged[min(merged.keys())], merged[max(merged.keys())]
    return int(f"{first_digit}{last_digit}")


def day_01_pt2_calibration_sum(texts: typing.Iterable[str]) -> int:
    return sum((day_01_pt2_parse_valibartion_value(t) for t in texts))


if __name__ == '__main__':
    print(f"Day 01, part 1 answer: {day_01_pt1_calibration_sum(texts=input_lines('input/day_01_calibration.txt'))}")
    print(f"Day 01, part 2 answer: {day_01_pt2_calibration_sum(texts=input_lines('input/day_01_calibration.txt'))}")
