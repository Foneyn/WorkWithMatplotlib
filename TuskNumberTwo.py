import numpy as np
import matplotlib.pyplot as plt

num_samples = 100
data_x = np.random.rand(num_samples)
data_y = np.random.rand(num_samples)

plt.scatter(data_x, data_y, alpha=0.7, edgecolor='r')
plt.title('Диаграмма рассеяния случайных данных')
plt.xlabel('X')
plt.ylabel('Y')

plt.show()