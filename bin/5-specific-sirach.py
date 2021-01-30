#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Prolog  verses are supposed to be milestone _before_ verse1.
<chapter osisID="Sir.1">
 <milestone type="x-alt-v11n" n="1"/>
  <w lemma="strong:G4183 lex:πολύς" morph="packard:A1+GPN" xlit="betacode:POLLW=N">πολλῶν</w>
  ...
 <milestone type="x-alt-v11n" n="2"/>
   <w lemma="strong:G2532 lex:καί" morph="packard:C" xlit="betacode:KAI\">καὶ</w>

 right now, those are set as milestones in verses Sir1:0

arg1:  input file
arg2:  output directory
"""
import sys
import re
from bs4 import BeautifulSoup
import copy

inputFile=sys.argv[1]
outputDir=sys.argv[2]


def dealWith(myFile):
  with open(myFile) as fp:
    soup = BeautifulSoup(fp, 'xml')
    insertIndex=0 
    milestoneCnt=1
    lastNewTag=False
    for verse in soup.find_all(osisID="Sir.1.0"):
      #I wonder if it may better to include the prolog before chapter 1, directly under the book <dev> ?
      chapter=verse.parent
      milestone=soup.new_tag("milestone",type="x-alt-v11n",n="%s"%milestoneCnt)
      milestoneCnt+=1
      chapter.insert(insertIndex,milestone)
      insertIndex+=1
      for c in verse.children:
        newC=copy.copy(c)
        chapter.insert(insertIndex,newC)
        insertIndex+=1
      verse.decompose()
    return str(soup)


print("Dealing with Prolog of Sirach")

newFile="%s/%s"%(outputDir,"32-Sir.xml")

newXml=dealWith(inputFile)


with open(newFile, "w", encoding='utf-8') as file:
  file.write(newXml)


