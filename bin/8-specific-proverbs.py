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

let's rename chapter 32 to 36 as 25 to 29


arg1:  input file
arg2:  output directory
"""
import sys
import re
from bs4 import BeautifulSoup

inputFile=sys.argv[1]
outputDir=sys.argv[2]

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


soup=None
with open(inputFile) as fp:
  soup = BeautifulSoup(fp, 'xml')
 
newFile="%s/%s"%(outputDir,"27-Prov.xml")

for chNbr in range(1,6):
  moveChapter(soup,31+chNbr,24+chNbr)
 
output=str(soup)

print("Dealing with Proverbs")
with open(newFile, "w", encoding='utf-8') as file:
  file.write(output)


