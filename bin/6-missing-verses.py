#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Some books miss some verses that confuses reader.
Just putting an empty verse nodes is not enough for some frontends
which require some content in order for the verse to be selectable.
Let's fill those missing verse with an empty <seg> node.

arg1:  input file
arg2:  output directory
"""
import sys
import re
import copy
from bs4 import BeautifulSoup
import Sword

inputFile=sys.argv[1]
outputDir=sys.argv[2]

markup=Sword.MarkupFilterMgr(Sword.FMT_OSIS)
markup.thisown=False
mgr = Sword.SWMgr(markup)
mod=mgr.getModule("LXX")
if not mod:
    print("No sword LXX module found.")
    sys.exit()
versification=mod.getConfigEntry("Versification")

def getVerseMax(moduleName,bookName,chapterNbr):
    vk=Sword.VerseKey()
    vk.setVersificationSystem(versification)
    vk.setBookName(bookName)
    vk.setChapter(chapterNbr)
    return vk.getVerseMax()

def missingVersesFromFile(fileName):
  with open(fileName) as fp:
    soup = BeautifulSoup(fp, 'xml')
    filling=soup.new_tag('seg')

    curChapter=0
    bookName=None
    for b in soup.find_all("div",type="book"):
      bookName=b["osisID"]

    if bookName==None:
      sys.exit("Cannot find book name")
    for chapter in soup.find_all('chapter'):
      curVerseNbr=0
      rc=re.search("%s\.(\d+)"%bookName,chapter["osisID"])
      if rc:
        curChapter=int(rc.group(1))
      else:
        print("Cannot parse chapter %s"%chapter["osisID"])
        sys.exit()

      for verse in chapter.find_all("verse"):
        expectedVerseNbr=curVerseNbr+1
        snt="%s.%s.(\d+)"%(bookName,curChapter)
        rv=re.search(snt,verse["osisID"])
        if rv:
          curVerseNbr=int(rv.group(1))
        else:
          print("Cannot parse verse %s"%verse)
          sys.exit()


        if curVerseNbr!=expectedVerseNbr:
            for missing in range (expectedVerseNbr,curVerseNbr):
              newVerseTag=soup.new_tag("verse", osisID="%s.%s.%s"%(bookName,curChapter,missing))
              newVerseTag.append(copy.copy(filling))
              verse.insert_before(newVerseTag)
      
      swordMaxVn=getVerseMax("LXX",bookName,curChapter)

      if curVerseNbr!=swordMaxVn:
        """
        print("ending %s chapter %s with verse %s"%(bookName,curChapter,curVerseNbr))
        print("should be %s"%swordMaxVn)
        """
        for missing in range (curVerseNbr+1,swordMaxVn+1):
          newVerseTag=soup.new_tag("verse", osisID="%s.%s.%s"%(bookName,curChapter,missing))
          newVerseTag.append(copy.copy(filling))
          chapter.append(newVerseTag)
      
  return str(soup)

print("Dealing with missing verses in %s"%inputFile)
newFile="%s/%s"%(outputDir,inputFile)
allVersesXml=missingVersesFromFile("xml-sorted/%s"%inputFile)

with open(newFile, "w", encoding='utf-8') as file:
  file.write(allVersesXml)


