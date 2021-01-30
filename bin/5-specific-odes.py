#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Odes miss some verses that confuses reader.
Lets fill in empty verses where there are one.

Then some title should be moved from a verse node to the parent chapter node.

arg1:  input file
arg2:  output directory
"""
import sys
import re
from bs4 import BeautifulSoup

inputFile=sys.argv[1]
outputDir=sys.argv[2]


def missingVersesFromFile(fileName):
  with open(fileName) as fp:
    soup = BeautifulSoup(fp, 'xml')

    curChapter=0
    for chapter in soup.find_all('chapter'):
      curVerseNbr=0
      rc=re.search("Odes\.(\d+)",chapter["osisID"])
      if rc:
        curChapter=int(rc.group(1))
      else:
        print("Cannot parse chapter %s"%chapter["osisID"])
        sys.exit()

      for verse in chapter.find_all("verse"):
        expectedVerseNbr=curVerseNbr+1
        snt="Odes.%s.(\d+)"%curChapter
        rv=re.search(snt,verse["osisID"])
        if rv:
          curVerseNbr=int(rv.group(1))
        else:
          print("Cannot parse verse %s"%verse)
          sys.exit()

        if curVerseNbr!=expectedVerseNbr:
            for missing in range (expectedVerseNbr,curVerseNbr):
              newVerseTag=soup.new_tag("verse", osisID="Odes.%s.%s"%(curChapter,missing))
              newVerseTag.string=" "
              verse.insert_before(newVerseTag)
  return str(soup)

def moveTitle(origXml):
  soup = BeautifulSoup(origXml, 'xml')
  curChapter=0
  for title in soup.find_all('title'):
    verse=title.parent
    chapter=verse.parent
    cur=title.extract()
    chapter.insert(0,title)

  return str(soup)

newFile="%s/%s"%(outputDir,"57-Odes.xml")
allVersesXml=missingVersesFromFile(inputFile)
newXml=moveTitle(allVersesXml)

print("Dealing with Odes")
with open(newFile, "w", encoding='utf-8') as file:
  file.write(newXml)


