#!/usr/bin/env python3
def best_score(a_dictionary):

    if not a_dictionary:
        return None

    high_key = next(iter(a_dictionary))

    for key in a_dictionary:
        a_dictionary[key] > a_dictionary[high_key]
        if a_dictionary[key] > a_dictionary[high_key]:
            high_key = key

    return high_key
