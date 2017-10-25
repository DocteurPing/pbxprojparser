#!/usr/bin/python2.7


def puttabintab(tab):
    i = 0
    tabbuilds = []
    while i in xrange(len(tab)):
        if "94026BDD15E24582001BBF61 /* Resources */ =" in tab[i]:
            tabbuilds.append(tab[i])
            print "loading 1 ... ok"
        if "94026C2515E24588001BBF61 /* Resources */ =" in tab[i]:
            tabbuilds.append(tab[i])
            print "loading 2 ... ok"
        if "94780DA213C5B3D300D2D360 /* Resources */ =" in tab[i]:
            tabbuilds.append(tab[i])
            print "loading 3 ... ok"
        if "94780DC613C5B3D400D2D360 /* Resources */ =" in tab[i]:
            tabbuilds.append(tab[i])
            print "loading 4 ... ok"
        if "977A83441BE7657D0068058F /* Resources */ =" in tab[i]:
            tabbuilds.append(tab[i])
            print "loading 5 ... ok"
        if "97B876A41BE7618D00805A22 /* Resources */ =" in tab[i]:
            tabbuilds.append(tab[i])
            print "loading 6 ... ok"
        if "97FA28F91B03560F00F31B2C /* Resources */ =" in tab[i]:
            tabbuilds.append(tab[i])
            print "loading 7 ... ok"
        i = i + 1
    return tabbuilds


def printtab(tab):
    i = 0
    while i < len(tab):
        print(tab[i])
        i = i + 1


def getfiles(tab):
    splittab = tab.split(",")
    tabfiles = []
    i = 0
    while i in xrange(len(splittab)):
        if "xib" in splittab[i]:
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
    max = []
    while i in xrange(len(files)):
        tab = files[i].split(" ")
        if len(tab) > len(max):
            intmax = i
            max = tab
        i = i + 1
    print "selected build", intmax, "as default"
    return intmax


def checkequal(str1, str2):
    tab1 = str1.split(" ")
    tab2 = str2.split(" ")
    i1 = 0
    check = -1
    while i1 in xrange(len(tab1)):
        i2 = 0
        while i2 in xrange(len(tab2)):
            if tab1[i1] == tab2[i2]:
                check = 0
                i2 = i2 + 1
                continue
            i2 = i2 + 1
        if check == -1:
            print tab1[i1], "is missing"
        check = -1
        i1 = i1 + 1
    return -1


def showdiff(tab):
    default = selecttab(tab)
    i = 0
    while i in xrange(len(tab)):
        if checkequal(tab[default], tab[i]) == 0:
            print i, "is good"
        else:
            print i, "check fail"
        i = i + 1


def main():
    print("starting...")
    inputfile = open('project.pbxproj')
    contenu = inputfile.read()
    tab = contenu.split("};")
    tabbuilds = puttabintab(tab)
    tabbuilds = formattab(tabbuilds)
    showdiff(tabbuilds)
    inputfile.close()


if __name__ == "__main__":
    main()
