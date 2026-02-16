def convert_temperature(value: float, unit: str) -> float | str:
    if unit == 'C':
        result = (value * 9 / 5) + 32
        return round(result, 1)
    elif unit == 'F':
        result = (value - 32) * 5 / 9
        return round(result, 1)
    else:
        return "Invalid Unit"


# Sample Tests
assert convert_temperature(0, 'C') == 32.0
assert convert_temperature(100, 'F') == 37.8
assert convert_temperature(100, 'C') == 212.0
assert convert_temperature(-40, 'F') == -40.0
assert convert_temperature(25, 'K') == "Invalid Unit"
