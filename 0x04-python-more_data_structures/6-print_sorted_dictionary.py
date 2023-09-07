#!/usr/bin/python3
# 6-print_sorted_dictionary.py

def print_sorted_dictionary(given_dict):
    """Print a dictionary by ordered keys."""
    [print("{}: {}".format(k, given_dict[k])) for k in sorted(given_dict)]
