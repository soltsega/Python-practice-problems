# Luhn algorithm is a simple checksum formula used to validate various identification numbers, such as credit card numbers, IMEI numbers, and social security numbers. It was created by Hans Peter Luhn in 1954 and is widely used in the financial industry to prevent accidental errors in data entry.

# The Luhn algorithm works by performing a series of calculations on the digits of the number being validated. The steps are as follows:
# 1. Starting from the rightmost digit, double the value of every second digit. If doubling the digit results in a number greater than 9, subtract 9 from the result.
# 2. Sum all the digits, including the modified digits from step 1.
# 3. If the sum is divisible by 10, the number is valid according to the Luhn algorithm.
# 4. If the sum is not divisible by 10, the number is invalid according to the Luhn algorithm.


def verify_card_number(card_number):
    # Step 1: Remove spaces and dashes
    cleaned = card_number.replace(' ', '').replace('-', '')
    
    # Step 2: Convert to a list of integers
    digits = [int(d) for d in cleaned]
    
    # Step 3: Apply Luhn algorithm
    # Start from the second-to-last digit, moving left
    for i in range(len(digits) - 2, -1, -2):
        doubled = digits[i] * 2
        # If doubling > 9, subtract 9
        if doubled > 9:
            doubled -= 9
        digits[i] = doubled
    
    # Step 4: Sum all digits
    total = sum(digits)
    
    # Step 5: Check if divisible by 10
    if total % 10 == 0:
        return "VALID!"
    else:
        return "INVALID!"    