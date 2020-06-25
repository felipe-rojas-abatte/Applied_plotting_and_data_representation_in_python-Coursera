import matplotlib.animation as animation #Modulo de animacion
import matplotlib.pyplot as plt
import numpy as np

#creamos una distribucion normal con 100 datos
n = 100
x = np.random.randn(n) #los numeros aleatorios los guardamos en x

#Creamos la funcion que va a hacer el gŕafico, donde curr es el frame actual
def update(curr):
    if curr == n: # verificamos si la animacion tiene su ultimo dato para parar la animacion
        a.event_source.stop() # a es el nombre de la animacion
    plt.cla() #limpiamos el eje actual
    bins = np.arange(-4, 4, 0.5) #seleccionamos el rango de los bins del histograma desde -4 hasta 4 separados una distancia de 0.5
    plt.hist(x[:curr], bins=bins) #definmos el histograma desde 0 hasta el frame actual
    plt.axis([-4,4,0,30])
    plt.gca().set_title('Sampling the Normal Distribution') #titulo
    plt.gca().set_ylabel('Frequency') #nombre de los ejex
    plt.gca().set_xlabel('Value')
    plt.annotate('n = {}'.format(curr), [3,27])

fig = plt.figure()
a = animation.FuncAnimation(fig, update, interval=100) #modulo de animacion (figura que estamos trabajando, el nombre de la funcion "update", intervalo de tiempo entre cada actualizacion en milisegundos )
plt.show()
#plt.savefig('animacion.pdf')
