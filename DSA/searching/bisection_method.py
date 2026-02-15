def square_root_bisection(number, tolerance=1e-7, max_iterations=100):
    # Requirement: Raise ValueError for negative numbers
    if number < 0:
        raise ValueError("Square root of negative number is not defined in real numbers")
    
    # Requirement: Handle 0 and 1 specifically
    if number == 0 or number == 1:
        print(f"The square root of {number} is {number}")
        return number

    # Set the search range
    # For numbers < 1, the root is larger than the number, so we use max(1, number)
    low = 0
    high = max(1, number)
    
    for i in range(max_iterations):
        mid = (low + high) / 2
        
        # Check convergence based on the interval width
        # This ensures the root is captured within the required precision
        if (high - low) <= tolerance:
            print(f"The square root of {number} is approximately {mid}")
            return mid
        
        if mid**2 < number:
            low = mid
        else:
            high = mid
            
    # If the loop finishes without hitting the tolerance
    print(f"Failed to converge within {max_iterations} iterations")
    return None