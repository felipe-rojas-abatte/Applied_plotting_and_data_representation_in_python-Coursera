#Un line plot es un scater plot donde cada punto esta unido por una línea recta
## Ejemplo:
#Creemos 2 listas en donde los valres crecen lineal y cuadraticamente
import numpy as np
import matplotlib.pyplot as plt

linear_data = np.array([1,2,3,4,5,6,7,8])
quadratic_data = linear_data**2
plt.figure()
plt.plot(linear_data, '-o', quadratic_data, '-o')
plt.plot([22,44,55], '--r')
plt.xlabel('Some data')
plt.ylabel('Some other data')
plt.title('A title')
plt.legend(['Baseline','Competition','Us'])
#plt.savefig('Linear_plot.pdf')
#En un linear plot podemos solo dar como input la lista de valores correspondientes al eje y
#Tambien linear plor reconoce que hay 2 series de datos, asignandoles un color diferente a cada lista.
#Existen marcadores para las líneas que podemos usar de manera rápida como '--r' para lineas segmentadas
#Tambien podemos nombrar los ejes y poner titulos. La diferencia radica en como etiquetamos la leyenda, ya que en vez de poner nombre en cada lista de datos, creamos una lista con los nombres de cada linea

## Una funcion muy usada es la fill_between que llena de color una zona entre 2 lineas.
# primero definimos el rango entre que valores del eje x vamos a llenar, luego definimos entre que valores del eje y, finalmente escogemos el color y la transparencia.
plt.gca().fill_between(range(len(linear_data)),linear_data, quadratic_data,facecolor='b', alpha=0.25 )
plt.savefig('Linear_plot.pdf')

## Creemos una nueva figura
plt.figure()
observation_dates = np.arange('2017-01-01', '2017-01-09', dtype='datetime64[D]')
#grafiquemos esta nueva lista contra los datos lineales
plt.plot(observation_dates, linear_data, '-o', observation_dates, quadratic_data, '-o')
#Lo que vemos es igual al plot 1. Tenemos que saber manejar los datos en forma de fecha. Para tranajar con fechas vamos a usar una libreria de pandas que convierte fechas en datos para poder graficarlos mejor.

import pandas as pd
observation_dates = np.arange('2017-01-01', '2017-01-09', dtype='datetime64[D]')
#Usemos la funcion map(): toma una función y una lista y aplica esa función a cada elemento de esa lista, produciendo una nueva lista.
observation_dates = map(pd.to_datetime, observation_dates)
print(observation_dates) #con esto observation_dates es ahora un map objets, pero nosotros queremos que sea una lista.
observation_dates = list(observation_dates)
print(observation_dates) # Ahora si es una lista
plt.plot(observation_dates, linear_data, '-o', observation_dates, quadratic_data, '-o')
#plt.savefig('Linear_plot2.pdf')
#En este caso las fechas estan traslapadas unas con otras. Podemos rotarlas 45° para poer ver todo el contenido
x = plt.gca().xaxis
for item in x.get_ticklabels():
    item.set_rotation(45)
#plt.savefig('Linear_plot2.pdf')
#Ahora los nombres de las fechas estan fuera de los margenes. Podemos ajustar los margenes con la funcion
plt.subplots_adjust(bottom=0.25)
#plt.savefig('Linear_plot2.pdf')

##matplotlib esta directamente conectado con librerias de latex, asi que podemos escribir ecuaciones y estas apareceran en el grafico.
ax=plt.gca()
ax.set_xlabel('Date')
ax.set_ylabel('Unit')
ax.set_title('Quadratic ($x^2$) vs. Linear ($x$) performance')
plt.savefig('Linear_plot2.pdf')
