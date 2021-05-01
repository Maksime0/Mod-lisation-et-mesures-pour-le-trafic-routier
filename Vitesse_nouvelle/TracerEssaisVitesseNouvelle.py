import numpy as np
import matplotlib.pyplot as plt
from GestionFichiers import *

listeDesParametres = reconstruireParametres("results/essaisVitesseNouvelle/config/config.txt")
longueurSegment = listeDesParametres[0]
dureeExperience = listeDesParametres[1]
nbPointsEspace = listeDesParametres[2]
deltaX = listeDesParametres[3]
deltaT = listeDesParametres[4]
nbPointsTemps = listeDesParametres[5]
v_max = listeDesParametres[6]
rho_max = listeDesParametres[7]
facteur = listeDesParametres[8]

temps = 0
rho = reconstruireListe("results/essaisVitesseNouvelle/calculs/0.txt")
axeDistance = np.linspace(0, longueurSegment, nbPointsEspace)
plt.figure(1)
line, = plt.plot(axeDistance, rho)
#plt.legend((line), ('rho'))
plt.xlabel('distance (en m)')
plt.ylabel('rho (en vehicules / km)')
plt.ylim((0, rho_max))
text = plt.text(longueurSegment // 2, rho_max + 1, str(temps) + ' secondes')

for i in range(1, nbPointsTemps):
    temps = temps + deltaT
    rho = reconstruireListe("results/essaisVitesseNouvelle/calculs/" + str(i) + ".txt")
    line.set_ydata(rho)
    plt.pause(1e-5)
    text.set_text(str(temps) + ' secondes')
    plt.draw()
