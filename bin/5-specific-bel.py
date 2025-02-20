#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Bel.1.15-17 -> Bel.1.15 (subType x-1)

arg1:  input file
arg2:  output directory
"""
import sys
import re
from bs4 import BeautifulSoup

inputFile=sys.argv[1]
outputDir=sys.argv[2]


def fixIt(myFile):
  with open(myFile) as fp:
    soup = BeautifulSoup(fp, 'xml')
    for verse in soup.find_all('verse'):
      if(verse["osisID"]=="Bel.1.15-17"):
        verse["osisID"]="Bel.1.15"
    return str(soup)


print("Dealing with Bel's verses")

newFile="%s/%s"%(outputDir,"55-Bel.xml")

newXml=fixIt(inputFile)


with open(newFile, "w", encoding='utf-8') as file:
  file.write(newXml)


