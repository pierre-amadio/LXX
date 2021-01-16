#!/home/melmoth/dev/ankiswordstuff/bin/python3
import sys
import re
import betacode.conv
"""
reimplementation of https://crosswire.org/svn/sword-tools/trunk/modules/lxxm/src/lxxm/LXXMConv.java

https://pypi.org/project/betacode/
~/dev/ankiswordstuff/bin/python3.7  -m pip install  betacode
~/dev/ankiswordstuff/bin/python3.7  -m pip install pygtrie

./mlxxtoimp.py ~/dev/lxx/scripts/lxxm-gen/lxxmorph/01.Gen.1.mlxx 

java -jar  ~/dev/lxx-cyrille/scripts/lxxm-gen/lxxm.jar original-text/lxxmorph/01.Gen.1.mlxx > java.plop
 ./bin/mlxx2imp.py original-text/lxxmorph/01.Gen.1.mlxx > python.plop

uconv -x Any-NFC  java.plop > java.conv
uconv -x Any-NFC  python.plop > python.conv

vimdiff java.conv python.conv

"""

inputFile=sys.argv[1]

#print(inputFile)

with open(inputFile) as fp:
    first=True
    heading=False
    headingTxt = ""
    for line in  fp:
        if(len(line)>1 and len(line)<36):
            """
                line smaller than 36 char, this is  probably the beginning of a verse or chapter.
                Let s print  things such as $$$Gen/1/2
            """
            #m=re.match("(\S+)\s+(\d+):(\d+)",line)
            #if m:
            #    book=m.group(1)
            #    chapter=m.group(2)
            #    verse=m.group(3)
            #    print("\n$$$%s/%s/%s"%(book,chapter,verse))
            #    """
            #        we still need to add some section stuff if headingTxt is not null
            #        see by example $$$Od/1/1
            #    """

            #at least 2 character followed by some digit(s).
            m=re.search("...*[0-9].*",line)
            if m:
                print("")
                print("$$$",end='')
                #book
                print(line[0:line.index(" ")],end='')
                # chapter (or verse if no chapter)
                if ":" in line:
                    ind=line.index(":")
                    if ind>0:
                        print("/%s"%line[line.index(" ")+1:ind],end='')
                        print("/%s"%line[line.index(":")+1],end='')
                    else:
                        print("/%s"%line[0:line.index(" ")],end='')
                print("") 

                if(len(headingTxt)):
                    print("<title type=\"section\" subtype=\"x-preverse\">%s</title>"%headingTxt,end='')
                    headingTxt=""
                    heading=False
            else:
                """
                    The line does not look like a regular Book chapter:verse line, we probably are in a header section (such as with Odes)
                """
                heading=True 
            first=True 
        else:
            """
                line larger than 36 char
            """
            out=""
            if(len(line)==36):
                print("What are len(36) line for???",line)
                sys.exit()
            #print(line)
            word=line[0:25].strip()
            parse=line[25:36].strip()
            lemma=line[36:].strip()
            #print("before='%s"%lemma)
            lemma=re.sub('\s+',', ',lemma)
            #print("\nparse avant '%s'"%parse,end="\n")
            #parse=re.sub('\s+',' ',parse)
            #print("parse apres '%s'"%parse,end="\n")
            #print("word '%s'"%word)
            #print("parse '%s'"%parse)
            #print("lemma '%s'"%lemma)
            #print("first",first)
            if not first :
                """
                    space between words
                """
                out+=" "
            else:
                first=False
            #print("out='%s'"%out)
            convertWord=betacode.conv.beta_to_uni(word)
            convertLemma=betacode.conv.beta_to_uni(lemma)
            #print("convert word='%s'"%convertWord)
            #print("convert lemma='%s"%convertLemma)
            out+="<w lemma=\"%s\" morph=\"packard:%s\" xlit=\"betacode:%s\">%s</w>"%(convertLemma,parse,word,convertWord)
            #print(out)
            if heading:
                headingTxt+=out
            else:
                if(len(word)):
                    print(out,end='')

    fp.close()
