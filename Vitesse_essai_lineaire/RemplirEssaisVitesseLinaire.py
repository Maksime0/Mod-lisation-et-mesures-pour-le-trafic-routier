from GestionFichiers import *
from FonctionsEssaisVitesseLineaire import *

rho_max = 250
v_max = 130 / 3.6
longueurSegment = 100000
dureeExperience = 900
facteur = 1 + 1e-2
nbPointsEspace = 25000
deltaX = longueurSegment / nbPointsEspace
deltaT = deltaX * (1 / (facteur * v_max))
nbPointsTemps = int(dureeExperience / deltaT)

rho = [rho0(i * deltaX, longueurSegment) for i in range(nbPointsEspace)]

nettoyage("results/essaisVitesseLineaire/config/")
nettoyage("results/essaisVitesseLineaire/calculs/")

ecrireParametresDansUnFichier("results/essaisVitesseLineaire/config/config.txt", longueurSegment, dureeExperience, nbPointsEspace, deltaX, deltaT, nbPointsTemps, v_max, rho_max, facteur)
ecrireListeDansUnFichier(rho, "results/essaisVitesseLineaire/calculs/0.txt")

temps = 0

for i in range(1, nbPointsTemps):
    temps = temps + deltaT
    rho = calcul(rho, deltaT, deltaX, v_max, rho_max)
    ecrireListeDansUnFichier(rho, "results/essaisVitesseLineaire/calculs/" + str(i) + ".txt")
