#!/usr/bin/python3
#4-fibonacci.py

def fibonacci_sequence(n):
    if n <= 0:
        return []  # Return an empty list for n <= 0
    elif n == 1:
        return [0]  # Return [0] for n == 1
    else:
        fibonacci_numbers = [0, 1]  # Initialize the list with the first two Fibonacci numbers

        while len(fibonacci_numbers) < n:
            next_number = fibonacci_numbers[-1] + fibonacci_numbers[-2]
            fibonacci_numbers.append(next_number)

        return fibonacci_numbers[:n] 