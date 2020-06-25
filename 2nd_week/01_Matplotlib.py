import matplotlib as mpl
print(mpl.get_backend()) #imprime TkAgg

## in python axis y axes son objetos distintos
# axis: ejes de un plano
# axes: objeto compuesto por 2 axis, uno para el eje x y otro para el eje y


## Matplotlib Architecture
#Contiene 3 capas
# a) Backend layer: es una capa abstracta la cual matplotlib conoce como interactuas con el entorno, dependiendo si es un sistema operativo, o un buscador.
# b) Artist layer: trabaja sobre Backend. Describe primitives, collections y contenedores. Sabe como las figuras estan compuestas de subfiguras y donde los objetos estan dadas los ejes de coordenadas.
# c) Scripting layer: Simplifica el acceso a las capas anteriores.

#matplotlib es un ejemplo de método de visualización de información procesal
#java script es un ejemplo de método de visualización de información declarativa

import matplotlib.pyplot as plt
# grafica un punto en la posicion 3,2
plt.plot(3,2,'.')
plt.savefig('first_plot.pdf')

## Otra forma de graficar
from matplotlib.backends.backend_agg import FigureCanvasAgg
from matplotlib.figure import Figure
fig = Figure()
canvas = FigureCanvasAgg(fig)

ax = fig.add_subplot(111)
ax.plot(3,2,'.')
canvas.print_png('test.png')

## creamos una nueva figuras
plt.figure()
plt.plot(3,2,'o')
ax = plt.gca() #gca: get current axes
print(ax.axis([0,6,0,10])) # definimos el rango de los ejes del plot
plt.savefig('second_plot.pdf')

## creamos una nueva figuras
plt.figure()
plt.plot(1.5,1.5,'o')
plt.plot(2,2,'o')
plt.plot(2.5,2.5,'o')
plt.savefig('third_plot.pdf') # hace 3 puntos en el grafico con distintos colores, ya que los reconoce como distintos grupos de datos
## Podemos obtener todos los objetos hijos que contiene el el axes
ax = plt.gca()
print(ax.get_children())
# Lo que vemos en la salida es que tenemos:
# 3 objetos Line2D que corresponden a los 3 puntos del grafico
# 4 objetos spine que corresponden a los 4 margenes del plot
# 2 objetos axis que son los 2 ejes del plot
# text corresponden a las etiquetas.
