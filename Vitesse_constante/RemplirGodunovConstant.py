from GestionFichiers import *
from FonctionsGodunovConstant import *

valMax = 200

rho_max = 250
v_max = 100 / 3.6
longueurSegment = 1000
dureeExperience = 20
facteur = 1 + 1e-2
nbPointsEspace = 1000
deltaX = longueurSegment / nbPointsEspace
deltaT = deltaX * (1 / (facteur * v_max))
nbPointsTemps = int(dureeExperience / deltaT)

rho = [rho0(i * deltaX, longueurSegment) for i in range(nbPointsEspace)]
reference = [rho0(i * deltaX, longueurSegment) for i in range(nbPointsEspace)]
erreurPourcentage = [0 for i in range(nbPointsTemps)]

nettoyage("results/vitesseConstante/config/")
nettoyage("results/vitesseConstante/calculee/")
nettoyage("results/vitesseConstante/theorique/")
nettoyage("results/vitesseConstante/erreur/")

ecrireParametresDansUnFichier("results/vitesseConstante/config/config.txt", longueurSegment, dureeExperience, nbPointsEspace, deltaX, deltaT, nbPointsTemps, v_max, rho_max, facteur)
ecrireListeDansUnFichier(rho, "results/vitesseConstante/calculee/0.txt")
ecrireListeDansUnFichier(reference, "results/vitesseConstante/theorique/0.txt")

temps = 0

for i in range(1, nbPointsTemps):
    temps = temps + deltaT
    rho = calcul(rho, deltaT, deltaX, v_max)
    reference = [rhoTheorique(j * deltaX, temps, v_max, longueurSegment) for j in range(nbPointsEspace)]
    difference = [(rho[k] - reference[k]) for k in range(nbPointsEspace)]
    erreurPourcentage[i] = calculerNormeErreur(difference, deltaX) / calculerNormeErreur(reference, deltaX) * 100
    ecrireListeDansUnFichier(rho, "results/vitesseConstante/calculee/" + str(i) + ".txt")
    ecrireListeDansUnFichier(reference, "results/vitesseConstante/theorique/" + str(i) + ".txt")

ecrireListeDansUnFichier(erreurPourcentage, "results/vitesseConstante/erreur/erreurPourcentage.txt")