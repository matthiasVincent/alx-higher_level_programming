#!/usr/bin/python3
# 8-simple_delete.py

def simple_delete(given_dict, key=""):
    if key in given_dict:
        del given_dict[key]
    return (given_dict)
