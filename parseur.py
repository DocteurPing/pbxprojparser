#!/usr/bin/python2.7
# coding=utf-8

import sys
import os
import time

nom = ["Credit Maritime", "Banque de Savoie", "Banque Populaire", "iBP Test", "Banque Savoie Pro",
       "Credit Maritime Pro", "Banque Populaire Pro"]


# On reccupere les targets grace aux IDs en dur tout en regardant si ils ne sont pas dans le fichier ignorefile

def makeListTargetFromFile(tab, ignorefile):
    i = 0
    tabbuilds = []
    while i in xrange(len(tab)):
        if "94026BCA15E24582001BBF61 /* Sources */ =" in tab[i] and "Credit Maritime" not in ignorefile:
            tabbuilds.append(tab[i])
            print "Loading Credit Maritime ... ok"
        if "94026C1215E24588001BBF61 /* Sources */ =" in tab[i] and "Banque de Savoie" not in ignorefile:
            tabbuilds.append(tab[i])
            print "Loading Banque de Savoie ... ok"
        if "94780DA013C5B3D300D2D360 /* Sources */ =" in tab[i] and "Banque Populaire" not in ignorefile:
            tabbuilds.append(tab[i])
            print "Loading Banque Populaire ... ok"
        if "94780DC413C5B3D400D2D360 /* Sources */ =" in tab[i] and "iBP Test" not in ignorefile:
            tabbuilds.append(tab[i])
            print "Loading iBP Test ... ok"
        if "977A81C11BE7657D0068058F /* Sources */ =" in tab[i] and "Banque Savoie Pro" not in ignorefile:
            tabbuilds.append(tab[i])
            print "Loading Banque Savoie Pro ... ok"
        if "97B875211BE7618D00805A22 /* Sources */ =" in tab[i] and "Credit Maritime Pro" not in ignorefile:
            tabbuilds.append(tab[i])
            print "Loading Credit Maritime Pro ... ok"
        if "97FA28231B03560F00F31B2C /* Sources */ =" in tab[i] and "Banque Populaire Pro" not in ignorefile:
            tabbuilds.append(tab[i])
            print "Loading Banque Populaire Pro ... ok"
        i = i + 1
    print ""
    return tabbuilds


# On reccupere seulement les fichiers utiles en regardant leurs extensions


def getFiles(tab):
    splittab = tab.split(",")
    tabfiles = []
    i = 0
    while i in xrange(len(splittab)):
        if ".swift" in splittab[i] or ".m" in splittab[i]:
            tab2 = splittab[i].split("*")
            tabfiles.append(tab2[1])
        i = i + 1
    strtoreturn = ''.join(tabfiles)
    return strtoreturn


# On parse les lignes pour n'avoir que le nom du fichier

def getFileName(tab):
    i = 0
    while i in xrange(len(tab)):
        newtab = tab[i].split(";")
        tab[i] = getFiles(newtab[2])
        i = i + 1
    return tab

# On choisi le fichier de reference. On fais ce choix par rapport à la target qui a le plus de fichier


def selectTarget(files):
    i = 0
    intmax = 0
    maxi = []
    while i in xrange(len(files)):
        tab = files[i].split(" ")
        if len(tab) > len(maxi):
            intmax = i
            maxi = tab
        i = i + 1
    print "\nselected build", intmax, "as default\n"
    return intmax

# On regarde si il y a une difference entre les differentes targets


def findMissingFiles(str1, str2, ignorefile):
    tab1 = str1.split(" ")
    tab2 = str2.split(" ")
    i1 = 0
    check = -1
    check2 = 0
    total = []
    sys.stdout.write('[')
    sys.stdout.flush()
    while i1 in xrange(len(tab1)):
        i2 = 0
        while i2 in xrange(len(tab2)):
            if tab1[i1] in ignorefile:
                check = 0
                break
            if tab1[i1] == tab2[i2]:
                check = 0
                break
            i2 = i2 + 1
        if check == -1:
            total.append(tab1[i1] + " is missing")
            check2 = -1
        check = -1
        if i1 % 50 == 0:
            sys.stdout.write('=')
            sys.stdout.flush()
        i1 = i1 + 1
    print '>'
    print total
    return check2

# On affiche toutes les targets a qui il manque des fichiers


def showResultTest(tab, ignorefile):
    i = 0
    default = selectTarget(tab)
    while i in xrange(len(tab)):
        if findMissingFiles(tab[default], tab[i], ignorefile) == 0:
            print nom[i], "is good\n"
        else:
            print nom[i], "check fail\n"
        i = i + 1


# On cherche dans les targets si il y a un fichier correspondant à la recherche


def searchFile(tab, str1):
    i = 0
    while i in xrange(len(tab)):
        if str1 in tab[i]:
            print "file wich contains", str1, "in", nom[i]
        i = i + 1

# On regarde si la target choisi existe


def checkIfTargetExist(str1):
    i = 0
    while i in xrange(len(nom)):
        if str1.lower() in nom[i].lower():
            return i
        i = i + 1
    return -1

# On prend pour reference le fihcier passé en parametre


def targetFile(tab, str1, ignorefile):
    default = checkIfTargetExist(str1)
    i = 0
    if default == -1:
        print "No target available"
        return
    while i in xrange(len(tab)):
        print "checking for", nom[i], "...\n"
        findMissingFiles(tab[default], tab[i], ignorefile)
        i = i + 1

# On met a jour la liste des nom au cas ou il y ait un fichier à ignorer


def updateListName(ignorefile):
    i = 0
    while i in xrange(len(nom)):
        if nom[i] in ignorefile:
            del nom[i]
        i = i + 1

# On regarde les targets qui ont le fichier passé en parametre dnas leur liste de fihcier


def searchInTarget(tab, str1, str2):
    default = checkIfTargetExist(str2)
    if default == -1:
        print "No target available"
        return
    if str1 in tab[default]:
        print str1, "in file", nom[default]


def main():
    checks = checkt = 0
    if "-s" in sys.argv:
        checks = 1
    if "-t" in sys.argv:
        checkt = 1
    try:
        inputignorefile = open('ignorefile')
        ignorefile = inputignorefile.read()
        inputfile = open(sys.argv[1])
        contenu = inputfile.read()
    except:
        print "use ./parser.py file.pbxproj [-s, -t] [string to search][]\n" \
              "Must have an ignorefile even if it's an empty file"
        return
    if ((checks == 1 and checkt == 1) and len(sys.argv) < 6) or ((checkt == 1 or checks == 1) and len(sys.argv) < 4):
        print "use ./parser.py file.pbxproj [-s, -t] [string to search][]\n" \
              "Must have an ignorefile even if it's an empty file"
        return
    tab = contenu.split("};")
    updateListName(ignorefile)
    tabbuilds = makeListTargetFromFile(tab, ignorefile)
    tabbuilds = getFileName(tabbuilds)
    if checks == 1 and checkt == 0:
        searchFile(tabbuilds, sys.argv[3])
    elif checkt == 1 and checks == 0:
        targetFile(tabbuilds, sys.argv[3], ignorefile)
    elif checks == 1 and checkt == 1:
        searchInTarget(tabbuilds, sys.argv[4], sys.argv[5])
    else:
        showResultTest(tabbuilds, ignorefile)
    inputignorefile.close()
    inputfile.close()
    print "ending !"


if __name__ == "__main__":
    main()
