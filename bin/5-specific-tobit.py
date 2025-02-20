#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tob.9.3-4 -> Tob.9.4 (subType x-2)
Tob.14.8-9 -> Tob.14.8 (subType x-2)
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
        if(verse["osisID"]=="Tob.9.3-4"):
            verse["osisID"]="Tob.9.4"
        if(verse["osisID"]=="Tob.14.8-9"):
            verse["osisID"]="Tob.14.8"
    return str(soup)


print("Dealing with Tobit verses")

newFile="%s/%s"%(outputDir,"20-Tob.xml")

newXml=fixIt(inputFile)


with open(newFile, "w", encoding='utf-8') as file:
  file.write(newXml)


