import matplotlib.pyplot as plt
import numpy as np

# 100,000 random values from a normal (bell curve) distribution
data = np.random.randn(100_000)

plt.hist(data, bins=50, color='red', edgecolor='black')
plt.title('Histogram')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.show()