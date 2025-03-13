#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sus.1.60-62 -> Sus.1.60 (subType x-1)
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
      if(verse["osisID"]=="Sus.1.60-62"):
        verse["osisID"]="Sus.1.60"
    return str(soup)


print("Dealing with Susanna's verses")

newFile="%s/%s"%(outputDir,"53-Sus.xml")

newXml=fixIt(inputFile)


with open(newFile, "w", encoding='utf-8') as file:
  file.write(newXml)


