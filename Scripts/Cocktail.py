"""
A cocktail sort is very similar to a Bubble sort, but it sorts backwards and forwards, instead of just forwards.
"""
from dataset import random_list

changed_list = True
unsorted_list = random_list(0, 1000)

while changed_list:
    changed_list = False
    for i in range(len(unsorted_list) - 1):
        if unsorted_list[i] > unsorted_list[i + 1]:
            unsorted_list[i], unsorted_list[i + 1] = unsorted_list[i + 1], unsorted_list[i]
            changed_list = True
        elif not changed_list and i == len(unsorted_list) - 2:
            break
    for i in range(len(unsorted_list) - 1, 0, -1):
        if unsorted_list[i] < unsorted_list[i - 1]:
            unsorted_list[i], unsorted_list[i - 1] = unsorted_list[i - 1], unsorted_list[i]
            changed_list = True
        elif not changed_list and i == 1:
            break

print(unsorted_list)
