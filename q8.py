def sanitize_email(raw_input: str) -> str:
    """
    Clean an email string and validate basic structure.

    Args:
        raw_input: A string containing a potential email address.

    Returns:
        The cleaned lowercase email or "Invalid Email".
    """
    # Step 1: Remove leading/trailing whitespace
    cleaned = raw_input.strip()
    
    # Step 2: Convert to lowercase
    cleaned = cleaned.lower()
    
    # Step 3: Check if it contains exactly one "@"
    if cleaned.count("@") == 1 and cleaned != "":
        return cleaned
    
    # Step 4: If invalid
    return "Invalid Email"



# Test Case 1: Standard cleaning
assert sanitize_email("  User@Example.com  ") == "user@example.com"

# Test Case 2: No whitespace
assert sanitize_email("test@domain.org") == "test@domain.org"

# Test Case 3: Missing @ symbol
assert sanitize_email("myname-website.com") == "Invalid Email"

# Test Case 4: Multiple @ symbols
assert sanitize_email("admin@@company.com") == "Invalid Email"

# Test Case 5: Empty input after stripping
assert sanitize_email("   ") == "Invalid Email"

print("All test cases passed!")
