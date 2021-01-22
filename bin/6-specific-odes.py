#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Odes miss some verses that confuses reader.
Lets fill in empty verses where there are one.

arg1:  input file
arg2:  output directory
"""
import sys
import re
from bs4 import BeautifulSoup

inputFile=sys.argv[1]
outputDir=sys.argv[2]


m=re.search(".*\/(\S+)$",inputFile)
if m:
  shortName=m.group(1)
else:
  shortName=inputFile

print(shortName)

def parseFile(fileName):
  print("parsing",fileName)
  with open(fileName) as fp:
    soup = BeautifulSoup(fp, 'html.parser')
    for link in soup.find_all('w'):
      print(link)
  out="plop"
  return out

newFile="%s/%s"%(outputDir,shortName)
new=parseFile(inputFile)
with open(newFile, "w", encoding='utf-8') as file:
  file.write(new)
  print(newFile)


