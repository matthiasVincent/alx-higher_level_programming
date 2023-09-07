#!/usr/bin/python3
# 9-multiple_by_2.py

def multiply_by_2(given_dict):
    """Return a new dictionary with all values multipled by 2."""
    return ({k: given_dict[k] * 2 for k in given_dict})
