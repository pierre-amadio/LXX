#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Some books miss some verses that confuses reader.
Lets fill in empty verses where there are one.


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
              newVerseTag.string=" "
              verse.insert_before(newVerseTag)
  return str(soup)


print("Dealing with %s"%inputFile)
newFile="%s/%s"%(outputDir,inputFile)
allVersesXml=missingVersesFromFile("xml0/%s"%inputFile)

with open(newFile, "w", encoding='utf-8') as file:
  file.write(allVersesXml)

