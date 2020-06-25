# Hasta ahora hemos visto como construir gráficos simples. Si quisieramos incluir varios graficos en una misma figura, podemos hacerlo con subplot
import matplotlib.pyplot as plt
import numpy as np

#Si vemos la documentacion de subplots vermos que el 1er argumento es el numero de filas, el 2do es el numero de columnas y el 3ro es el numero de plots.
## Ejemplo
plt.figure()
plt.subplot(1,2,1) # 1 fila, 2 columnas, donde queremos el primer plot.
linear_data = np.array([1,2,3,4,5,6,7,8])
plt.plot(linear_data, '-o') #creamos un plot angosto al lado izquierdo del marco
#plt.show()
#crearemos un segundo subplot con el 3er parametro = 2 para que quede a la derecha
exponential_data = linear_data**2
plt.subplot(1,2,2)
plt.plot(exponential_data, '-o')
#plt.show()
#Tambien podemos poner dentro del plot lineal los datos exponenciales cambiando el 3r numero del subplot
plt.subplot(1,2,1)
plt.plot(exponential_data, '-x')
#plt.show()
#antes de graficar los datos exponenciales en el mismo plot de los datos lineales, pareciera que ambos generan la misma area bajo la curva. A nemos que nos percatemos de los valores del eje y podemos generar confusión a la hora de mostrar los datos.
# Para evitar eso podemos hacer que ambos posean el mismo eje y
plt.figure()
ax1 = plt.subplot(1,2,1)
plt.plot(linear_data,'-o')
ax2 = plt.subplot(1,2,2, sharey=ax1)
plt.plot(exponential_data,'-x')
#plt.show()
#Existe una forma abreviada de escribir subplot: plt.subplot(1,2,1) == plt.subplot(121)
#Podemos crear una matrix de subplots para mostrar diferentes cosas
fig,((ax1,ax2,ax3),(ax4,ax5,ax6),(ax7,ax8,ax9)) = plt.subplots(3,3,sharex=True, sharey=True)
ax5.plot(linear_data, '-')
plt.show()
#En este caso las etiquetas de los ejex x e y solo aparecen en la parte izquierda y abajo, pero si queremos que en todos los plots aparezcan las etiquetas debemos iterar sobre cada plot
for ax in plt.gcf().get_axes():
    for label in ax.get_xticklabels() + ax.get_yticklabels():
        label.set_visible(True)
        #plt.gcf().canvas.draw()
#plt.show()
