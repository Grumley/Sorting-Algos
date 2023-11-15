"""
Steps through the input list element by element, comparing the current element with the one after it,
swapping their values if needed.
Average with 0-500: 0.073 seconds
"""
from dataset import random_list

changed_list = True
unsorted_list = random_list(0, 500)

while changed_list:
    changed_list = False
    for i in range(len(unsorted_list) - 1):
        if unsorted_list[i] > unsorted_list[i + 1]:
            unsorted_list[i], unsorted_list[i + 1] = unsorted_list[i + 1], unsorted_list[i]
            changed_list = True
        elif not changed_list and i == len(unsorted_list) - 2:
            break
