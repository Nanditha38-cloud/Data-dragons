def average_passing_grades(grades: list[int]) -> float:
    total = 0
    count = 0

    for grade in grades:
        if grade >= 50:
            total += grade
            count += 1

    if count == 0:
        return 0.0

    return total / count


# Sample Tests
assert average_passing_grades([40, 60, 80, 20]) == 70.0
assert average_passing_grades([50, 100]) == 75.0
assert average_passing_grades([10, 20, 30]) == 0.0
assert average_passing_grades([85]) == 85.0
assert average_passing_grades([]) == 0.0
