def calculate_check_digit_10(main_digits_list):
    digits_sum = 0
    # Use only the first 9 digits for calculation
    for index, digit in enumerate(main_digits_list[:9]):
        digits_sum += digit * (10 - index)
    
    result = 11 - (digits_sum % 11)
    
    if result == 11:
        return '0'
    elif result == 10:
        return 'X'
    else:
        return str(result)

def calculate_check_digit_13(main_digits_list):
    digits_sum = 0
    # Use only the first 12 digits for calculation
    for index, digit in enumerate(main_digits_list[:12]):
        if index % 2 == 0:
            digits_sum += digit * 1
        else:
            digits_sum += digit * 3
            
    result = 10 - (digits_sum % 10)
    
    if result == 10:
        return '0'
    else:
        return str(result)

def validate_isbn(isbn, length):
    # 1. Check if the actual length matches the input length
    if len(isbn) != length:
        print(f'ISBN-{length} code should be 10 digits long.' if length == 10 else f'ISBN-{length} code should be 13 digits long.')
        return

    # 2. Check for invalid characters (only digits allowed, except 'X' at the end of ISBN-10)
    for i, char in enumerate(isbn):
        if not char.isdigit():
            if length == 10 and i == 9 and char.upper() == 'X':
                continue
            print('Invalid character was found.')
            return

    # 3. Separate main digits and the given check digit
    # For ISBN-10, main is first 9. For ISBN-13, main is first 12.
    main_digits = [int(d) for d in isbn[:-1]]
    given_check_digit = isbn[-1].upper()

    # 4. Calculate expected check digit
    if length == 10:
        expected = calculate_check_digit_10(main_digits)
    else:
        expected = calculate_check_digit_13(main_digits)

    # 5. Final Comparison
    if given_check_digit == expected:
        print('Valid ISBN Code.')
    else:
        print('Invalid ISBN Code.')

def main():
    user_input = input('Enter ISBN and length: ')
    
    # Check for comma separation
    if ',' not in user_input:
        print('Enter comma-separated values.')
        return
        
    values = user_input.split(',')
    if len(values) != 2:
        print('Enter comma-separated values.')
        return

    isbn = values[0].strip()
    raw_length = values[1].strip()

    # Validate length is a number
    if not raw_length.isdigit():
        print('Length must be a number.')
        return
    
    length = int(raw_length)

    # Validate length is 10 or 13
    if length != 10 and length != 13:
        print('Length should be 10 or 13.')
        return

    validate_isbn(isbn, length)

# 1. You should comment out the call to the main function 
# to allow for the rest of the tests to work properly.
# main()