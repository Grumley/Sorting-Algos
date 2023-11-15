"""
Bogo Sort uses random shuffling. Used for example purposes only, as even the expected best-case runtime is awful
Average: n * n!
"""
from random import shuffle
from dataset import random_list

list_sorted = False
unsorted_list = random_list(0, 9)

while not list_sorted:
    shuffle(unsorted_list)
    for i in range(len(unsorted_list) - 1):
        if unsorted_list[i] > unsorted_list[i + 1]:
            break
        elif i == len(unsorted_list) - 2:
            list_sorted = True

print(unsorted_list)
