def main_function():
    # Define a variable and initialize it
    total_sum = 0

    # Call another function to calculate sum
    subtotal_1 = calculate_subtotal(numbers=[1, 2, 3])

    # Calculate final total
    total_sum += subtotal_1

    # Print the final total
    print(total_sum)


def calculate_subtotal(numbers):
    # Initialize subtotal to 0
    subtotal = 0

    # Loop over numbers and add them together
    for number in numbers:
        subtotal += calculate_inner_subtotal(number)

    return subtotal


def calculate_inner_subtotal(number):
    # Base case: if number is 0, return 0
    if number == 0:
        return 0

    # Recursive case: add current number to innersubtotal and recurse on remainder
    else:
        inner_subtotal = number % 2!= 0
        if inner_subtotal > 0:
            return calculate_inner_subtotal(number//2) + 1
        else:
            return calculate_inner_subtotal(number//2)
