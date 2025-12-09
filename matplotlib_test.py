import matplotlib.pyplot as plt
import numpy as np

Years = np.array([2020, 2021, 2022, 2023, 2024, 2025])
Events1 = np.array([20, 23, 56, 2000, 199, 208])
Events2 = np.array([32, 56, 84, 1000, 12, 64])
Events3 = np.array([12, 11, 54, 234, 121, 19])
Lines_styles = dict(marker=".", 
                    markersize=20,
                    markerfacecolor="#ccc",
                    markeredgecolor="#F00",
                    linestyle="solid",
                    linewidth=4,
                    color="#ccc"
                    )

plt.plot(Years, Events1, **Lines_styles)
plt.plot(Years, Events2, **Lines_styles)
plt.plot(Years, Events3, **Lines_styles)
plt.show()