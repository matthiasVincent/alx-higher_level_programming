#!/usr/bin/python3
# 10-best_score.py

def best_score(given_dict):
    """Returns a key with the biggest integer value."""
    if not isinstance(given_dict, dict) or len(given_dict) == 0:
        return None

    ret = list(given_dict.keys())[0]
    big = given_dict[ret]
    for k, v in given_dict.items():
        if v > big:
            big = v
            ret = k
    return (ret)
