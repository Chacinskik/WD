import numpy as np
import matplotlib.pyplot as plt


def rzut2k6(n):
    wyniki = []
    for i in range(n):
        a = np.random.randint(1, 7)
        b = np.random.randint(1, 7)
        c = a + b
        wyniki.append(c)
    return wyniki


plt.hist(rzut2k6(10000), facecolor='g', alpha=0.75, density=True)

plt.xlabel('Wartości')
plt.ylabel('Prawdopodobieństwo')
plt.title('Histogram')
plt.grid(True)
plt.show()