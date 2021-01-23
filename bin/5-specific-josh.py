#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Combine JoshA and JoshB in a single book.
arg1:  main book of joshua (07.JoshB.xml) variant book subType x-1
arg2:  version A (08.JoshA.xml) of the book of joshua starting at  15:21 subType x-2
arg3: destination folder
"""
import sys
import re
from bs4 import BeautifulSoup
import copy

joshBFile=sys.argv[1]
joshAFile=sys.argv[2]
outputDir=sys.argv[3]


def addVariant(xml,subType):
  """
  wrap the verses in xml in some <seg> nodes:
  <verse osisID="Josh.1.1"><seg type="x-variant" subType="x-1">blabla</verse></seg>
  """
  for verse in xml.find_all("verse"):
    seg=xml.new_tag("seg", type="x-variant", subtype="%s"%subType)
    verse.insert_before(seg)
    newV=verse.extract()
    seg.append(newV)
  return xml

def josh(xmlB,xmlA):
  for chapter in xmlA.find_all('chapter'):
    #print(chapter["osisID"])
    m=re.search("Josh\.(\d+)",chapter["osisID"])
    curChapter=0
    if m:
      curChapter=m.group(1)
    else:
      print("Cannot parse chatper %s"%josh["osisID"])
      sys.exit()
    #print(curChapter)
    for seg in chapter.find_all("seg"):
      #print("seg=",seg)
      chapterB=xmlB.find('chapter',attrs={"osisID":chapter["osisID"]})
      #print("chapterB",chapterB["osisID"] )
      chapterB.append(seg)
  
  out=str(soupB)
  return out

newFile="%s/%s"%(outputDir,"06-Josh.xml")
soupA=False
soupB=False

with open(joshAFile) as joshA:
  soupA= BeautifulSoup(joshA,'xml')
  joshA.close()

with open(joshBFile) as joshB:
  soupB= BeautifulSoup(joshB,'xml')
  joshB.close()

xmlB=addVariant(soupB,"x-1")
xmlA=addVariant(soupA,"x-2")
result=josh(xmlB,xmlA)
with open(newFile, "w", encoding='utf-8') as file:
  file.write(result)
print(newFile)

