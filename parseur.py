#!/usr/bin/python2.7
# coding=utf-8

import sys

nom = ["Credit Maritime", "Banque de Savoie", "Banque Populaire", "iBP Test", "Banque Savoie Pro",
       "Credit Maritime Pro", "Banque Populaire Pro"]


# On reccupere les targets grace aux IDs en dur tout en regardant si ils ne sont pas dans le fichier ignorefile

def makeListTargetFromFile(tab):
    i = 0
    tabbuilds = []
    while i in xrange(len(tab)):
        if "94026BCA15E24582001BBF61 /* Sources */ =" in tab[i]:
            tabbuilds.append(tab[i])
            print "Loading Credit Maritime ... ok"
        if "94026C1215E24588001BBF61 /* Sources */ =" in tab[i]:
            tabbuilds.append(tab[i])
            print "Loading Banque de Savoie ... ok"
        if "94780DA013C5B3D300D2D360 /* Sources */ =" in tab[i]:
            tabbuilds.append(tab[i])
            print "Loading Banque Populaire ... ok"
        if "94780DC413C5B3D400D2D360 /* Sources */ =" in tab[i]:
            tabbuilds.append(tab[i])
            print "Loading iBP Test ... ok"
        if "977A81C11BE7657D0068058F /* Sources */ =" in tab[i]:
            tabbuilds.append(tab[i])
            print "Loading Banque Savoie Pro ... ok"
        if "97B875211BE7618D00805A22 /* Sources */ =" in tab[i]:
            tabbuilds.append(tab[i])
            print "Loading Credit Maritime Pro ... ok"
        if "97FA28231B03560F00F31B2C /* Sources */ =" in tab[i]:
            tabbuilds.append(tab[i])
            print "Loading Banque Populaire Pro ... ok"
        i = i + 1
    return tabbuilds


def makeignorefile(ignorefile):
    tab = ignorefile.split("\n")
    tabtotal = []
    statut = -1
    i2 = 0
    for i in xrange(len(tab)):
        if i2 in xrange(len(nom)) and nom[i2] in tab[i]:
            i2 += 1
            statut += 1
            tabtotal.append("")
            continue
        if statut >= 0:
            tabtotal[statut] += " " + tab[i]
    return tabtotal


def makefiletab(files):
    tab = []
    check = -1
    for line in files:
        if "Begin PBXBuildFile" in line:
            check = 0
        if "End PBXBuildFile" in line:
            break
        if check == 0:
            if ".m" in line or ".swift" in line:
                tmp = line.split("*")
                if 1 in xrange(len(tmp)):
                    tmp = tmp[1].split(" ")
                    if tmp[1] not in tab:
                        tab.append(tmp[1])
    return tab


def printtab(tab):
    for i in xrange(len(tab)):
        print tab[i]


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


def checkignorefile(str1, ignorefile):
    tab = ignorefile.split(" ")
    i = 1
    while i in xrange(len(tab)):
        if tab[i] in str1:
            return 0
        i += 1
    return -1


# On regarde si il y a une difference entre les differentes targets

def findMissingFiles(tab1, str2, ignorefile):
    tab2 = str2.split(" ")
    i1 = 0
    check2 = 0
    total = []
    sys.stdout.write('[')
    sys.stdout.flush()
    while i1 in xrange(len(tab1)):
        if tab1[i1] not in tab2 and checkignorefile(tab1[i1], ignorefile) == -1:
            total.append(tab1[i1] + " is missing")
            check2 = -1
        if i1 % 30 == 0:
            sys.stdout.write('=')
            sys.stdout.flush()
        i1 = i1 + 1
    print '>\n'
    printtab(total)
    return check2


# On affiche toutes les targets a qui il manque des fichiers


def showResultTest(tab, tabref, ignorefile):
    i = 0
    while i in xrange(len(tab)):
        if findMissingFiles(tabref, tab[i], ignorefile[i]) == 0:
            print nom[i], "has no missing files\n"
        else:
            print nom[i], "check fail\n"
        i = i + 1

# On met a jour la liste des nom au cas ou il y ait un fichier à ignorer


def main():
    try:
        inputignorefile = open('ignorefile')
        ignorefile = inputignorefile.read()
        inputfile = open(sys.argv[1])
        contenu = inputfile.read()
    except:
        print "use ./parser.py file.pbxproj\n" \
              "Must have an ignorefile even if it's an empty file"
        return
    tab = contenu.split("};")
    tabref = makefiletab(tab)
    tabbuilds = makeListTargetFromFile(tab)
    tabbuilds = getFileName(tabbuilds)
    ignorefile = makeignorefile(ignorefile)
    showResultTest(tabbuilds, tabref, ignorefile)
    inputignorefile.close()
    inputfile.close()
    print "ending !"


if __name__ == "__main__":
    main()