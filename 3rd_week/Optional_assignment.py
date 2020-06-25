import matplotlib.animation as animation #Modulo de animacion
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import numpy as np

n = 500
## Definimos las distribuciones
x1 = np.random.normal(-2.5, 1, n)
x2 = np.random.gamma(2, 1.5, n)
x3 = np.random.exponential(2, n)
x4 = np.random.uniform(14,21, n)

x = [x1, x2, x3, x4]

bins1 = np.arange(-7.5, 2.5, 0.5)
bins2 = np.arange(0, 10, 0.5)
bins3 = np.arange(0, 17, 0.5)
bins4 = np.arange(14, 21, 0.5)
bins = [bins1, bins2, bins3, bins4]

axis1 = [-7.5, 2.5, 0, 0.6]
axis2 = [0, 10, 0, 0.6]
axis3 = [0, 17, 0, 0.6]
axis4 = [13, 22, 0, 0.6]
axis = [axis1, axis2, axis3, axis4]

gspec = gridspec.GridSpec(2, 2)
plt.figure()
#definimos posicion de distribuciones en grid
ax1 = plt.subplot(gspec[0, 0])
ax2 = plt.subplot(gspec[0, 1])
ax3 = plt.subplot(gspec[1, 0])
ax4 = plt.subplot(gspec[1, 1])
ax = [ax1, ax2, ax3, ax4]
for a in ax:
    # Quitamos linea superior y derecha del marco del histograma
    a.spines['right'].set_visible(False)
    a.spines['top'].set_visible(False)
gspec.update(wspace = 0.6, hspace = .6) #separacion horizontal y vertial de los histogramas

def update(curr):
    if curr == n:
        a.event_source.stop()
    for i in range(len(ax)):
        ax[i].cla()
        ax[i].hist(x[i][:curr], normed = True, bins = bins[i])
        ax[i].axis(axis[i])
        ax[i].set_ylabel('Frequency')
        ax1.annotate('n = {}'.format(curr), [2,0.6])
        ax2.annotate('n = {}'.format(curr), [10,0.6])
        ax3.annotate('n = {}'.format(curr), [17,0.6])
        ax4.annotate('n = {}'.format(curr), [22,0.6])
    ax1.set_title('Normal')
    ax2.set_title('Gamma')
    ax3.set_title('Exponential')
    ax4.set_title('Uniform')
    #plt.tight_layout()

fig = plt.gcf()
a = animation.FuncAnimation(fig, update, interval = 100)
plt.show()
