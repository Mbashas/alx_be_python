def safe_divide(numerator,denominator):
    """
    # The issue with your error handling implementation is that the ValueError exception will never be caught because the float() conversion happens before the try block. When invalid input is provided, the ValueError is raised during the conversion, outside of the try block.
    numerator=float(numerator)
    denominator=float(denominator)
    """
    try:   
        numerator=float(numerator)
        denominator=float(denominator)
# We're converting the input values to floating-point numbers using float() 
    
        result = numerator/denominator
        return f"The result of the division is {result}"
    except ZeroDivisionError:
        return f"Error: Cannot divide by zero."
        
    except ValueError:
        return f"Error: Please enter numeric values only."

    
    