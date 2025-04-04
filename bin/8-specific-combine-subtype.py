#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Combine two book from different sources (such as JoshA and JoshB) in a single book.
arg1:  main book of joshua (07.JoshB.xml) variant book subType x-1
arg2:  version A (08.JoshA.xml) of the book of joshua starting at  15:21 subType x-2
arg3: destination folder
"""
import sys
import re
from bs4 import BeautifulSoup
import copy

bookInd={}
bookInd["Josh"]="06"
bookInd["Judg"]="07"
bookInd["Tob"]="20"
bookInd["Sus"]="53"
bookInd["Dan"]="54"
bookInd["Bel"]="55"

BFile=sys.argv[1]
AFile=sys.argv[2]
outputDir=sys.argv[3]

def getBookName(xml):
  """
    return the name of the book
  """
  out=""
  chapter=xml.find("chapter")
  m=re.search("(\S+)\.\d+",chapter["osisID"])
  if m:
   out=m.group(1)
  else:
    print("Cannot find book name in %s"%chapter["osisID"])
    sys.exit()
  return out

def addVariant(xml,subType):
  """
  wrap the contnt of verses in some <seg> nodes:
  <verse osisID="Josh.1.1"><seg type="x-variant" subType="x-1">blabla</verse></seg>
  """
  for verse in xml.find_all("verse"):
    # for l in verse.children:
    #   print("c='%s'"%l)
    copyVerse=copy.copy(verse)
    origContent=copyVerse.children
    verse.clear()
    #print("clear->",verse)
    seg=xml.new_tag("seg", type="x-variant", subType="%s"%subType)
    verse.append(seg)
    for c in copyVerse.children:
      seg.append(copy.copy(c))
  return xml

def combine(xmlB,xmlA,bookName):
  for chapter in xmlA.find_all('chapter'):
    m=re.search("%s\.(\d+)"%bookName,chapter["osisID"])
    curChapter=0
    if m:
      curChapter=m.group(1)
    else:
      print("Cannot parse chapter %s"%chapter["osisID"])
      sys.exit()
    for verse in chapter.find_all("verse"):
      chapterB=xmlB.find('chapter',attrs={"osisID":chapter["osisID"]})
      chapterB.append(verse)
  
  out=str(soupB)
  return out

soupA=False
soupB=False

print("Mixing '%s' and '%s'"%(BFile,AFile))

with open(AFile) as A:
  soupA= BeautifulSoup(A,'xml')
  A.close()

with open(BFile) as B:
  soupB= BeautifulSoup(B,'xml')
  B.close()

bookName=getBookName(soupA)


newFile="%s/%s"%(outputDir,"%s-%s.xml")%(bookInd[bookName],bookName)
xmlB=addVariant(soupB,"x-1")
xmlA=addVariant(soupA,"x-2")
result=combine(xmlB,xmlA,bookName)
with open(newFile, "w", encoding='utf-8') as file:
  file.write(result)


