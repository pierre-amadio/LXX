#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
In the source text, Proverbs have no chapter 25,26,27,28,29 but has
the following set of chapters:
1-24,30-31.9,32.1-36,and then again some bits of chapter 31.10-31.31

Excerpt from "Septuaginta, a reader's edition", p334 explaining why it
is probably so:
some witnesses to the greek version of proverbs contain portion of chs
30-31 inserted within ch24 as reflected in rahlfs-hannhart.
the reason for this textual divergence remains unclear and we have
retained the versifications of the masoretic text for simplicity.

As canon_lxx has 31 chapters for proverbs,before the chapter 32-36 have been
renamed as 25,26,27,28,29 by changing the number directly in the
generated imp file. But this had side effect when dealing with empyt verses later on.
Let's deal with it at this stage instead.

First of all, getting read of the empty verses added in phase 4:

second occurence of chapter 24 node verses 1-22
second occurence of chapter 30 node verses 1-14
second occurence of chapter 31 node verses 1-9

Then let's rename chapter 32 to 36 as 25 to 29


arg1:  input file
arg2:  output directory
"""
import sys
import re
from bs4 import BeautifulSoup

inputFile=sys.argv[1]
outputDir=sys.argv[2]

def removeEmpty(fileName):
  with open(fileName) as fp:
    soup = BeautifulSoup(fp, 'xml')
    curChapter=0
    """
    Removing all verses 1-22 in the second occurence of chapter 24:
    """
    chapter=soup.find_all('chapter',osisID="Prov.24")[1]
    for verse in chapter.find_all("verse"):
      target=re.match("Prov\.24\.(\d+)",verse['osisID'])
      if not target:
        print("Problem parsing '%s'"%verse['osisID'])
        sys.exit()
      verseNbr=int(target.group(1))
      if(verseNbr>=0 and verseNbr<=22):
        verse.decompose()

    """
    Removing all verses 1-14 in the second occurence of chapter 30:
    """
    chapter=soup.find_all('chapter',osisID="Prov.30")[1]
    for verse in chapter.find_all("verse"):
      target=re.match("Prov\.30\.(\d+)",verse['osisID'])
      if not target:
        print("Problem parsing '%s'"%verse['osisID'])
        sys.exit()
      verseNbr=int(target.group(1))
      if(verseNbr>=0 and verseNbr<=14):
        verse.decompose()

    """
    Removing all verses 1-9 in the second occurence of chapter 31:
    """
    chapter=soup.find_all('chapter',osisID="Prov.31")[1]
    for verse in chapter.find_all("verse"):
      target=re.match("Prov\.31\.(\d+)",verse['osisID'])
      if not target:
        print("Problem parsing '%s'"%verse['osisID'])
        sys.exit()
      verseNbr=int(target.group(1))
      if(verseNbr>=0 and verseNbr<=9):
        verse.decompose()

    return soup

def moveChapter(xml,fro,to):
  #print("Moving chapter %s to %s"%(fro,to))
  for chapter in xml.find_all("chapter",osisID="Prov.%s"%fro):
    chapter["osisID"]="Prov.%s"%to
    for verse in chapter.find_all("verse"):
      tregsnt="Prov.%s.(\w+)"%fro
      treg=re.search(tregsnt,verse["osisID"])
      if not treg:
        print("Cannot parse '%s' with '%s'"%(verse["osisID"],tregsnt))
        sys.exit()
      curVerseNbr=treg.group(1)
      verse["osisID"]="Prov.%s.%s"%(to,curVerseNbr)

newFile="%s/%s"%(outputDir,"27-Prov.xml")
newXml=removeEmpty(inputFile)

for chNbr in range(1,6):
  moveChapter(newXml,31+chNbr,24+chNbr)
 
output=str(newXml)

print("Dealing with Proverbs")
with open(newFile, "w", encoding='utf-8') as file:
  file.write(output)


