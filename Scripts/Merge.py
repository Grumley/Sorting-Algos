"""
Merge sort uses a divide and conquer rule:
    1. Divide the unsorted array into subarray, each containing a single element.
    2. Take adjacent pairs of two single-element array and merge them to form an array of 2 elements.
    3. Repeat the process till a single sorted array is obtained.
"""
# Incomplete

from dataset import random_list

changed_list = True
minimum, maximum = 0, 100
unsorted_list = random_list(minimum, maximum)
sub_lists = []

for i in range(len(unsorted_list)):
    sub_lists.append([unsorted_list[i]])

# TODO Workout how handle odd number of values
mid_point = len(sub_lists)//2

print(sub_lists)
for i in range(minimum, mid_point):
    if sub_lists[i][0] > sub_lists[i+1][0]:
        sub_lists[i] = [sub_lists[i+1][0], sub_lists[i][0]]
    else:
        sub_lists[i] = [sub_lists[i][0], sub_lists[i+1][0]]
    sub_lists.pop(i+1)

# for i in range(minimum, len(sub_lists)//4):
#     if sub_lists[i][0] > sub_lists[i+1][0]:
#         sub_lists[i] = [sub_lists[i+1][0], sub_lists[i][0]]
#     else:
#         sub_lists[i] = [sub_lists[i][0], sub_lists[i+1][0]]
#     sub_lists.pop(i+1)

# TODO Workout how to improve and condense the loop for any size array

print(sub_lists)
