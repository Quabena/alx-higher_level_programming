#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    printed_count = 0
    try:
        for i in range(x):
            if isinstance(my_list[i], int):
                print("{:d}".format(my_list[i]), end="")
                printed_count += 1
    except IndexError:
        pass  # Ignore IndexError if x exceeds the list length
    print()  # Print a new line after printing integers
    return printed_count
