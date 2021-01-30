#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Daniel 5 has a title currently included with the <chapter><verse><seg> tag.
It should be moved just below the chapter tag.
arg1:  input file
arg2:  output directory
"""
import sys
import re
from bs4 import BeautifulSoup

inputFile=sys.argv[1]
outputDir=sys.argv[2]


def moveTitle(myFile):
  with open(myFile) as fp:
    soup = BeautifulSoup(fp, 'xml')
    for title in soup.find_all('title'):
      """
        there is supposed to be only 1 title:
        <chapter osisID="Dan.5"><verse osisID="Dan.5.1"><seg subType="x-1" type="x-variant"><title type="chapter">
      """
      chapter=title.parent.parent.parent
      newTitle=title.extract()
      chapter.insert(0,newTitle)
    return str(soup)


print("Dealing with Daniel's title")

newFile="%s/%s"%(outputDir,"54-Dan.xml")

newXml=moveTitle(inputFile)


with open(newFile, "w", encoding='utf-8') as file:
  file.write(newXml)


