#!/usr/bin/python2.7

import os

def findstring(tab, str):
	i = 0
	while ((str not in tab[i]) and i in xrange(len(tab))):
		i = i + 1
	if (i == len(tab) - 1):
		return None
	return (tab[i])

def puttabintab(tab):
	tabbuilds = []
	print("loading 1 ...")
	str = findstring(tab, "94026BDD15E24582001BBF61 /* Resources */ =")
	if (str is not None):
		print("... ok")
		print("loading 2 ...")
		tabbuilds.append(str)
	else:
		print("... fail")
	str = findstring(tab, "94026C2515E24588001BBF61 /* Resources */ =")
	if (str is not None):
		print("... ok")
		print("loading 3 ...")
		tabbuilds.append(str)
	else:
		print("... fail")
	str = findstring(tab, "94780DA213C5B3D300D2D360 /* Resources */ =")
	if (str is not None):
		print("... ok")
		print("loading 4 ...")
		tabbuilds.append(str)
	else:
		print("... fail")
	str = findstring(tab, "94780DC613C5B3D400D2D360 /* Resources */ =")
	if (str is not None):
		print("... ok")
		print("loading 5 ...")
		tabbuilds.append(str)
	else:
		print("... fail")
	str = findstring(tab, "977A83441BE7657D0068058F /* Resources */ =")
	if (str is not None):
		print("... ok")
		print("loading 6 ...")
		tabbuilds.append(str)
	else:
		print("... fail")
	str = findstring(tab, "97B876A41BE7618D00805A22 /* Resources */ =")
	if (str is not None):
		print("... ok")
		print("loading 7 ...")
		tabbuilds.append(str)
	else:
		print("... fail")
	str = findstring(tab, "97FA28F91B03560F00F31B2C /* Resources */ =")
	if (str is not None):
		print("... ok")
		tabbuilds.append(str)
	else:
		print("... fail")
	return tabbuilds

def printtab(tab):
	i = 0
	while (i < len(tab)):
		print(tab[i])
		i = i + 1

def getfiles(tab):
	splittab = tab.split(",")
	tabfiles = []
	i = 0
	while (i in xrange(len(splittab))):
		if (splittab[i].find("swift")):
			tabfiles.append(splittab[i])
		i = i + 1
	strtoreturn = ''.join(tabfiles)
	return strtoreturn


def formattab(tab):
	i = 0
	while (i in xrange(len(tab))):
		newtab = tab[i].split(";")
		tab[i] = getfiles(newtab[2])
		i = i + 1
	return tab


def showdiff(tab):
	i = 1
	while (i in xrange(len(tab))):
		if (tab[0] == tab[i]):
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
	printtab(tabbuilds)
	showdiff(tabbuilds)
	inputfile.close()


if __name__ == "__main__":
	main()