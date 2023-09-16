#!/usr/bin/python3
#5-prime.py

def is_prime(number):
    if number <= 1:
        return False  # Numbers less than or equal to 1 are not prime

    # Check for divisibility from 2 to the square root of the number
    for divisor in range(2, int(number**0.5) + 1):
        if number % divisor == 0:
            return False  # Number is divisible by 'divisor', so it's not prime
    return True  # If no divisors were found, the number is prime
