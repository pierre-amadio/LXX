#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Odes miss some verses that confuses reader.
Lets fill in empty verses where there are one.

Then some title should be moved from a verse node to the parent chapter node.

arg1:  main book of joshua (07.JoshB.xml) variant bookq
arg2:  version A (08.JoshA.xml) of the book of joshua starting at  15:21
arg3: destination folder
"""
import sys
import re
from bs4 import BeautifulSoup
import copy

joshBFile=sys.argv[1]
joshAFile=sys.argv[2]
outputDir=sys.argv[3]


#m=re.search(".*\/(\S+)$",inputFile)
#if m:
#  shortName=m.group(1)
#else:
#  shortName=inputFile
#
#print(shortName)

def addVariant(xml,subType):
  """
  <verse osisID="Josh.1.1"><seg type="x-variant" subType="x-1">
  """
  out=""
  s= BeautifulSoup(xml,'xml')
  for verse in s.find_all("verse"):
    print("##\n",verse)
    seg=s.new_tag("seg", type="x-variant", subtype="%s"%subType)
    print(seg)
    verse.insert_before(seg)
    newV=verse.extract()
    seg.append(newV)
  return str(s)

def Josh(xmlB,xmlA):
  for chapter in soupA.find_all('chapter'):
    print(chapter["osisID"])
    m=re.search("JoshA\.(\d+)",chapter["osisID"])
    curChapter=0
    if m:
      curChapter=m.group(1)
    else:
      print("Cannot parse chatper %s"%joshB["osisID"])
      sys.exiit()
    print(curChapter)





  out=str(soupB)
  return out

newFile="%s/%s"%(outputDir,"06-Josh.xml")
#allVersesXml=missingVersesFromFile(inputFile)
#newXml=moveTitle(allVersesXml)
soupA=False
soupB=False

with open(joshAFile) as joshA:
  soupA= BeautifulSoup(joshA,'xml')
  joshA.close()

with open(joshBFile) as joshB:
  soupB= BeautifulSoup(joshB,'xml')
  joshB.close()

xmlB=addVariant(str(soupB),"x-1")
print(xmlB)
#with open(newFile, "w", encoding='utf-8') as file:
#  file.write(newXml)
#  print(newFile)


