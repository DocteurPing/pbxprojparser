#!/usr/bin/python2.7

import os

def findstring(tab, str):
	i = 0
	while ((str not in tab[i]) and (i < len(tab) - 1)):
		i = i + 1
	if (i == len(tab) - 1):
		return None
	return (tab[i])


def main():
	print("starting...")
	inputfile = open('project.pbxproj')
	contenu = inputfile.read()
	tab = contenu.split("};")
	str = findstring(tab, "xxxxxxxxxxxxxxxxxxxxx");
	if (str is not None):
		print(str)
	inputfile.close()


if __name__ == "__main__":
	main()