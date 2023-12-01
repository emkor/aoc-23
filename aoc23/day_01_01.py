def day_01_first_last_digit(text: str) -> str:
    digits = list(filter(lambda c: c.isdigit(), text))
    return f"{digits[0]}{digits[-1]}"
