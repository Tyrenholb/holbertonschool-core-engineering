#!/usr/bin/env python3
def add_tuple(tuple_a=(), tuple_b=()):
    tupa = (tuple_a + (0, 0))[:2]
    tupb = (tuple_b + (0, 0))[:2]
    first_result = tupa[0] + tupb[0]
    second_result = tupa[1] + tupb[1]
    return (first_result, second_result)
