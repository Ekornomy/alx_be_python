def safe_divide(numerator, denominator):
    """
    Perform division with robust error handling.
    
    Parameters:
    numerator (str or float): The numerator
    denominator (str or float): The denominator
    
    Returns:
    str: Error message or string representation of result
    """
    try:
        # Try to convert inputs to floats (handles non-numeric inputs)
        num = float(numerator)
        den = float(denominator)
        
        # Try to perform division (handles division by zero)
        result = num / den
        
        # Return the result
        return f"The result of the division is {result}"
    
    except ValueError:
        # Handle non-numeric input (e.g., "ten" instead of "10")
        return "Error: Please enter numeric values only."
    
    except ZeroDivisionError:
        # Handle division by zero
        return "Error: Cannot divide by zero."
    
    except Exception as e:
        # Catch any other unexpected errors
        return f"Unexpected error occurred: {str(e)}"