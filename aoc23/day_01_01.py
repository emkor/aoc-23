def day_01_first_last_digit(text: str) -> str:
    digits = list(filter(None, [c if c.isdigit() else None for c in text]))
    return f"{digits[0]}{digits[-1]}"
