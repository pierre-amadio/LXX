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
print( sys.argv)
for curFileName in sys.argv[1:]:
  with open(curFileName) as fp:
    #DO we expect a $$$Name/// header ? 
    newVerseFlag=True
    for line in fp:
      if re.search("^\s$",line):
        continue
      #print("line='%s'"%line.strip())
      if newVerseFlag:
        print("new")
        print("line='%s'"%line.strip())
        verseLineReg=re.search("\$\$\$(\S+)/(\d+)/(\d+)",line)
        chapterLineReg=re.search("\$\$\$(\S+)/(\d+)",line)
        if verseLineReg:
          bookName=verseLineReg.group(1)
          chapter=verseLineReg.group(2)
          verse=verseLineReg.group(3)
          print(bookName,chapter,verse)
        elif chapterLineReg:
          bookName=chapterLineReg.group(1)
          chapter=chapterLineReg.group(2)
          print(bookName,chapter)
        else:
          print("Cannot parse '%s'"%line.strip())
          print("in '%s'"%curFileName)
          sys.exit()
        newVerseFlag=False
      else:
        newVerseFlag=True
    fp.close()




output = template.render(book=book)
#print(output)
