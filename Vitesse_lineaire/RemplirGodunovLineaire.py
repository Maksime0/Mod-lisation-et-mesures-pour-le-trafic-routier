from GestionFichiers import *
from FonctionsGodunovLineaire import *

rho_max = 250
v_max = 130 / 3.6
longueurSegment = 32000
dureeExperience = 300
facteur = 1.001

matriceDesFacteurs = [1, 2, 4, 8, 16, 32]
matriceDesNombresPointsEspace = [int(longueurSegment / matriceDesFacteurs[i]) for i in range(len(matriceDesFacteurs))]
matriceDesDeltaX = [matriceDesFacteurs[i] for i in range(len(matriceDesFacteurs))]
matriceDesDeltaT = [(matriceDesDeltaX[i] * (1 / (facteur * v_max))) for i in range(len(matriceDesFacteurs))]
matriceDesNombresPointsTemps = [(int(dureeExperience / matriceDesDeltaT[i])) for i in range(len(matriceDesFacteurs))]

reference = [rho0(i * matriceDesDeltaX[0], longueurSegment) for i in range(matriceDesNombresPointsEspace[0])]
rho2 = [rho0(i * matriceDesDeltaX[1], longueurSegment) for i in range(matriceDesNombresPointsEspace[1])]
rho4 = [rho0(i * matriceDesDeltaX[2], longueurSegment) for i in range(matriceDesNombresPointsEspace[2])]
rho8 = [rho0(i * matriceDesDeltaX[3], longueurSegment) for i in range(matriceDesNombresPointsEspace[3])]
rho16 = [rho0(i * matriceDesDeltaX[4], longueurSegment) for i in range(matriceDesNombresPointsEspace[4])]
rho32 = [rho0(i * matriceDesDeltaX[5], longueurSegment) for i in range(matriceDesNombresPointsEspace[5])]

erreurPourcentage2 = [0 for i in range(matriceDesNombresPointsTemps[1])]
erreurPourcentage4 = [0 for i in range(matriceDesNombresPointsTemps[2])]
erreurPourcentage8 = [0 for i in range(matriceDesNombresPointsTemps[3])]
erreurPourcentage16 = [0 for i in range(matriceDesNombresPointsTemps[4])]
erreurPourcentage32 = [0 for i in range(matriceDesNombresPointsTemps[5])]

nettoyage("results/vitesseLineaire/configs/")
nettoyage("results/vitesseLineaire/deltaX1/calcul/")
nettoyage("results/vitesseLineaire/deltaX2/calcul/")
nettoyage("results/vitesseLineaire/deltaX2/erreur/")
nettoyage("results/vitesseLineaire/deltaX4/calcul/")
nettoyage("results/vitesseLineaire/deltaX4/erreur/")
nettoyage("results/vitesseLineaire/deltaX8/calcul/")
nettoyage("results/vitesseLineaire/deltaX8/erreur/")
nettoyage("results/vitesseLineaire/deltaX16/calcul/")
nettoyage("results/vitesseLineaire/deltaX16/erreur/")
nettoyage("results/vitesseLineaire/deltaX32/calcul/")
nettoyage("results/vitesseLineaire/deltaX32/erreur/")

ecrireParametresDansUnFichier("results/vitesseLineaire/configs/configdeltaX1.txt", longueurSegment, dureeExperience, matriceDesNombresPointsEspace[0], matriceDesDeltaX[0], matriceDesDeltaT[0], matriceDesNombresPointsTemps[0], v_max, rho_max, facteur)
ecrireParametresDansUnFichier("results/vitesseLineaire/configs/configdeltaX2.txt", longueurSegment, dureeExperience, matriceDesNombresPointsEspace[1], matriceDesDeltaX[1], matriceDesDeltaT[1], matriceDesNombresPointsTemps[1], v_max, rho_max, facteur)
ecrireParametresDansUnFichier("results/vitesseLineaire/configs/configdeltaX4.txt", longueurSegment, dureeExperience, matriceDesNombresPointsEspace[2], matriceDesDeltaX[2], matriceDesDeltaT[2], matriceDesNombresPointsTemps[2], v_max, rho_max, facteur)
ecrireParametresDansUnFichier("results/vitesseLineaire/configs/configdeltaX8.txt", longueurSegment, dureeExperience, matriceDesNombresPointsEspace[3], matriceDesDeltaX[3], matriceDesDeltaT[3], matriceDesNombresPointsTemps[3], v_max, rho_max, facteur)
ecrireParametresDansUnFichier("results/vitesseLineaire/configs/configdeltaX16.txt", longueurSegment, dureeExperience, matriceDesNombresPointsEspace[4], matriceDesDeltaX[4], matriceDesDeltaT[4], matriceDesNombresPointsTemps[4], v_max, rho_max, facteur)
ecrireParametresDansUnFichier("results/vitesseLineaire/configs/configdeltaX32.txt", longueurSegment, dureeExperience, matriceDesNombresPointsEspace[5], matriceDesDeltaX[5], matriceDesDeltaT[5], matriceDesNombresPointsTemps[5], v_max, rho_max, facteur)
ecrireListeDansUnFichier(reference, "results/vitesseLineaire/deltaX1/calcul/0.txt")
ecrireListeDansUnFichier(rho2, "results/vitesseLineaire/deltaX2/calcul/0.txt")
ecrireListeDansUnFichier(rho4, "results/vitesseLineaire/deltaX4/calcul/0.txt")
ecrireListeDansUnFichier(rho8, "results/vitesseLineaire/deltaX8/calcul/0.txt")
ecrireListeDansUnFichier(rho16, "results/vitesseLineaire/deltaX16/calcul/0.txt")
ecrireListeDansUnFichier(rho32, "results/vitesseLineaire/deltaX32/calcul/0.txt")

temps = 0
for i in range(1, matriceDesNombresPointsTemps[0]):
    temps = temps + matriceDesDeltaT[0]
    reference = calcul(reference, matriceDesDeltaT[0], matriceDesDeltaX[0], v_max, rho_max)
    ecrireListeDansUnFichier(reference, "results/vitesseLineaire/deltaX1/calcul/" + str(i) + ".txt")

temps = 0
for i in range(1, matriceDesNombresPointsTemps[1]):
    temps = temps + matriceDesDeltaT[1]
    rho2 = calcul(rho2, matriceDesDeltaT[1], matriceDesDeltaX[1], v_max, rho_max)
    ref = reconstruireListe("results/vitesseLineaire/deltaX1/calcul/" + str(2 * i) + ".txt")
    ecrireListeDansUnFichier(rho2, "results/vitesseLineaire/deltaX2/calcul/" + str(i) + ".txt")
    referenceRetouchee = [(ref[2 * k]) for k in range(matriceDesNombresPointsEspace[1])]
    difference = [(rho2[k] - referenceRetouchee[k]) for k in range(matriceDesNombresPointsEspace[1])]
    erreurPourcentage2[i] = calculerNormeErreur(difference, matriceDesDeltaX[1]) / calculerNormeErreur(referenceRetouchee, matriceDesDeltaX[1]) * 100

temps = 0
for i in range(1, matriceDesNombresPointsTemps[2]):
    temps = temps + matriceDesDeltaT[2]
    rho4 = calcul(rho4, matriceDesDeltaT[2], matriceDesDeltaX[2], v_max, rho_max)
    ref = reconstruireListe("results/vitesseLineaire/deltaX1/calcul/" + str(4 * i) + ".txt")
    ecrireListeDansUnFichier(rho4, "results/vitesseLineaire/deltaX4/calcul/" + str(i) + ".txt")
    referenceRetouchee = [(ref[4 * k]) for k in range(matriceDesNombresPointsEspace[2])]
    difference = [(rho4[k] - referenceRetouchee[k]) for k in range(matriceDesNombresPointsEspace[2])]
    erreurPourcentage4[i] = calculerNormeErreur(difference, matriceDesDeltaX[2]) / calculerNormeErreur(referenceRetouchee, matriceDesDeltaX[2]) * 100

temps = 0
for i in range(1, matriceDesNombresPointsTemps[3]):
    temps = temps + matriceDesDeltaT[3]
    rho8 = calcul(rho8, matriceDesDeltaT[3], matriceDesDeltaX[3], v_max, rho_max)
    ref = reconstruireListe("results/vitesseLineaire/deltaX1/calcul/" + str(8 * i) + ".txt")
    ecrireListeDansUnFichier(rho8, "results/vitesseLineaire/deltaX8/calcul/" + str(i) + ".txt")
    referenceRetouchee = [(ref[8 * k]) for k in range(matriceDesNombresPointsEspace[3])]
    difference = [(rho8[k] - referenceRetouchee[k]) for k in range(matriceDesNombresPointsEspace[3])]
    erreurPourcentage8[i] = calculerNormeErreur(difference, matriceDesDeltaX[3]) / calculerNormeErreur(referenceRetouchee, matriceDesDeltaX[3]) * 100

temps = 0
for i in range(1, matriceDesNombresPointsTemps[4]):
    temps = temps + matriceDesDeltaT[4]
    rho16 = calcul(rho16, matriceDesDeltaT[4], matriceDesDeltaX[4], v_max, rho_max)
    ref = reconstruireListe("results/vitesseLineaire/deltaX1/calcul/" + str(16 * i) + ".txt")
    ecrireListeDansUnFichier(rho16, "results/vitesseLineaire/deltaX16/calcul/" + str(i) + ".txt")
    referenceRetouchee = [(ref[16 * k]) for k in range(matriceDesNombresPointsEspace[4])]
    difference = [(rho16[k] - referenceRetouchee[k]) for k in range(matriceDesNombresPointsEspace[4])]
    erreurPourcentage16[i] = calculerNormeErreur(difference, matriceDesDeltaX[4]) / calculerNormeErreur(referenceRetouchee, matriceDesDeltaX[4]) * 100

temps = 0
for i in range(1, matriceDesNombresPointsTemps[5]):
    temps = temps + matriceDesDeltaT[5]
    rho32 = calcul(rho32, matriceDesDeltaT[5], matriceDesDeltaX[5], v_max, rho_max)
    ref = reconstruireListe("results/vitesseLineaire/deltaX1/calcul/" + str(32 * i) + ".txt")
    ecrireListeDansUnFichier(rho32, "results/vitesseLineaire/deltaX32/calcul/" + str(i) + ".txt")
    referenceRetouchee = [(ref[32 * k]) for k in range(matriceDesNombresPointsEspace[5])]
    difference = [(rho32[k] - referenceRetouchee[k]) for k in range(matriceDesNombresPointsEspace[5])]
    erreurPourcentage32[i] = calculerNormeErreur(difference, matriceDesDeltaX[5]) / calculerNormeErreur(referenceRetouchee, matriceDesDeltaX[5]) * 100


ecrireListeDansUnFichier(erreurPourcentage2, "results/vitesseLineaire/deltaX2/erreur/erreurPourcentage2.txt")
ecrireListeDansUnFichier(erreurPourcentage4, "results/vitesseLineaire/deltaX4/erreur/erreurPourcentage4.txt")
ecrireListeDansUnFichier(erreurPourcentage8, "results/vitesseLineaire/deltaX8/erreur/erreurPourcentage8.txt")
ecrireListeDansUnFichier(erreurPourcentage16, "results/vitesseLineaire/deltaX16/erreur/erreurPourcentage16.txt")
ecrireListeDansUnFichier(erreurPourcentage32, "results/vitesseLineaire/deltaX32/erreur/erreurPourcentage32.txt")
