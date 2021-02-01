#!/usr/bin/env python3
import sys
import re
import betacode.conv
"""
reimplementation of https://crosswire.org/svn/sword-tools/trunk/modules/lxxm/src/lxxm/LXXMConv.java

arguments: (multiples) input files
"""

inputFile=sys.argv[1]

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
                    #System.out.print("/"+((line.indexOf(':') > 0) ? line.substring(line.indexOf(' ') + 1, line.indexOf(':')) : line.substring(line.indexOf(' ') + 1)));
                    if ind>0:
                        print("/%s"%line[line.index(" ")+1:ind],end='')
                        #System.out.print("/"+line.substring(line.indexOf(':') + 1));
                        print("/%s"%line[line.index(":")+1:],end='')
                    else:
                        print("/%s"%line[0:line.index(" ")],end='')

                if(len(headingTxt)):
                    print("<title type=\"section\" subType=\"x-preverse\">%s</title>"%headingTxt,end='')
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
            word=line[0:25].strip()
            parse=line[25:36].strip()
            lemma=line[36:].strip()
            lemma=re.sub('\s+',', ',lemma)
            parse=re.sub('\s+',' ',parse)
            if not first :
                """
                    space between words
                """
                out+=" "
            else:
                first=False
            convertWord=betacode.conv.beta_to_uni(word)
            convertLemma=betacode.conv.beta_to_uni(lemma)
            out+="<w lemma=\"%s\" morph=\"packard:%s\" xlit=\"betacode:%s\">%s</w>"%(convertLemma,parse,word,convertWord)
            if heading and len(word):
                headingTxt+=out
            else:
                if(len(word)):
                    print(out,end='')

    fp.close()
