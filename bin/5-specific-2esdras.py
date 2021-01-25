#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Splitting 2Esdr so it match include/canon_lxx.h
{"I Esdras", "1Esd", "1Esd", 9},
{"Ezra", "Ezra", "Ezra", 10},
{"Nehemiah", "Neh", "Neh", 13},

1Esdr         -> 15-1Esd
2Esdr-> 1-9   -> 16-Ezra
2Esdr-> 10-23 -> 17-Neh
"""
import sys
import re
from bs4 import BeautifulSoup
import copy

inputFile=sys.argv[1]
outputDir=sys.argv[2]


def splitEsdr(myFile):
  with open(myFile) as fp:
    soup = BeautifulSoup(fp, 'xml')
    #for title in soup.find_all('title'):
    #  """
    #    there is supposed to be only 1 title:
    #    <chapter osisID="Dan.5"><verse osisID="Dan.5.1"><seg subType="x-1" type="x-variant"><title type="chapter">
    #  """
    #  chapter=title.parent.parent.parent
    #  newTitle=title.extract()
    #  chapter.insert(0,newTitle)
    #return str(soup)
    


  return ("a","b")


print("Dealing with 2Esdr")

#newFile="%s/%s"%(outputDir,"54-Dan.xml")
ezra=False
neh=False

with open(inputFile) as fp:
  soup = BeautifulSoup(fp, 'xml')
  ezra=copy.copy(soup)
  neh=copy.copy(soup)
  fp.close()


#2Esdr-> 1-9   -> 16-Ezra
ezra.div["osisID"]="Ezra"
for chapter in ezra.find_all("chapter"):
  print("chapter",chapter["osisID"])
  m=re.search("2Esdr\.(\d+)",chapter["osisID"])
  if m:
    print(m.group(1))
  else:
    print("Cannot parse %s"%chapter["osisID"])
    sys.exit()
  chapterNbr=m.group(1)
  chapter["osisID"]="Ezra.%s"%chapterNbr
  if int(chapterNbr)>9:
    chapter.decompose()
  else:
    for verse in chapter.find_all("verse"):
      print("verse",verse["osisID"])
      v=re.search("2Esdr\.%s\.(\d+)"%chapterNbr,verse["osisID"])
      if v:
        verse["osisID"]="Ezra.%s.%s"%(chapterNbr,v.group(1))
        print("become",verse["osisID"])
      else:
        print("Cannot parse %s"%verse["osisID"])
        sys.exit()

print(ezra)

#with open(newFile, "w", encoding='utf-8') as file:
#  file.write(newXml)
#  print(newFile)


