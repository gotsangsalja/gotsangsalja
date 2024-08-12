#include <stdio.h>

int calculate_inner_subtotal(int number);
int calculate_subtotal(int numbers[], int size);

void main_function() {
    // Define a variable and initialize it
    int total_sum = 0;

    // Define an array of numbers
    int numbers[] = {1, 2, 3};

    // Call another function to calculate sum
    int subtotal_1 = calculate_subtotal(numbers, 3);

    // Calculate final total
    total_sum += subtotal_1;

    // Print the final total
    printf("%d\n", total_sum);
}

int calculate_subtotal(int numbers[], int size) {
    // Initialize subtotal to 0
    int subtotal = 0;

    // Loop over numbers and add them together
    for (int i = 0; i < size; i++) {
        subtotal += calculate_inner_subtotal(numbers[i]);
    }

    return subtotal;
}

int calculate_inner_subtotal(int number) {
    // Base case: if number is 0, return 0
    if (number == 0) {
        return 0;
    }

    // Recursive case: add current number to innersubtotal and recurse on remainder
    else {
        int inner_subtotal = number % 2 != 0;
        if (inner_subtotal > 0) {
            return calculate_inner_subtotal(number / 2) + 1;
        } else {
            return calculate_inner_subtotal(number / 2);
        }
    }
}

int main() {
    main_function();
    return 0;
}
