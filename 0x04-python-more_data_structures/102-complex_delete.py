#!/usr/bin/python3
# 102-complex_delete.py

def complex_delete(given_dict, value):
    """Delete keys with a specific value in a dictionary."""
    while value in given_dict.values():
        for k, v in given_dict.items():
            if v == value:
                del given_dict[k]
                break

    return (given_dict)
