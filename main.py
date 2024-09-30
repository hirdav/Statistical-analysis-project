import numpy as np
import matplotlib.pyplot as plt

# Generating random data (1000 points from a normal distribution)
data = np.random.normal(loc=50, scale=10, size=1000)

# Calculating mean and standard deviation
mean = np.mean(data)
std_dev = np.std(data)

# Printing results
print(f"Mean: {mean}, Standard Deviation: {std_dev}")

# Ploting histogram
plt.hist(data, bins=30, color='skyblue', edgecolor='black')
plt.title('Histogram of Random Data')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.show()
