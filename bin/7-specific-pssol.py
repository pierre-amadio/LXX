#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PssSol has a chapter's  title located in verse 1 for several psalms.
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
      chapter=title.parent.parent
      newTitle=title.extract()
      chapter.insert(0,newTitle)
  return str(soup)

print("Dealing with Ps Sol")

newFile="%s/%s"%(outputDir,"33-PssSol.xml")

newXml=dealWith(inputFile)


with open(newFile, "w", encoding='utf-8') as file:
  file.write(newXml)


