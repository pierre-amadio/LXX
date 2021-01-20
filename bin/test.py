#!/usr/bin/env python3
"""
https://zetcode.com/python/jinja/
"""
import sys
import re
from jinja2 import Template, FileSystemLoader, Environment
file_loader = FileSystemLoader('templates')
env = Environment(loader=file_loader)
template = env.get_template('book.xml')

"""
testBook={}
testBook['name']="Genesis"
testBook['chapters']=[]

ch1={}
ch1["osisId"]="Gen 1"
ch1["title"]="The creation"
ch1["verses"]=[]
ch1["verses"].append({})
ch1["verses"][0]["osisId"]="Gen 1:1"
ch1["verses"][0]["content"]="in the beginning..."
ch1["verses"].append({})
ch1["verses"][1]["osisId"]="Gen 1:2"
ch1["verses"][1]["content"]="blablabla"

ch2={}
ch2["osisId"]="Gen 2"
#ch2["title"]="The second chapter title"
ch2["verses"]=[]
ch2["verses"].append({})
ch2["verses"][0]["osisId"]="Gen 2:1"
ch2["verses"][0]["content"]="blablabla 21"
ch2["verses"].append({})
ch2["verses"][1]["osisId"]="Gen 2:2"
ch2["verses"][1]["content"]="blablabla 22"


testBook["chapters"].append(ch1)
testBook["chapters"].append(ch2)
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
    #curVerseSnt=""
    curVerseNbr=0
    knownChapterNbr=0
    for line in fp:
      #let s ignore blank line.
      if re.search("^\s$",line):
        continue
      #print("line='%s'"%line.strip())
      if newVerseFlag:
        """we are in a $$$bookname sort of line"""
        #print("line='%s'"%line.strip())
        verseLineReg=re.search("\$\$\$(\S+)/(\d+)/(\d+)",line)
        chapterLineReg=re.search("\$\$\$(\S+)/(\d+)",line)
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

        elif chapterLineReg:
          """ we are ina book/chapter (no verse) definition line """
          bookName=int(chapterLineReg.group(1))
          curChapterNbr=int(chapterLineReg.group(2))
          curVerseNbr=0
          #print(bookName,chapter)
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
          #print("line='%s'"%line.strip())
          book["chapters"].append(newChapter)
          knownChapterNbr=curChapterNbr
      else:
        """We are in a text line (not a $$chapter/verse  one)"""
        newVerseFlag=True
        content=""
        if milestoneFlag:
          #content=milestoneFlag+"\n"
          content='<milestone type="x-alt-v11n" n="%s"/>'%milestoneFlag
          milestoneFlag=False
        content+=line.strip()
        curVerse={}
        curVerse["osisId"]="%s %s:%s"%(book["name"],curChapterNbr,curVerseNbr)
        curVerse["content"]=content
        book["chapters"][len(book["chapters"])-1]["verses"].append(curVerse)
        #print(line)
    fp.close()
    #We still need to destroy the last (empty) chapter created when we hit the actual last chapter.
    #book["chapters"]=book["chapters"][:-1]

#print(book)


output = template.render(book=book)
print(output)
