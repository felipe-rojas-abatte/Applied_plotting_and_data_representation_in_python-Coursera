#Cosas para recordar:
#a) pyplot va a recuperar la figura actual con la funcion gcf y luego obtiene los ejes actuales con la funcion gca.
#b) pyplot solo imita el API del objeto axis. Tu puedes llamar la funcion plot contra el modulo pyplot.
#c) la declaracion de funciones en matplotlib termina con un conjunto de argumentos.

## Scatter plot (grafico de puntos).
# Grafico en 2 dimensiones

import matplotlib.pyplot as plt
import numpy as np

x = np.array([1,2,3,4,5,6,7,8])
y = x
plt.figure()
plt.scatter(x,y)
plt.savefig('scatter_plot.pdf')

## Creemos una lista con puntos de color verte y hagamos que el último punto sea de color rojo.
x = np.array([1,2,3,4,5,6,7,8])
y = x
colors = ['green']*(len(x)-1)
colors.append('red')
plt.figure()
#   funcion x, y , tamaño puntos, colores
plt.scatter(x,y, s=100, c=colors)
plt.savefig('scatter_plot2.pdf')

## metodo zip: toma un numero de iterables y crea una tupla como salida, pareando elementos basados en el index.
#              por lo tanto si tenemos 2 listas de numeros, zip tomara el primero de cada lista y creará una tupla, luego el segundo de cada lista y creara otra tupla, etc.
# ejemplo
zip_generator = zip([1,2,3,4,5], [6,7,8,9,10])
print(list(zip_generator))

## Otra opcion es pasar a una variable x e y las lista por separado. Para eso usamos la funcion zip, pero de la siguiente forma
zip_generator = zip([1,2,3,4,5], [6,7,8,9,10])
x,y = zip(*zip_generator)
print(x)
print(y)

##Ahora tomemos estas 2 listas y usemoslas para graficar un scatter plot
plt.figure()
plt.scatter(x[:2], y[:2], s=100, c='red', label='Tall student')
plt.scatter(x[2:], y[2:], s=100, c='blue', label='Short student')
plt.xlabel('The number of times the child kicked a ball')
plt.ylabel('The grade of the student')
plt.title('Relationship between ball kicking and grades')
plt.legend(loc=4, frameon=False, title='Legend') #loc: posicion en el plot. frameon=Encerramos o no en un cuadro. title:Titulo
plt.savefig('scatter_plot3.pdf')

## La leyenda en si misma es un artist, por lo que puede contener childrens. Creemos una rutina que que recursivamente vaya a traves de la losta de childrens en un artist
child = plt.gca().get_children()
for c in child:
    print(c)
# La leyenda esta en el penultimo espacio de la lista.
legend = plt.gca().get_children()[-2]
print(legend.get_children()[0].get_children()[1].get_children()[0].get_children())
#Verificamos si el objeto es un artista. Si lo es, imprimimos el nombre
from matplotlib.artist import Artist
def rec_gc(art, depth=0):
    if isinstance(art, Artist):
        # increase the depth for pretty printing
        print("  " * depth + str(art))
        for child in art.get_children():
            rec_gc(child, depth+2)
rec_gc(legend)
