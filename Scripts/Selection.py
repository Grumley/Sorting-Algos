"""
Selection sort finds the minimum value in a list then swaps it with the number in the first position.
It moves along the list swapping each next largest number into it's respective position.
"""
from dataset import random_list

unsorted_list = random_list(0, 100)

for i in range(len(unsorted_list) - 1):
    minimum_index = i
    for j in range(i + 1, len(unsorted_list)):
        if unsorted_list[j] < unsorted_list[minimum_index]:
            minimum_index = j
    unsorted_list[i], unsorted_list[minimum_index] = unsorted_list[minimum_index], unsorted_list[i]

print(unsorted_list)
