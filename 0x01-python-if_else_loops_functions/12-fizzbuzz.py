#!/usr/bin/python3

def fizzbuzz():
    """
    Prints the numbers from 1 to 100 separated by a space.
    For multiples of three, prints 'Fizz' instead of the number.
    For multiples of five, prints 'Buzz' instead of the number.
    For numbers which are multiples of both three and five, prints 'FizzBuzz'.

    Returns: None
    """
    for num in range(1, 101):
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz", end=" ")
        elif num % 3 == 0:
            print("Fizz", end=" ")
        elif num % 5 == 0:
            print("Buzz", end=" ")
        else:
            print(num, end=" ")
