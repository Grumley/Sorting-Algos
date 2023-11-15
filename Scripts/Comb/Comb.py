"""
The comb sort is an improvement on bubble sort. It introduces a gap between the comparison points that reduces
every iteration. This helps move small points that could take several more iterations in bubble sort to get
into the correct position sooner.
Average with 0-500: 0.01024 seconds
"""
import time
from math import pow
from statistics import mean
from dataset import random_list

times_list = []
for _ in range(500):
    start_time = time.time()
    power = 1
    changed_list = True
    shrink_factor = 1.24733
    unsorted_list = random_list(0, 500)
    pointer_two = int(len(unsorted_list) // pow(shrink_factor, power))

    while changed_list:
        changed_list = False
        pointer_one = 0
        pointer_two = max(1, int(pointer_two // pow(shrink_factor, power)))
        power += 0.25
        for i in range(pointer_two, len(unsorted_list)):
            if unsorted_list[pointer_one] > unsorted_list[i]:
                unsorted_list[pointer_one], unsorted_list[i] = unsorted_list[i], unsorted_list[pointer_one]
                changed_list = True
            pointer_one += 1

    end_time = time.time()  # Record the end time
    elapsed_time = end_time - start_time  # Calculate elapsed time

    times_list.append(elapsed_time)

print(f"Elapsed Time: {mean(times_list):.6f} seconds")
