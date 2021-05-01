import os


def ecrireListeDansUnFichier(liste, nomDuFichier):
    a = open(nomDuFichier, 'w')
    for i in range(len(liste)):
        a.write('%s\n' % liste[i])
    a.close()


def ecrireParametresDansUnFichier(nomDuFichier, longueurSegment, dureeExperience, nbPointsEspace, deltaX, deltaT, nbPointsTemps, v_max, rho_max, facteur):
    a = open(nomDuFichier, 'w')
    a.write("longueurSegment = " + str(longueurSegment) + "\n")
    a.write("dureeExperience = " + str(dureeExperience) + "\n")
    a.write("nbPointsEspace = " + str(nbPointsEspace) + "\n")
    a.write("deltaX = " + str(deltaX) + "\n")
    a.write("deltaT = " + str(deltaT) + "\n")
    a.write("nbPointsTemps = " + str(nbPointsTemps) + "\n")
    a.write("v_max = " + str(v_max) + "\n")
    a.write("rho_max = " + str(rho_max) + "\n")
    a.write("facteur = " + str(facteur) + "\n")


def reconstruireListe(nomDuFichier):
    a = open(nomDuFichier, 'r')
    liste = []
    lignes = a.readlines()
    for ligne in lignes:
        liste.append(float(ligne[:-1]))
    return liste


def reconstruireParametres(nomDuFichier):
    a = open(nomDuFichier, 'r')
    listeDesParametres = []
    lignes = a.readlines()
    longueurSegement = int(((lignes[0].split("="))[1])[1:])
    dureeExperience = int(((lignes[1].split("="))[1])[1:])
    nbPointsEspace= int(((lignes[2].split("="))[1])[1:])
    deltaX = float(((lignes[3].split("="))[1])[1:])
    deltaT = float(((lignes[4].split("="))[1])[1:])
    nbPointsTemps = int(((lignes[5].split("="))[1])[1:])
    v_max = float(((lignes[6].split("="))[1])[1:])
    rho_max = int(((lignes[7].split("="))[1])[1:])
    facteur = float(((lignes[8].split("="))[1])[1:])
    listeDesParametres.append(longueurSegement)
    listeDesParametres.append(dureeExperience)
    listeDesParametres.append(nbPointsEspace)
    listeDesParametres.append(deltaX)
    listeDesParametres.append(deltaT)
    listeDesParametres.append(nbPointsTemps)
    listeDesParametres.append(v_max)
    listeDesParametres.append(rho_max)
    listeDesParametres.append(facteur)
    return listeDesParametres


def nettoyage(repertoire):
    for rep, sreps, fics in os.walk(repertoire, topdown=False):
        for fic in fics:
            os.remove(os.path.join(rep, fic))
        for srep in sreps:
            os.rmdir(os.path.join(rep, srep))