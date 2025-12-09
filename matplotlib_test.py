import matplotlib.pyplot as plt
import numpy as np

Years = np.array([2020, 2021, 2022, 2023, 2024, 2025])
Events = np.array([20, 23, 56, 2000, 199, 208])

plt.plot(Years, Events)
plt.show()