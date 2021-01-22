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


m=re.search(".*\/(\S+)$",inputFile)
if m:
  shortName=m.group(1)
else:
  shortName=inputFile

print(shortName)

def missingVersesFromFile(fileName):
  print("parsing",fileName)
  with open(fileName) as fp:
    soup = BeautifulSoup(fp, 'xml')

    curChapter=0
    for chapter in soup.find_all('chapter'):
      curVerseNbr=0
      rc=re.search("Od\.(\d+)",chapter["osisID"])
      if rc:
        curChapter=int(rc.group(1))
      else:
        print("Cannot parse chapter %s"%chapter["osisID"])
        sys.exit()

      for verse in chapter.find_all("verse"):
        expectedVerseNbr=curVerseNbr+1
        snt="Od.%s.(\d+)"%curChapter
        rv=re.search(snt,verse["osisID"])
        if rv:
          curVerseNbr=int(rv.group(1))
        else:
          print("Cannot parse verse %s"%verse)
          sys.exit()

        if curVerseNbr!=expectedVerseNbr:
            for missing in range (expectedVerseNbr,curVerseNbr):
              newVerseTag=soup.new_tag("verse", osisID="Od.%s.%s"%(curChapter,missing))
              newVerseTag.string=" "
              verse.insert_before(newVerseTag)
  return str(soup)

newFile="%s/%s"%(outputDir,shortName)
allVersesXml=missingVersesFromFile(inputFile)
newXml=allVersesXml

with open(newFile, "w", encoding='utf-8') as file:
  file.write(newXml)
  print(newFile)


