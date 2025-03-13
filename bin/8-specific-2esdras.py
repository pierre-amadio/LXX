#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Splitting 2Esdr so it match include/canon_lxx.h
{"I Esdras", "1Esd", "1Esd", 9},
{"Ezra", "Ezra", "Ezra", 10},
{"Nehemiah", "Neh", "Neh", 13},

1Esdr         -> 15-1Esd
2Esdr-> 1-10  -> 16-Ezra
2Esdr-> 11-23 -> 17-Neh
"""
import sys
import re
from bs4 import BeautifulSoup
import copy

inputFile=sys.argv[1]
outputDir=sys.argv[2]

print("Dealing with 2Esdr")
ezra=False
ezraF="%s/16-Ezra.xml"%outputDir

neh=False
nehF="%s/17-Neh.xml"%outputDir

with open(inputFile) as fp:
  soup = BeautifulSoup(fp, 'xml')
  ezra=copy.copy(soup)
  neh=copy.copy(soup)
  fp.close()


#2Esdr-> 1-10  -> 16-Ezra
ezra.div["osisID"]="Ezra"
for chapter in ezra.find_all("chapter"):
  m=re.search("2Esdr\.(\d+)",chapter["osisID"])
  if not m:
    print("Cannot parse %s"%chapter["osisID"])
    sys.exit()
  chapterNbr=m.group(1)
  chapter["osisID"]="Ezra.%s"%chapterNbr
  if int(chapterNbr)>10:
    chapter.decompose()
  else:
    for verse in chapter.find_all("verse"):
      v=re.search("2Esdr\.%s\.(\d+)"%chapterNbr,verse["osisID"])
      if v:
        verse["osisID"]="Ezra.%s.%s"%(chapterNbr,v.group(1))
      else:
        print("Cannot parse %s"%verse["osisID"])
        sys.exit()


#2Esdr-> 11-23 -> 17-Neh
neh.div["osisID"]="Neh"
for chapter in neh.find_all("chapter"): 
  m=re.search("2Esdr\.(\d+)",chapter["osisID"])
  if not m:
    print("Cannot parse %s"%chapter["osisID"])
    sys.exit()
  origChapterNbr=int(m.group(1))
  if origChapterNbr<=10:
    chapter.decompose()
    continue
  chapterNbr=origChapterNbr-10
  chapter["osisID"]="Neh.%s"%chapterNbr
  for verse in chapter.find_all("verse"):
    v=re.search("2Esdr\.%s\.(\d+)"%origChapterNbr,verse["osisID"])
    if v:
      verse["osisID"]="Neh.%s.%s"%(chapterNbr,v.group(1))
    else:
      print("Cannot parse %s"%verse["osisID"])
      sys.exit()

with open(nehF,"w",encoding='utf-8') as file:
  file.write(str(neh))
  file.close()

with open(ezraF,"w",encoding='utf-8') as file:
  file.write(str(ezra))
  file.close()


