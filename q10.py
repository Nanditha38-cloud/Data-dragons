def organize_scores(scores: list[int], descending: bool) -> list[int]:
    """
    Sort scores without modifying the original list.

    Args:
        scores: A list of integers.
        descending: Boolean indicating sort order.

    Returns:
        A new sorted list of integers.
    """
    return sorted(scores, reverse=descending)
# Test Case 1: Ascending order
print(organize_scores([10, 5, 8], False))
# Expected Output: [5, 8, 10]

# Test Case 2: Descending order
print(organize_scores([10, 5, 8], True))
# Expected Output: [10, 8, 5]

# Test Case 3: Verify original list is not changed
original = [3, 1, 2]
organize_scores(original, True)
print(original)
# Expected Output: [3, 1, 2]

# Test Case 4: Already sorted
print(organize_scores([1, 2, 3], False))
# Expected Output: [1, 2, 3]

# Test Case 5: Empty list
print(organize_scores([], False))
# Expected Output: []
