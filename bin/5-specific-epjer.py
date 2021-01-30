#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
EpJer has a chapter (1) title located in verse 1.
It must be placed under the chapter node directly
arg1:  input file
arg2:  output directory
"""
import sys
import re
from bs4 import BeautifulSoup
import copy

inputFile=sys.argv[1]
outputDir=sys.argv[2]


def dealWith(myFile):
  with open(myFile) as fp:
    soup = BeautifulSoup(fp, 'xml')
    for title in soup.find_all('title'):
      """
        there should be only 1 title.
      """
      chapter=title.parent.parent
      newTitle=title.extract()
      chapter.insert(0,newTitle)
  return str(soup)

print("Dealing with Prolog of EpJer")

newFile="%s/%s"%(outputDir,"50-EpJer.xml")

newXml=dealWith(inputFile)


with open(newFile, "w", encoding='utf-8') as file:
  file.write(newXml)


