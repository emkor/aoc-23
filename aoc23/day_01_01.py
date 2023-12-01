def day_01_first_last_digit(text: str) -> int:
    digits = list(filter(lambda c: c.isdigit(), text))
    return int(f"{digits[0]}{digits[-1]}")


def day_01_sum_calibration_values(texts: list[str]) -> int:
    return sum((day_01_first_last_digit(t) for t in texts))
