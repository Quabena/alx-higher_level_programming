#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    a_el1 = tuple_a[0] if len(tuple_a) > 0 else 0
    a_el2 = tuple_a[1] if len(tuple_a) > 1 else 0
    b_el1 = tuple_b[0] if len(tuple_b) > 0 else 0
    b_el2 = tuple_b[1] if len(tuple_b) > 1 else 0

    sum_of_el1 = a_el1 + b_el1
    sum_of_el2 = a_el2 + b_el2

    return (sum_of_el1, sum_of_el2)
