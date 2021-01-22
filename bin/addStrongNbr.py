#!/usr/bin/env python3 
# -*- coding: utf-8 -*-
# Trying to fill the gap in the LXX strong entry.
"""
This script takes an LXX osis xml file, and try to replace the missing strong id based on the 
content of the old Sword LXX module and on a flat file dictionnary.

TODO: gen 1.7 
<w lemma="χωρίζω, δια" morph="packard:VAI AAI3S" xlit="betacode:DIEXW/RISEN">διεχώρισεν</w>
should there be lex entry ? if so, one or two ?
in previous osis:
<w lemma="strong:G0,G0 lex:χωρίζω,δια" morph="packard:VAI+AAI3S" xlit="betacode:DIEXW/RISEN">διεχώρισεν</w>


"""
import unicodedata
import re
import sys
from bs4 import BeautifulSoup
import Sword

def get_verse(bookStr,chapterInt,verseNbr,moduleName,outputType=Sword.FMT_PLAIN):
    """
        Return a verse from the Sword engine.
    """
    markup=Sword.MarkupFilterMgr(outputType)
    markup.thisown=False
    mgr = Sword.SWMgr(markup)

    mod=mgr.getModule(moduleName)
    versification=mod.getConfigEntry("Versification")
    vk=Sword.VerseKey()
    vk.setVersificationSystem(versification)
    #vk.setTestament() ??
    vk.setBookName(bookStr)
    vk.setChapter(chapterInt)
    vk.setVerse(verseNbr)
    mod.setKey(vk)
    #mgr.setGlobalOption("Hebrew Vowel Points", "On")
    mgr.setGlobalOption("Greek Accents", "Off")
    mgr.setGlobalOption("Strong's Numbers", "On")
    #mgr.setGlobalOption("Hebrew Cantillation", "Off")
    if not mod:
        print("No module")
        sys.exit()
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
    print("Let s parse some xml")

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
        soup = BeautifulSoup(fp, 'html.parser')
        for link in soup.find_all('w'):
            lemma=link["lemma"]
            fullWord=link.contents[0]
            parentVerse=link.find_parent("verse")
            if not parentVerse:
                #Some chapter title have w node but no actual verse id.
                #We ignore those.
                print("no parent verse")
                continue
            try:
                osisId=parentVerse["osisid"]
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

            if fullWord in strongDic:
              dicStrongId=strongDic[fullWord]
              if dicStrongId!=lxxStrongId:
                """
                  This may happen for entry such as Gen1.2 τοῦ
                  Old module:3588
                  codesStrong.strong: 5120
                  by default, let s use the old module value, but still print a warning.
                """
                print("Strong entry differ for %s in %s"%(fullWord,parentVerse["osisid"]))
                print("Old module:%s"%lxxStrongId)
                print("codesStrong.strong: %s\n"%dicStrongId)
                dicStrongId=lxxStrongId

            finalNbr=0
            if dicStrongId:
              finalNbr=dicStrongId
            if lxxStrongId:
              finalNbr=lxxStrongId

            #newLemma=lemma.replace(r.group(1),"strong:G%s"%strongId)
            #link["lemma"]=newLemma
            #print(link)
            #print(lemma)
            if finalNbr:
              newLemma='strong:G%s lex:%s'%(finalNbr,lemma)
              #print(lemma)
              #print(newLemma)
              link["lemma"]=newLemma
              #print(link)
        #out=soup.prettify()
        out=str(soup)
        return out


#Where to write the modified output:
newFile="./test.xml"

inputFile=sys.argv[1]

new=parseLXX(inputFile)
with open(newFile, "w", encoding='utf-8') as file:
    file.write(new)
