def calculate_total_bill(amount: float, tip_percent: int) -> float:
    """
    Calculate the total bill including tip.
    
    Args:
        amount: The initial bill amount (numeric)
        tip_percent: The tip percentage (integer)
    
    Returns:
        The total bill rounded to 2 decimal places.
    """
    # Convert inputs to float to ensure decimal precision
    amount = float(amount)
    tip_percent = float(tip_percent)
    
    # Calculate the total using the formula
    total = amount + (amount * tip_percent / 100)
    
    # Return the result rounded to 2 decimal places
    return round(total, 2)


# Test the function with the provided test cases
print(calculate_total_bill(100.0, 15))    # Should output: 115.0
print(calculate_total_bill(55.50, 20))    # Should output: 66.6
print(calculate_total_bill(200, 0))       # Should output: 200.0
print(calculate_total_bill(12.99, 10))    # Should output: 14.29
print(calculate_total_bill(0, 15))        # Should output: 0.0
