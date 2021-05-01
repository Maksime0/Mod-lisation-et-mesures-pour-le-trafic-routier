from GestionFichiers import *
from FonctionsEssaisVitesseNouvelle import *

rho_max = 250
v_max = 130 / 3.6
longueurSegment = 10000
dureeExperience = 100
facteur = 1 + 1e-2
nbPointsEspace = 10000
deltaX = longueurSegment / nbPointsEspace
deltaT = deltaX * (1 / (facteur * v_max))
nbPointsTemps = int(dureeExperience / deltaT)

rho = [rho0(i * deltaX, longueurSegment) for i in range(nbPointsEspace)]

nettoyage("results/essaisVitesseNouvelle/config/")
nettoyage("results/essaisVitesseNouvelle/calculs/")

ecrireParametresDansUnFichier("results/essaisVitesseNouvelle/config/config.txt", longueurSegment, dureeExperience, nbPointsEspace, deltaX, deltaT, nbPointsTemps, v_max, rho_max, facteur)
ecrireListeDansUnFichier(rho, "results/essaisVitesseNouvelle/calculs/0.txt")

temps = 0

for i in range(1, nbPointsTemps):
    temps = temps + deltaT
    rho = calcul(rho, deltaT, deltaX, v_max, rho_max)
    ecrireListeDansUnFichier(rho, "results/essaisVitesseNouvelle/calculs/" + str(i) + ".txt")
