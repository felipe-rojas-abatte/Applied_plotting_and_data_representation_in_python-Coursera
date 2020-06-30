##Seaborn es una herramienta de visualizacion que ayuda a mejorar la apariencia de los graficos
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
plt.style.use('seaborn-colorblind')

#Creemos 2 series con 1000 datos basados en una distribucion normal donde la serie v1 tiene media 0 y std 10 y la segunda setrie es una construccion de 2 veces v1 + otra distribucion normal con media 60 y std 15
np.random.seed(1234)
v1 = pd.Series(np.random.normal(0,10,1000), name='v1')
v2 = pd.Series(2*v1 + np.random.normal(60,15,1000), name='v2')
#Grafiquemos estas 2 Series
plt.figure()
plt.hist(v1, alpha=0.7, bins=np.arange(-50,150,5), label='v1')
plt.hist(v2, alpha=0.7, bins=np.arange(-50,150,5), label='v2')
plt.legend()
plt.savefig('Histograms_series.pdf')

#Visualicemos estos histogramas en una forma distinta.
plt.figure()
#primero pasemos las dos series a una lista y usemos la opcion histtype=barra apilada (barstacked). Tambien normalizamos los histogramas para formar una densidad de probabilidad.
plt.hist([v1, v2], histtype='barstacked', density=True)
#creamos una variable v3 que es una combinacin de v1 y v2
v3 = np.concatenate((v1,v2))
#usamos v3 para graficar un kernel density estimate plot sobre los 2 histogramas anteriores.
sns.kdeplot(v3)
#la funcion kdeplot estima la densidad de probabilidad de v3
plt.savefig('Histograms_series2.pdf')

# podemos cambiar e color de cada histograma para que quede todo de 1 solo color
plt.figure()
sns.distplot(v3, hist_kws={'color': 'Teal'}, kde_kws={'color': 'Navy'})
plt.savefig('Histograms_series3.pdf')

# Otro tipo de plots son los join plots
# El joinplot crea un scatter plot en el centro y por cada variable del scatter plot crea un histograma.
sns.jointplot(v1, v2, alpha=0.4);
plt.savefig('Join_plot.pdf')

#Como seaborn usa matplotlib como base, podemos usar las mismas herramientas de matplotlib para modificar los graficos
grid = sns.jointplot(v1, v2, alpha=0.4);
grid.ax_joint.set_aspect('equal')

#Podemos crear un jpinplot pero dejando hexagonos en ves de puntos para el scatter plot. Para eso usamos el flag=hex
sns.jointplot(v1, v2, kind='hex');
plt.savefig('Join_plot_hex.pdf')

# Tambien podemos usar kde plots con el flag=kde
sns.set_style('white')# primero cambiamos el estilo
sns.jointplot(v1, v2, kind='kde', space=0);
plt.savefig('Join_plot_kde.pdf')

#Usemos nuevamente el cvs iris
iris = pd.read_csv('iris.csv')
print(iris.head())

#Seaborn tambien tiene una funcion para crear un scatter matrix plot
#sns.pairplot(iris, hue='Name', diag_kind='kde', size=2);
#plt.savefig('Scatter_matrix_seaborn.pdf')

#Swarm and Violin plot
plt.figure(figsize=(8,6))
plt.subplot(121)
sns.swarmplot('Name', 'PetalLength', data=iris);
plt.subplot(122)
sns.violinplot('Name', 'PetalLength', data=iris);
