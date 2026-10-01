import matplotlib.pyplot as plt
import numpy as np

x = np.random.rand(100)
y = x + np.random.rand(100) * 0.5

plt.scatter(x, y)
plt.title('Scatter Plot')
plt.xlabel('X values')
plt.ylabel('Y values')
plt.savefig('scatter.png')
plt.show()