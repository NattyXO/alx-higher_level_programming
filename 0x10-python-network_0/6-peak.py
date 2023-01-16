#!/usr/bin/python3
""" Finds a peak inside a list """


def find_peak(list_of_integers):
    """
    Finds a peak in a list of unsorted integers using divide and conquer approach.
    Complexity: O(log(n))
    """
    if not list_of_integers:
        return None
    elif len(list_of_integers) == 1:
        return list_of_integers[0]
    elif len(list_of_integers) == 2:
        return max(list_of_integers)
    else:
        mid = len(list_of_integers) // 2
        if list_of_integers[mid] > list_of_integers[mid - 1] and list_of_integers[mid] > list_of_integers[mid + 1]:
            return list_of_integers[mid]
        elif list_of_integers[mid] < list_of_integers[mid - 1]:
            return find_peak(list_of_integers[:mid])
        else:
            return find_peak(list_of_integers[mid+1:])
