#!/usr/bin/env python3 
# -*- coding: utf-8 -*-
# Trying to fill the gap in the LXX strong entry.
"""
This script takes an LXX osis xml file, and try to replace the missing strong id based on the 
content of the old Sword LXX module and on a flat file dictionnary.

first argument: input (single) file
second argument: output directory
"""
import unicodedata
import re
import sys
from bs4 import BeautifulSoup
import Sword
import copy

markup=Sword.MarkupFilterMgr(Sword.FMT_OSIS)
markup.thisown=False
mgr = Sword.SWMgr(markup)
mod=mgr.getModule("LXX")
if not mod:
    print("No module")
    sys.exit()
versification=mod.getConfigEntry("Versification")
mgr.setGlobalOption("Greek Accents", "Off")
mgr.setGlobalOption("Strong's Numbers", "On")

def get_verse(bookStr,chapterInt,verseNbr,moduleName,outputType=Sword.FMT_PLAIN):
    """
        Return a verse from the Sword engine.
    """
    vk=Sword.VerseKey()
    vk.setVersificationSystem(versification)
    #vk.setTestament() ??
    vk.setBookName(bookStr)
    vk.setChapter(chapterInt)
    vk.setVerse(verseNbr)
    mod.setKey(vk)
    return mod.renderText()

#From https://stackoverflow.com/questions/517923/what-is-the-best-way-to-remove-accents-normalize-in-a-python-unicode-string
def strip_accents(s):
   return ''.join(c for c in unicodedata.normalize('NFD', s)
                     if unicodedata.category(c) != 'Mn')

def findStrongIdFor(osisId,fullWord):
    """
        Try to find what is the correct strong number for fullWord by looking in the Sword engine for verse OsisId
        to see if it is set there.
        Return the strong number if it find it, 0 otherwise.
    """
    #print("What is the strong id for %s / %s"%(osisId,fullWord))
    m=re.match("(\S+)\.(\d+)\.(\d+)",osisId)
    swordVerse=""
    if m:
        bookAbr=m.group(1)
        chaptNbr=int(m.group(2))
        verseNbr=int(m.group(3))
        swordVerse=get_verse(bookAbr,chaptNbr,verseNbr,"LXX",outputType=Sword.FMT_OSIS).getRawData()
    else:
        print("Cannot parse osisId %s"%osisId)
        sys.exit()

    soup=BeautifulSoup(swordVerse,features="html.parser")
    for w in soup.find_all("w"):
        candidateWord=w.contents[0]
        if not w.get("lemma"):
          #print("no lemma for %s"%w)
          return 0
        candidateLemma=w["lemma"]
        m=re.match("strong:G(\d+)",candidateLemma)
        candidateStrong=0
        if m:
            candidateStrong=m.group(1)
        else:
            #print("Warning: cannot parse lemma %s"%candidateLemma)
            continue
        #print(candidateWord,candidateStrong)
        noAccent=strip_accents(fullWord)
        if(noAccent==candidateWord):
            return candidateStrong
    #print("No match found....")
    return(0)

def parseLXX(fileName):
    strongDic={}
    with open("codesStrong.strong") as fp:
      for line in fp:
        #print(line)
        m=re.search("(\d+)#(.+)",line)
        if m:
          #print("%s -> %s"%(m.group(1),m.group(2)))
          strongDic[m.group(2)]=m.group(1)
        else:
          print("Cannot parse strongDic : '%s'"%line)
          sys.exit()

    with open(fileName) as fp:
        soup = BeautifulSoup(fp, features='xml')
        #soup = BeautifulSoup(fp, 'html.parser')
        for link in soup.find_all('w'):
            lemma=link["lemma"]
            #print(link)
            fullWord=link.contents[0]
            parentVerse=link.find_parent("verse")
            if not parentVerse:
                #Some chapter title have w node but no actual verse id.
                #We ignore those.
                #print("no parent verse")
                continue
            try:
                osisId=parentVerse["osisID"]
            except:
                print( "Problem with ")
                print(link)
                print("_____ PARENTVERSE")
                print(parentVerse)
                print("_____________ PARENT:)")
                print(link.parent)
                sys.exit()
            lxxStrongId=findStrongIdFor(osisId,fullWord) 
            dicStrongId=0


            targetLex=False
            if not "," in link["lemma"]:
              targetLex=link["lemma"]

            if targetLex in strongDic:
              dicStrongId=strongDic[targetLex]


            #print(link)
            finalNbr=lxxStrongId
            if dicStrongId!=lxxStrongId:
              """
                This may happen for entry such as Gen1.8
                Strong entry differ for εἶδεν (old:1492 flatfile:3708)
                1492: οἶδα
                3708: ὁράω (The aorist form (eidon), is discussed at 1492 /eídō, "see.)

                If the old value is not equal to zeron let s use it.
                (because the lex does not contain any information about the thense, wich is used in some strong entry such as this one 1492/3708)
              """
              #print("Strong entry differ for %s (old:%s flatfile:%s) in %s"%(fullWord,lxxStrongId,dicStrongId,parentVerse["osisID"]))
              if lxxStrongId==0:
                finalNbr=dicStrongId
              else:
                finalNbr=lxxStrongId


            lex=copy.copy(link["lemma"]).replace(" ","")
            newLemma=False
            if int(finalNbr):
              #newLemma='strong:G%s lex:%s'%(finalNbr,lex)
              newLemma='strong:G%s'%(finalNbr)
            else:
              #newLemma='lex:%s'%lex
              del(link["lemma"])
            if newLemma:
              link["lemma"]=newLemma

        out=str(soup)
        return out



inputFile=sys.argv[1]
outputDir=sys.argv[2]


m=re.search(".*\/(\S+)$",inputFile)
if m:
  shortName=m.group(1)
else:
  shortName=inputFile

print("Dealing with strong number in '%s'"%shortName)

newFile="%s/%s"%(outputDir,shortName)
new=parseLXX(inputFile)
with open(newFile, "w", encoding='utf-8') as file:
    file.write(new)

