import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm


df = pd.read_csv('Comb.csv')

df = df[df['average time (s)'] <= 0.15]

# # Create a 3D scatter plot
# fig = plt.figure(figsize=(12, 10))
# ax = fig.add_subplot(111, projection='3d')
# sc = ax.scatter(df['power'],
#                 df['shrink factor'],
#                 df['average time (s)'],
#                 c=df['list length'],
#                 cmap='viridis',
#                 marker='o')
#
# # Set labels for each axis
# ax.set_xlabel('Power')
# ax.set_ylabel('Shrink Factor')
# ax.set_zlabel('Average Time (s)')
#
# # Set title for the plot
# plt.title('3D Scatter Plot with Power, Shrink Factor, Maximum, and Average Time')
#
# # Add color bar to show the mapping of average time to color
# cbar = fig.colorbar(sc)
# cbar.set_label('Maximum')
#
# plt.show()

# Simple Linear Regression for each variable
for col in ["list length", "power", "shrink factor"]:
    X = sm.add_constant(df[col])
    model = sm.OLS(df["average time (s)"], X).fit()
    print(f"\n{col} vs. average_time:")
    print(model.summary())
