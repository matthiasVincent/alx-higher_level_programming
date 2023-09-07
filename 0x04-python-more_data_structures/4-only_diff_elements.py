#!/usr/bin/python3
# 4-only_diff_elements.py

def only_diff_elements(first_set, second_set):
    """Return a set of all elements present in only one set."""
    return (first_set ^ second_set)
