#Heatmap es una forma de visualizar datos tridimensionales
import matplotlib.pyplot as plt
import numpy as np

plt.figure()
Y = np.random.normal(loc=0.0, scale=1.0, size=10000)
X = np.random.random(size=10000)
_ = plt.hist2d(X, Y, bins=25)
plt.colorbar() # add a colorbar legend
plt.savefig('Heatmap.pdf')

#Que ocurre cuando cambiamos el numero de bins
plt.figure()
_ = plt.hist2d(X, Y, bins=100)
plt.savefig('Heatmap2.pdf')
