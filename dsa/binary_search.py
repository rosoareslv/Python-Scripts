import random
import math


# Complexidade
# Temporal - O(log N)
# Espacial - O(1)
# A lista precisa estar ordenada
def binary_search(arr: list, target: int, start=0, end=None):
    """ "
    Binary search algorithm - O(log n) coplexity
    """
    steps = 0
    if end == None:
        end = len(arr) - 1
    while start <= end:
        steps += 1
        index = (end + start) // 2
        if arr[index] == target:
            print(f"Needed {steps} steps to find!")
            return index
        if arr[index] > target:
            end = index - 1
        else:
            start = index + 1
    return -1
