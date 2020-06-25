# Un histograma es un grafico de barras que muestra la frecuencia de un determinado fenomeno.
# Creemos una gris de 2x2 con figuras
import matplotlib.pyplot as plt
import numpy as np

fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, sharex=True)
axs = [ax1,ax2,ax3,ax4]

for n in range(0,len(axs)):
    sample_size = 10**(n+1) #en cada plot consideraremos un mayor numero de datos
    sample = np.random.normal(loc=0.0, scale=1.0, size=sample_size)
    axs[n].hist(sample)
    axs[n].set_title('n={}'.format(sample_size))
plt.savefig('grid_histograms.pdf')
#plt.show()

#Lo primero que podemos notar es que a medida que incrementamos el numero de samples el histograma muestra de manera mas clara el tipo de distribución que es (normal centrada en 0 co desviación estandard 1).
#También podemos notar que el ancho de las barras a medida que incrementamos n. Por dejecto el histograma muestra una figura con 10 bins. Por lo que para el histograma con n=10000 hay muchos datos en cada bin.
# Cambiemos ahora el numero de bins a 100 para ver que ocurre.

fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, sharex=True)
axs = [ax1,ax2,ax3,ax4]

for n in range(0,len(axs)):
    sample_size = 10**(n+1) #en cada plot consideraremos un mayor numero de datos
    sample = np.random.normal(loc=0.0, scale=1.0, size=sample_size)
    axs[n].hist(sample, bins=100)
    axs[n].set_title('n={}'.format(sample_size))
plt.savefig('grid_histograms2.pdf')
#plt.show()
# Aca nos muestra que el histograma con n=10000 datos es mucho mas suave que el resto, sin embargo el histograma con n=10, cada dato es su propio bin. Esto nos lleva a la siguiente pregunta.
# ¿Cuantos bins son apropiados para un histograma?. No hay una respuesta correcta para esta pregunta. Solo que en algunos casos el histograma se vuelve inutil, a pesar de mostrar los mismos datos.

##Existe una forma mas flexible de diseñar los histogramas. Esto es usando el GridSpec.
# Esto te permite mapear ejex sobre multiples celdas en una grid.
#Por ejemplo: creemos un scatter plot donde los valores del eje y son creados con una distribucion normal y los valores del eje x provienen de una distribucion uniforme.
plt.figure()
Y = np.random.normal(loc=0.0, scale=1.0, size=10000)
X = np.random.random(size=10000)
plt.scatter(X,Y)
plt.savefig('scatter_plot.pdf')
#Al observar el grafico no podemos distinguir exactamente cual eje es una distribucion normal o no.
#Para ver mejor esto haremos una grid de 3x3 donde: el primer histograma ocupara el espacio superior derecho y el 2do histograma que ocupe el lugar inferior izquierdo. El scatter plot original ocupara una matrix de 2x2 abajo a la derecha.
import matplotlib.gridspec as gridspec
plt.figure()
gspec = gridspec.GridSpec(3, 3) # le decimos que matrix debe cubrir 3x3

top_histogram = plt.subplot(gspec[0, 1:3]) #Fila 0, columna desde la 1 hasta la 2
side_histogram = plt.subplot(gspec[1:3, 0]) #Fila 1 hasta 2, columna 0
lower_right = plt.subplot(gspec[1:3, 1:3]) # Fila 1 hasta 2 , columna 1 hasta 2
#Ahora tenemos que llenar esto con los datos
Y = np.random.normal(loc=0.0, scale=1.0, size=10000)
X = np.random.random(size=10000)
lower_right.scatter(X, Y)
top_histogram.hist(X, bins=100)
s = side_histogram.hist(Y, bins=100, orientation='horizontal') #rotamos el histograma vertical
plt.savefig('scatter_plot_gridspec.pdf')
#Ahora vamos a limpiar un poco el histograma. Dado que no nos interasa saber los valores absolutos del eje y en el histograma superior, ni los valores absolutos del eje x del histograma de la izquierda, solo queremos conocer los valores relativos (normalizados a 1. La probabilidad). Vamos a limpiar esto.
top_histogram.clear() # con la funcion clear limpiamos el marco
top_histogram.hist(X, bins=100, normed=True) #Con la funcion norm=True, normalizamos
side_histogram.clear()
side_histogram.hist(Y, bins=100, orientation='horizontal', normed=True)
side_histogram.invert_xaxis() # con esto invertimos la orientacion del histograma lateral
plt.savefig('scatter_plot_gridspec2.pdf')
#Finalmente podemos cambiar los limites de los ejes
# change axes limits
for ax in [top_histogram, lower_right]:
    ax.set_xlim(0, 1)
for ax in [side_histogram, lower_right]:
    ax.set_ylim(-5, 5)
plt.savefig('scatter_plot_gridspec3.pdf')
