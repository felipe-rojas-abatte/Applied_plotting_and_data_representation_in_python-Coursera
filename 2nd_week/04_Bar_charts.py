# matplotlib soporta graficos de barras. Para el caso mas simple indicamos el rango para el eje x y la altura de cada componente.
import numpy as np
import matplotlib.pyplot as plt

linear_data = np.array([1,2,3,4,5,6,7,8])
quadratic_data = linear_data**2

plt.figure()
xvals = range(len(linear_data)) #
plt.bar(xvals, linear_data, width = 0.3)
#plt.savefig('bar_plot1.pdf')

##Podemos agragar una segunda tanda de barras de otro color
new_xvals = []
for item in xvals:
    new_xvals.append(item+0.3) #corremos el segundo set de barras 0.3 hacia la derecha

plt.bar(new_xvals, quadratic_data, width = 0.3, color='r')
#plt.savefig('bar_plot1.pdf')

##Podemos agragar error al grafico con la opcion yerr.
from random import randint
linear_err = [randint(0,15) for x in range(len(linear_data))]
plt.bar(xvals, linear_data, width=0.3, yerr=linear_err)
plt.savefig('bar_plot1.pdf')

##Podemos ademas hacer que ambas columnas esten usna sobre la otra, mostrando la menor por encima
plt.figure()
xvals = range(len(linear_data)) #
plt.bar(xvals, linear_data, width = 0.3, color='b')
plt.bar(xvals, quadratic_data, width = 0.3, bottom=linear_data, color='r')
plt.savefig('bar_plot2.pdf')

## Finalmente podemos hacer un gŕafico horizontal de barras, pero ahora cambiamos bar por barh, el width a height, y el bottom a left
plt.figure()
xvals = range(len(linear_data)) #
plt.barh(xvals, linear_data, height=0.3, color='b')
plt.barh(xvals, quadratic_data, height = 0.3, left=linear_data, color='r')
plt.savefig('barh_plot3.pdf')
