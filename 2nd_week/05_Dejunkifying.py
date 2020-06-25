import matplotlib.pyplot as plt
import numpy as np

plt.figure()

languages =['Python', 'SQL', 'Java', 'C++', 'JavaScript']
pos = np.arange(len(languages))
popularity = [56, 39, 34, 34, 29]

#Change the bar colors to be less bright blue, make one bar, the python bar, a contrasting
#color, soften all labels by turning grey.
colors = ['red']
colors2 = ['grey']*(len(pos)-1)
for c in colors2:
    colors.append(c)
print(colors)

#plt.bar(pos, popularity, align='center')
plt.bar(pos, popularity, color=colors, align='center')
#plt.xticks(pos, languages)
#plt.ylabel('% Popularity')
#plt.title('Top 5 Languages for Math & Data \nby % popularity on Stack Overflow', alpha=0.8)
plt.xticks(pos, languages, color='grey')
#plt.ylabel('% Popularity', color='grey')
plt.title('Top 5 Languages for Math & Data \nby % popularity on Stack Overflow', alpha=0.8, color='grey')

# remove all the ticks (both axes), and tick labels on the Y axis
plt.tick_params(top='off', bottom='off', left='off', right='off', labelleft='off', labelbottom='on')
#Remove the frame of the chart.
plt.box(False)

#Directly label each bar with Y axis values, and remove the Y label since bars are directly labeled.
for i, pop in enumerate(popularity):
    plt.text(pos[i]-0.2, pop-5, str(pop)+'%', color='w', fontsize=15)

plt.savefig('Dejunkifying.pdf')
#plt.show()
