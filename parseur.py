#!/usr/bin/python2.7

import sys

nom = ["Credit Maritime", "Banque de Savoie", "Banque Populaire", "iBP Test", "Banque Savoie Pro",
       "Credit Maritime Pro", "Banque Populaire Pro"]


def puttabintab(tab, ignorefile):
    i = 0
    tabbuilds = []
    while i in xrange(len(tab)):
        if "94026BDD15E24582001BBF61 /* Resources */ =" in tab[i] and "Credit Maritime" not in ignorefile:
            tabbuilds.append(tab[i])
            print "Loading Credit Maritime ... ok"
        if "94026C2515E24588001BBF61 /* Resources */ =" in tab[i] and "Banque de Savoie" not in ignorefile:
            tabbuilds.append(tab[i])
            print "Loading Banque de Savoie ... ok"
        if "94780DA213C5B3D300D2D360 /* Resources */ =" in tab[i] and "Banque Populaire" not in ignorefile:
            tabbuilds.append(tab[i])
            print "Loading Banque Populaire ... ok"
        if "94780DC613C5B3D400D2D360 /* Resources */ =" in tab[i] and "iBP Test" not in ignorefile:
            tabbuilds.append(tab[i])
            print "Loading iBP Test ... ok"
        if "977A83441BE7657D0068058F /* Resources */ =" in tab[i] and "Banque Savoie Pro" not in ignorefile:
            tabbuilds.append(tab[i])
            print "Loading Banque Savoie Pro ... ok"
        if "97B876A41BE7618D00805A22 /* Resources */ =" in tab[i] and "Credit Maritime Pro" not in ignorefile:
            tabbuilds.append(tab[i])
            print "Loading Credit Maritime Pro ... ok"
        if "97FA28F91B03560F00F31B2C /* Resources */ =" in tab[i] and "Banque Populaire Pro" not in ignorefile:
            tabbuilds.append(tab[i])
            print "Loading Banque Populaire Pro ... ok"
        i = i + 1
    print ""
    return tabbuilds


def getfiles(tab):
    splittab = tab.split(",")
    tabfiles = []
    i = 0
    while i in xrange(len(splittab)):
        if ".xib" in splittab[i] or ".swift" in splittab[i] or ".m" in splittab[i] or ".storyboard" in splittab[i] or \
                        ".xml" in splittab[i] or ".xcassets" in splittab[i]:
            tab2 = splittab[i].split("*")
            tabfiles.append(tab2[1])
        i = i + 1
    strtoreturn = ''.join(tabfiles)
    return strtoreturn


def formattab(tab):
    i = 0
    while i in xrange(len(tab)):
        newtab = tab[i].split(";")
        tab[i] = getfiles(newtab[2])
        i = i + 1
    return tab


def selecttab(files):
    i = 0
    intmax = 0
    maxi = []
    while i in xrange(len(files)):
        tab = files[i].split(" ")
        if len(tab) > len(maxi):
            intmax = i
            maxi = tab
        i = i + 1
    print "selected build", intmax, "as default"
    return intmax


def checkequal(str1, str2, ignorefile):
    tab1 = str1.split(" ")
    tab2 = str2.split(" ")
    i1 = 0
    check = -1
    check2 = 0
    while i1 in xrange(len(tab1)):
        i2 = 0
        while i2 in xrange(len(tab2)):
            if tab1[i1] == tab2[i2] or tab1[i1] in ignorefile:
                check = 0
                break
            i2 = i2 + 1
        if check == -1:
            print tab1[i1], "is missing"
            check2 = -1
        check = -1
        i1 = i1 + 1
    return check2


def showdiff(tab, ignorefile):
    i = 0
    default = selecttab(tab)
    while i in xrange(len(tab)):
        if checkequal(tab[default], tab[i], ignorefile) == 0:
            print '==========>', nom[i], "is good\n"
        else:
            print '==========>', nom[i], "check fail\n"
        i = i + 1


def searchfile(tab, str1):
    i = 0
    while i in xrange(len(tab)):
        if str1 in tab[i]:
            print str1, "in file", nom[i]
        i = i + 1


def findpath(str1):
    i = 0
    while i in xrange(len(nom)):
        if str1.lower() in nom[i].lower():
            return i
        i = i + 1
    return -1


def targetfile(tab, str1, ignorefile):
    default = findpath(str1)
    i = 0
    if default == -1:
        print "No target available"
        return
    while i in xrange(len(tab)):
        print "checking for", nom[i], "...\n"
        checkequal(tab[default], tab[i], ignorefile)
        i = i + 1


def updatename(ignorefile):
    i = 0
    while i in xrange(len(nom)):
        if nom[i] in ignorefile:
            del nom[i]
        i = i + 1


def main():
    checks = 0
    checkt = 0
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
    if (checks == 1 and checkt == 1) and len(sys.argv) < 5:
        print "use ./parser.py file.pbxproj [-s, -t] [string to search][]\n" \
              "Must have an ignorefile even if it's an empty file"
        return
    elif (checkt == 1 or checks == 1) and len(sys.argv) < 4:
        print "use ./parser.py file.pbxproj [-s, -t] [string to search][]\n" \
              "Must have an ignorefile even if it's an empty file"
        return
    tab = contenu.split("};")
    updatename(ignorefile)
    tabbuilds = puttabintab(tab, ignorefile)
    tabbuilds = formattab(tabbuilds)
    if checks == 1:
        searchfile(tabbuilds, sys.argv[3])
    elif checkt == 1:
        targetfile(tabbuilds, sys.argv[3], ignorefile)
    else:
        showdiff(tabbuilds, ignorefile)
    inputignorefile.close()
    inputfile.close()
    print "ending !"


if __name__ == "__main__":
    main()
