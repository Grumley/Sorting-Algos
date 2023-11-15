import random
import time
import pandas as pd
from math import pow
from statistics import mean
from dataset import random_list
from matplotlib import pyplot as plt

data = []

for _ in range(500):
    power = random.uniform(0.1, 1.2)
    shrink_factor = random.uniform(1.0, 1.5)
    list_length = random.randint(100, 2000)
    times_list = []

    for _ in range(200):
        unsorted_list = random_list(0, list_length)
        pointer_two = int(len(unsorted_list) // pow(shrink_factor, power))
        start_time = time.time()
        swapped = True

        while swapped:
            swapped = False
            pointer_one = 0
            pointer_two = max(1, int(pointer_two // pow(shrink_factor, power)))

            for i in range(pointer_two, len(unsorted_list)):
                if unsorted_list[pointer_one] > unsorted_list[i]:
                    unsorted_list[pointer_one], unsorted_list[i] = (unsorted_list[i], unsorted_list[pointer_one])
                    swapped = True
                pointer_one += 1

        end_time = time.time()
        elapsed_time = end_time - start_time
        times_list.append(elapsed_time)

    print(power, shrink_factor, maximum, mean(times_list))
    data.append({
        'list length': maximum,
        'power': power,
        'shrink factor': shrink_factor,
        'average time (s)': mean(times_list)
    })


# Save df to CSV
df = pd.DataFrame(data, columns=['list length', 'power', 'shrink factor', 'average time (s)'])
df.to_csv(path_or_buf='Comb.csv', index=False)

# Create a 3D scatter plot
fig = plt.figure(figsize=(12, 10))
ax = fig.add_subplot(111, projection='3d')
sc = ax.scatter(df['power'],
                df['shrink factor'],
                df['average time (s)'],
                c=df['list length'],
                cmap='viridis',
                marker='o')

# Set labels for each axis
ax.set_xlabel('Power')
ax.set_ylabel('Shrink Factor')
ax.set_zlabel('Average Time (s)')

# Set title for the plot
plt.title('3D Scatter Plot with Power, Shrink Factor, Maximum, and Average Time')

# Add colour bar to show the mapping of average time to color
cbar = fig.colorbar(sc)
cbar.set_label('Maximum')

plt.show()
