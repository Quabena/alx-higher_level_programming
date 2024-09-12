#!/usr/bin/python3
if __name__ == "__main__":
    from add_0 import add  # Importing the add function from add_0

    # Assign values to variables a and b
    a = 1
    b = 2

    # Using the add function and print to display the formatted result
    print("{} + {} = {}".format(a, b, add(a, b)))
