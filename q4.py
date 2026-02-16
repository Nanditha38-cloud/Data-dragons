def get_ticket_price(age: int, is_student: bool) -> int:
    if age < 12:
        return 8
    elif age >= 65:
        return 10
    else:
        if is_student:
            return 12
        else:
            return 15


# Sample Tests
assert get_ticket_price(10, False) == 8
assert get_ticket_price(70, True) == 10
assert get_ticket_price(20, True) == 12
assert get_ticket_price(25, False) == 15
assert get_ticket_price(12, False) == 15
