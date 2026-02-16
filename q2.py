def convert_seconds(total_seconds: int) -> str:
    """
    Convert total seconds into minutes and remaining seconds.
    
    Args:
        total_seconds: An integer representing time in seconds.
    
    Returns:
        A string formatted as "Xm Ys".
    """
    # Determine the number of full minutes using integer division
    minutes = total_seconds // 60
    
    # Determine the remaining seconds using the modulo operator
    seconds = total_seconds % 60
    
    # Return the result in the format "Xm Ys"
    return f"{minutes}m {seconds}s"


# Test the function with the provided test cases
print(convert_seconds(125))     # Should output: 2m 5s
print(convert_seconds(60))      # Should output: 1m 0s
print(convert_seconds(45))      # Should output: 0m 45s
print(convert_seconds(3600))    # Should output: 60m 0s
print(convert_seconds(0))       # Should output: 0m 0s





2nd dhi
