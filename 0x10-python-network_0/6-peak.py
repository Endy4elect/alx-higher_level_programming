#!/usr/bin/python3
def find_peak(list_of_integers):
    """
    Finds a peak in a list of unsorted integers using a binary search algorithm.
    Returns the peak value.
    """
    n = len(list_of_integers)
    if n == 0:
        return None
    elif n == 1:
        return list_of_integers[0]
    elif n == 2:
        return max(list_of_integers)
    else:
        left = 0
        right = n - 1
        while left < right:
            mid = (left + right) // 2
            if list_of_integers[mid] < list_of_integers[mid + 1]:
                left = mid + 1
            else:
                right = mid
        return list_of_integers[left]
