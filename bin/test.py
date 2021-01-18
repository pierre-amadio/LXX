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
    curVerseSnt=""
    curVerseNbr=0
    curChapterNbr=0
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
        if len(book["chapters"])!=curChapterNbr+1:
          newChapter={}
          newChapter["osisId"]=""
          newChapter["verses"]=[]
          book["chapters"].append(newChapter)
      else:
        """We are in a text line (not a $$chapter/verse  one)"""
        newVerseFlag=True
        curVerseSnt=line
        #print(book["name"],curChapterNbr,curVerseNbr)
        #print(line.strip())
        curVerse={}
        curVerse["osisId"]="%s %s:%s"%(book["name"],curChapterNbr,curVerseNbr)
        curVerse["content"]=line.strip()
        book["chapters"][curChapterNbr-1]["verses"].append(curVerse)
    fp.close()

#print(book)


output = template.render(book=book)
print(output)
