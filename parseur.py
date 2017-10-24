#!/usr/bin/python2.7

import os

def findstring(tab, str):
	i = 0
	while ((str not in tab[i]) and (i < len(tab) - 1)):
		i = i + 1
	if (i == len(tab) - 1):
		return None
	return (tab[i])

def puttabintab(tab):
	tabbuilds = []
	str = findstring(tab, "94026BDD15E24582001BBF61 /* Resources */ =")
	if (str is not None):
		tabbuilds.append(str)
		print(tabbuilds[0])
	return tabbuilds

def printtab(tab):
	i = 0
	while (i < len(tab) - 1):
		print(tab[0])
		i = i + 1

def main():
	print("starting...")
	inputfile = open('project.pbxproj')
	contenu = inputfile.read()
	tab = contenu.split("};")
	tabbuilds = puttabintab(tab)
	printtab(tabbuilds)
	inputfile.close()


if __name__ == "__main__":
	main()