#!/usr/bin/env python3 
# -*- coding: utf-8 -*-
"""
Some verses index contained alphanumerical values such as '1Kgs 2:46a' '1Kgs 2:46b'
The sword module concanete all those in a single verse.
Let's put some marker to show there is supposed to be different verses there.
https://wiki.crosswire.org/OSIS_Bibles#Marking_Pilcrows

first argument: input (single) file
second argument: output directory
"""
import re
import sys
from bs4 import BeautifulSoup

inputFile=sys.argv[1]
outputDir=sys.argv[2]

def deconc(myFile):
  with open(myFile) as fp:
    soup = BeautifulSoup(fp,'xml')
    for verse in soup.find_all('verse'):
      concFlag=re.match("(.*\d+)\D+$",verse["osisID"])
      if concFlag:
        pilcrows=soup.new_tag("milestone",type="x-p",marker="¶")
        verse.insert(0,pilcrows)
        """
        Also, let rename the verse without the alphabetical suffix as it generate
        funny behaviour in Sword: the last verse is doubled.
        """
        verse["osisID"]=concFlag.group(1)

    return str(soup)


newXml=deconc(inputFile)

m=re.search(".*\/(\S+)$",inputFile)
shortName=None
if m:
  shortName=m.group(1)
else:
  shortName=inputFile

newFile="%s/%s"%(outputDir,shortName)

print("Dealing with concatenated verses in %s"%shortName)
with open(newFile,"w",encoding="utf-8") as file:
  file.write(newXml)

