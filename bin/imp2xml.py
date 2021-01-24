#!/usr/bin/env python3
"""
This script will transfrom a set of imp files into a single book in xml format.
"""
import sys
import re
from jinja2 import Template, FileSystemLoader, Environment
file_loader = FileSystemLoader('templates')
env = Environment(loader=file_loader)
template = env.get_template('book.xml')

"""
Assuming we have a book data structure like this:
{ 'chapters': [ { 'osisId': 'Gen 1',
                  'title': 'The creation',
                  'verses': [ { 'content': 'in the beginning...',
                                'osisId': 'Gen 1:1'},
                              {'content': 'blablabla',
                                'osisId': 'Gen 1:2'}]},
                { 'osisId': 'Gen 2',
                  'verses': [ {'content': 'blablabla 21',
                               'osisId': 'Gen 2:1'},
                              { 'content': 'blablabla 22',
                                'osisId': 'Gen 2:2'}]}],
  'name': 'Genesis'}
"""

book={}
inputFiles=sys.argv[1]

book={}
book["name"]=False
book["chapters"]=[]
for curFileName in sys.argv[1:]:
  with open(curFileName) as fp:
    #newVerseFlag is true when we expect the current line to be a $$$Book Chapter:Verse sort of line 
    newVerseFlag=True
    #is this an alternate versification verse such as Exod 28:29a that requires a <milestone> node ?
    milestoneFlag=False
    curVerseNbr=0
    knownChapterNbr=0
    for line in fp:
      #let s ignore blank line.
      if re.search("^\s$",line):
        continue
      if newVerseFlag:
        """we are in a $$$bookname sort of line"""
        verseLineReg=re.search("\$\$\$(\S+)/(\d+)/(\d+)",line)
        chapterLineReg=re.search("\$\$\$(\S+)/(\d+)",line)
        sirPrologReg=re.search("\$\$\$Sir/Prolog/(\d+)",line)
        if verseLineReg:
          """we are in a book/chapter/verse definition line"""
          bookName=verseLineReg.group(1)
          curChapterNbr=int(verseLineReg.group(2))
          curVerseNbr=int(verseLineReg.group(3))
          ms=re.search("\$\$\$(\S+)/(\d+)/(\d+)([a-z]+)",line)
          if ms:
            milestoneFlag=ms.group(4)
          else:
            milestoneFlag=False
        elif sirPrologReg:
          """ we are in one of those funny Sir Prolog line: $$$Sir/Prolog/4"""
          bookName="Sir"
          curChapterNbr=1
          curVerseNbr=0
          milestoneFlag=sirPrologReg.group(1)
        elif chapterLineReg and not sirPrologReg:
          """ we are ina book/chapter (no verse) definition line """
          bookName=int(chapterLineReg.group(1))
          curChapterNbr=int(chapterLineReg.group(2))
          curVerseNbr=0
        else:
          print("Cannot parse '%s'"%line.strip())
          print("in '%s'"%curFileName)
          sys.exit()
        if not book["name"]:
          book["name"]=bookName
        newVerseFlag=False

        #are we suppose to create a new chapter ?
        needNewChapter=False
        #if there is no chapter created yes, obviously we need.
        if len(book["chapters"])==0:
          needNewChapter=True
        #if the current chapter does not match the last one we dealt with, 
        #it s a new chapter that needs to be created.
        if knownChapterNbr!=curChapterNbr:
          needNewChapter=True

        if needNewChapter:
          newChapter={}
          newChapter["osisId"]=""
          newChapter["verses"]=[]
          newChapter["osisId"]="%s.%s"%(book["name"],curChapterNbr)
          book["chapters"].append(newChapter)
          knownChapterNbr=curChapterNbr
      else:
        """We are in a text line (not a $$chapter/verse  one)"""
        newVerseFlag=True
        content=""
        if milestoneFlag:
          content='<milestone type="x-alt-v11n" n="%s"/>'%milestoneFlag
          milestoneFlag=False

        rawContent=line.strip()
        content=rawContent.replace('<title type="section" subType="x-preverse">','<title type="chapter">')
        curVerse={}
        curVerse["osisId"]="%s.%s.%s"%(book["name"],curChapterNbr,curVerseNbr)
        curVerse["content"]=content
        book["chapters"][len(book["chapters"])-1]["verses"].append(curVerse)
    fp.close()

output = template.render(book=book)
print(output)
