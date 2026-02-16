def generate_threes(start: int, end: int) -> list[int]:
    """
    Generate a list of numbers from start to end, skipping by 3.

    Args:
        start: The starting integer.
        end: The integer to stop before.

    Returns:
        A list of integers incremented by 3.
    """
    if start >= end:
        return []
    
    return list(range(start, end, 3))




# Test Case 1: Standard range
assert generate_threes(1, 11) == [1, 4, 7, 10]

# Test Case 2: Exact multiple
assert generate_threes(0, 9) == [0, 3, 6]

# Test Case 3: Start equals end
assert generate_threes(5, 5) == []

# Test Case 4: Start greater than end
assert generate_threes(20, 10) == []

# Test Case 5: Starting from a negative number
assert generate_threes(-5, 5) == [-5, -2, 1, 4]

print("All test cases passed!")
