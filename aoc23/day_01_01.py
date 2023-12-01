import typing

from aoc23.util import day_01_input_lines


def day_01_first_last_digit(text: str) -> int:
    digits = list(filter(lambda c: c.isdigit(), text))
    return int(f"{digits[0]}{digits[-1]}")


def day_01_sum_calibration_values(texts: typing.Iterable[str]) -> int:
    return sum((day_01_first_last_digit(t) for t in texts))


def day_01_answer() -> int:
    return day_01_sum_calibration_values(texts=day_01_input_lines())


if __name__ == '__main__':
    print(f"Day 01: {day_01_answer()}")
