#!/usr/bin/python3
"""Defines a peak-finding algorithm."""


def find_peak(list_of_integers):
    """Return a peak in a list of unsorted integers."""
    if list_of_integers == []:
        return None

    size = len(list_of_integers)
    if size == 1:
        return list_of_integers[0]
    elif size == 2:
        return max(list_of_integers)
    left = 0
    r = size - 1
    m = int((left + r) / 2)
    while left <= r:
        p = list_of_integers[m]
        if (
                (m == 0 or peak >= list_of_integers[m - 1]) and
                (m == r or p >= list_of_integers[m + 1])):
            break
        elif p < list_of_integers[m - 1]:
            r = m - 1
            m = int((left + r) / 2)
        else:
            left = m + 1
            m = int((left + r) / 2)
    return p
