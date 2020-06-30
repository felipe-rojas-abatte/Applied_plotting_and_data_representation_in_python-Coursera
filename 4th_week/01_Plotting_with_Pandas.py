#Pandas usa matplotlib bajo la manga por lo que podemos conectar facilmente las librerias de pandas con las visualizaciones de matplotlib

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Usando este comando podemos ver los estilos que estan disponibles en matplotlib
#Esto ayudara a que la apariencia de los graficos cambie de acuerdo a nuestros requerimientos
print(plt.style.available)

#Usemos uno de estos estilos
plt.style.use('seaborn-colorblind')

#Creemos un dataframe
np.random.seed(123)
df = pd.DataFrame({'A': np.random.randn(365).cumsum(0),
                   'B': np.random.randn(365).cumsum(0) + 20,
                   'C': np.random.randn(365).cumsum(0) - 20},
                  index=pd.date_range('1/1/2017', periods=365)) #podemos dejar como indice la fecha de toto un año
print(df.head())

#Una forma rápida de graficar esto es usando el comando
df.plot()
plt.savefig('first_pandas_plot.pdf')
#Podemos cambiar el tipo de gráfico usando la opcion kind. Por ejemplo
df.plot('A','B', kind = 'scatter')
plt.savefig('scatter_pandas_plot.pdf')

#Creemos algo mas elaborado
#Hagamos un scatter plot con puntos que varien en tamaño
df.plot.scatter('A','C', c='B', s=df['B'], colormap='viridis' )
plt.savefig('scatter_pandas_plot2.pdf')
#Dado que df.plot.scatter devuelve un objeto tipo matplotlib.axes._subplot, podemos aplicar modificaciones a este objeto al igual que usando matplotlib
ax = df.plot.scatter('A', 'C', c='B', s=df['B'], colormap='viridis')
ax.set_aspect('equal') #esto permite ver que el rango de la serie A es mas pqeueño que el rango de la serie C
plt.savefig('scatter_pandas_plot3.pdf')

#Con pandas es fácil hacer graficos de barras, histogramas y kernel estimate plots.
df.plot.box()
plt.savefig('box_pandas_plot.pdf')
df.plot.hist(alpha=0.7);
plt.savefig('histogram_pandas_plot.pdf')
#Kernel density estimation plots, son utiles para derivar una funcion continua suave desde una sample.
df.plot.kde();
plt.savefig('kde_pandas_plot.pdf')

#Pandas tambien tiene otro set de herramientas de visualizacion para ayudar a entender garndes cantidades de datos
iris = pd.read_csv('iris.csv')
print(iris.head())
#Pandas tiene una herramienta para crear una scatter matrix. Esto es una forma de comparar cada columna del DF con cada una de las otras columnas formando parejas
# La scatter matrix crea scatter plots entre las diferentes variables y tambien crea historamas a lo largo de las diagonales
pd.tools.plotting.scatter_matrix(iris);
plt.savefig('scatter_matrix.pdf')

#Pandas tambien incluye una herramienta para crear graficos de coordenadas paralelas. Esta es una forma eficiente de visualizar datos multidimensionales.
plt.figure()
pd.tools.plotting.parallel_coordinates(iris, 'Name');
