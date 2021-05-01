import numpy as np
import matplotlib.pyplot as plt
from GestionFichiers import *

listeDesParametres1 = reconstruireParametres("results/vitesseLineaire/configs/configdeltaX1.txt")
listeDesParametres2 = reconstruireParametres("results/vitesseLineaire/configs/configdeltaX2.txt")
listeDesParametres4 = reconstruireParametres("results/vitesseLineaire/configs/configdeltaX4.txt")
listeDesParametres8 = reconstruireParametres("results/vitesseLineaire/configs/configdeltaX8.txt")
listeDesParametres16 = reconstruireParametres("results/vitesseLineaire/configs/configdeltaX16.txt")
listeDesParametres32 = reconstruireParametres("results/vitesseLineaire/configs/configdeltaX32.txt")

rho_max = listeDesParametres1[7]
facteur = listeDesParametres1[8]
v_max = listeDesParametres1[6]
longueurSegment = listeDesParametres1[0]
dureeExperience = listeDesParametres1[1]

deltaX1 = listeDesParametres1[3]
deltaT1 = listeDesParametres1[4]
nbPointsTemps1 = listeDesParametres1[5]
nbPointsEspace1 = listeDesParametres1[2]

deltaX2 = listeDesParametres2[3]
deltaT2 = listeDesParametres2[4]
nbPointsTemps2 = listeDesParametres2[5]
nbPointsEspace2 = listeDesParametres2[2]

deltaX4 = listeDesParametres4[3]
deltaT4 = listeDesParametres4[4]
nbPointsTemps4 = listeDesParametres4[5]
nbPointsEspace4 = listeDesParametres4[2]

deltaX8 = listeDesParametres8[3]
deltaT8 = listeDesParametres8[4]
nbPointsTemps8 = listeDesParametres8[5]
nbPointsEspace8 = listeDesParametres8[2]

deltaX16 = listeDesParametres16[3]
deltaT16 = listeDesParametres16[4]
nbPointsTemps16 = listeDesParametres16[5]
nbPointsEspace16 = listeDesParametres16[2]

deltaX32 = listeDesParametres32[3]
deltaT32 = listeDesParametres32[4]
nbPointsTemps32 = listeDesParametres32[5]
nbPointsEspace32 = listeDesParametres32[2]

temps = 0

reference = reconstruireListe("results/vitesseLineaire/deltaX1/calcul/0.txt")
rho2 = reconstruireListe("results/vitesseLineaire/deltaX2/calcul/0.txt")
rho4 = reconstruireListe("results/vitesseLineaire/deltaX4/calcul/0.txt")
rho8 = reconstruireListe("results/vitesseLineaire/deltaX8/calcul/0.txt")
rho16 = reconstruireListe("results/vitesseLineaire/deltaX16/calcul/0.txt")
rho32 = reconstruireListe("results/vitesseLineaire/deltaX32/calcul/0.txt")

axeDistanceReference = np.linspace(0, longueurSegment, nbPointsEspace1)
axeDistance2 = np.linspace(0, longueurSegment, nbPointsEspace2)
axeDistance4 = np.linspace(0, longueurSegment, nbPointsEspace4)
axeDistance8 = np.linspace(0, longueurSegment, nbPointsEspace8)
axeDistance16 = np.linspace(0, longueurSegment, nbPointsEspace16)
axeDistance32 = np.linspace(0, longueurSegment, nbPointsEspace32)

plt.figure(1)
lineReference, = plt.plot(axeDistanceReference, reference)
line2, = plt.plot(axeDistance2, rho2)
line4, = plt.plot(axeDistance4, rho4)
line8, = plt.plot(axeDistance8, rho8)
line16, = plt.plot(axeDistance16, rho16)
line32, = plt.plot(axeDistance32, rho32)

plt.xlabel('distance (en m)')
plt.ylabel('rho (en vehicules / km)')
plt.ylim((0, rho_max))
text = plt.text(longueurSegment // 2, rho_max + 1, str(temps) + ' secondes')

for i in range(1, nbPointsTemps32):
    temps = temps + deltaT32
    reference = reconstruireListe("results/vitesseLineaire/deltaX1/calcul/" + str(32 * i) + ".txt")
    rho2 = reconstruireListe("results/vitesseLineaire/deltaX2/calcul/" + str(16 * i) + ".txt")
    rho4 = reconstruireListe("results/vitesseLineaire/deltaX4/calcul/" + str(8 * i) + ".txt")
    rho8= reconstruireListe("results/vitesseLineaire/deltaX8/calcul/" + str(4 * i) + ".txt")
    rho16 = reconstruireListe("results/vitesseLineaire/deltaX16/calcul/" + str(2 * i) + ".txt")
    rho32 = reconstruireListe("results/vitesseLineaire/deltaX32/calcul/" + str(i) + ".txt")
    lineReference.set_ydata(reference)
    line2.set_ydata(rho2)
    line4.set_ydata(rho4)
    line8.set_ydata(rho8)
    line16.set_ydata(rho16)
    line32.set_ydata(rho32)
    plt.pause(1e-5)
    text.set_text(str(temps) + ' secondes')
    plt.draw()


erreurPourcentage2 = reconstruireListe("results/vitesseLineaire/deltaX2/erreur/erreurPourcentage2.txt")
erreurPourcentage4 = reconstruireListe("results/vitesseLineaire/deltaX4/erreur/erreurPourcentage4.txt")
erreurPourcentage8 = reconstruireListe("results/vitesseLineaire/deltaX8/erreur/erreurPourcentage8.txt")
erreurPourcentage16 = reconstruireListe("results/vitesseLineaire/deltaX16/erreur/erreurPourcentage16.txt")
erreurPourcentage32 = reconstruireListe("results/vitesseLineaire/deltaX32/erreur/erreurPourcentage32.txt")
plt.figure(2)
axeTemporel2 = np.linspace(0, dureeExperience, nbPointsTemps2)
axeTemporel4 = np.linspace(0, dureeExperience, nbPointsTemps4)
axeTemporel8 = np.linspace(0, dureeExperience, nbPointsTemps8)
axeTemporel16 = np.linspace(0, dureeExperience, nbPointsTemps16)
axeTemporel32 = np.linspace(0, dureeExperience, nbPointsTemps32)
linePourcentage2, = plt.plot(axeTemporel2, erreurPourcentage2)
linePourcentage4, = plt.plot(axeTemporel4, erreurPourcentage4)
linePourcentage8, = plt.plot(axeTemporel8, erreurPourcentage8)
linePourcentage16, = plt.plot(axeTemporel16, erreurPourcentage16)
linePourcentage32, = plt.plot(axeTemporel32, erreurPourcentage32)
plt.legend((linePourcentage2, linePourcentage4, linePourcentage8, linePourcentage16, linePourcentage32), ('pourcentage d\'erreur, deltaX=2', 'pourcentage d\'erreur, deltaX=4', 'pourcentage d\'erreur, deltaX=8', 'pourcentage d\'erreur, deltaX=16', 'pourcentage d\'erreur, deltaX=32'))
plt.xlabel('temps (en secondes)')
plt.ylabel('pourcentage d\'erreur')
plt.draw()
plt.show()
