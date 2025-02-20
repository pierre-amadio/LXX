#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Some title should be moved from a verse node to the parent chapter node.

arg1:  input file
arg2:  output directory
"""
import sys
import re
from bs4 import BeautifulSoup

inputFile=sys.argv[1]
outputDir=sys.argv[2]

def moveTitle(fileName):
  with open(fileName) as fp:
    soup = BeautifulSoup(fp, 'xml')
    curChapter=0
    for title in soup.find_all('title'):
      verse=title.parent
      chapter=verse.parent
      cur=title.extract()
      chapter.insert(0,title)

    return str(soup)

newFile="%s/%s"%(outputDir,"57-Odes.xml")
newXml=moveTitle(inputFile)

print("Dealing with Odes")
with open(newFile, "w", encoding='utf-8') as file:
  file.write(newXml)


