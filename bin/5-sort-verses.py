#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Somes books have funny sort order of chapters, or verses within a chapter.
By example:

Proverbs ends up with several nodes for the same chapter in this order 24,30,24,30.
Jeremiah 10 has the following verse order: 1,2,3,4,9,5

Some frontends such as Xiphos are confused when a text has missing verses, which happens.
To workaround this, non existing verses are creating containing just […].
Having chapter or verses not sorted correctly makes this process complicated.
This script takes a xml book and turn it into a well sorted book.


arg1:  input file
arg2:  output directory
"""
import sys
import re
from bs4 import BeautifulSoup
import copy

inputFile=sys.argv[1]
outputDir=sys.argv[2]

def get_verse_nbr(fullv):
  test=re.match("\w+\.\d+\.(\d+)",fullv["osisID"])
  if not test:
    print("Cannot parse %s"%fullv)
  out=int(test.group(1))
  return(out)

def sort_verses(chapter):
  vList=[]
  for curV in chapter.find_all("verse"):
    newV=copy.copy(curV)
    curV.decompose()
    vList.append(newV)
  
  vList.sort(key=get_verse_nbr)
  for v in vList:
    chapter.append(v)
  return

def combine_chapters():
  existing={}
  for chapter in soup.find_all("chapter"):
    cid=chapter["osisID"]
    if cid not in existing:
      existing[cid]=chapter
      continue
    """
      there was already a node with this chapter id, 
      lets put all its verse in the first occurence
      and delete the current chatper.
    """
    print("Need to combine %s"%cid)
    for n in chapter.children:
      newNode=copy.copy(n)
      existing[cid].append(newNode)
    chapter.decompose()

soup=None
with open("./xml0/%s"%inputFile) as fp:
  soup = BeautifulSoup(fp, 'xml')


print("Sorting content in %s"%inputFile)
newFile="%s/%s"%(outputDir,inputFile)

combine_chapters()

for chapter in soup.find_all("chapter"):
  sort_verses(chapter)


output=str(soup)
with open(newFile, "w", encoding='utf-8') as file:
  file.write(output)


