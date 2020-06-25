# Un box_plot o grafico de caja es un metodo para mostrar de una forma concisa varias muestras de datos.
# La informacion contenida en el box_plot es: la mediana, el valor minimo, el valor maximo y los rangos intercuartiles.

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

#Como ejemplo creemos 3 muestras diferentes, cada una con una distribucion distinta: normal, uniforma y gamma.
normal_sample = np.random.normal(loc=0.0, scale=1.0, size=10000)
random_sample = np.random.random(size=10000)
gamma_sample = np.random.gamma(2, size=10000)

#guardamos todo en un df
df = pd.DataFrame({'normal': normal_sample,
                   'random': random_sample,
                   'gamma': gamma_sample})

#Podemos usar la funcion describe para ver alguos datos estadisticos de la muestras
print(df.describe())
plt.figure()
# create a boxplot of the normal data, assign the output to a variable to supress output
_ = plt.boxplot(df['normal'], whis='range') #Simplemente proyectamos la columna que queremos visualizar. Con la opcion whis le decimos el rango de datos que queremos considerar. Ademas vamos a pasar la informacion del grafico a la variable _
plt.savefig('box_plot.pdf')
#Agraguemos los otros 2 samples
plt.clf() #Limpiamos la figura actual
_ = plt.boxplot([ df['normal'], df['random'], df['gamma'] ], whis='range') #Proyectamos cada columna
plt.savefig('box_plot2.pdf')
#Inmediatamente nos damos cuenta que la distribucion gamma tiene una cola muy larga. Veamos cmo se ve esta distribucion en in histograma
plt.figure()
_ = plt.hist(df['gamma'], bins=100)
plt.savefig('gamma_distribution_histogram.pdf')

#Podemos insertar este histograma dentro del box_plot usando:
import mpl_toolkits.axes_grid1.inset_locator as mpl_il

plt.figure() #creamos la figura
plt.boxplot([ df['normal'], df['random'], df['gamma'] ], whis='range') #creamos el boxplot
# overlay axis on top of another
ax2 = mpl_il.inset_axes(plt.gca(), width='60%', height='40%', loc=2) #pasamos el objeto que queremos traslapar seguido por el tamaño de este. POdemos usar el porcentaje que queremos que tenga en relacion al tamaño original del boxplot
ax2.hist(df['gamma'], bins=100) #le decimos que graficos queremos hacer
ax2.margins(x=0.5) #fijamos el margen con respecto al plot original
ax2.yaxis.tick_right() # cambiamos la etiqueta del eje y hacia el lado derecho.
plt.savefig('2_graficos_en_1.pdf')
