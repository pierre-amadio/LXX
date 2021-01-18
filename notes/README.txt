#This repository store the information needed to build the septuagin module LXX for the Sword engine.

#It is based on the following informations:

#actual LXX text:
#http://ccat.sas.upenn.edu/gopher/text/religion/biblical/lxxmorph/

#existing scripts from Cyrille.
#https://git.crosswire.org/cyrille/lxx

#This is java code used by Cyrille's scripts.
#https://crosswire.org/svn/sword-tools/trunk/modules/lxxm/src/lxxm/LXXMConv.java
#It require the following class: http://www.mneuhold.at/antike/grkconv_en.html
#I failed to recompile all this from scratch so i re implemeted it in python (mlxx2imp.py)

#1) Prepare your environnement.

#You will need several python module that may not be packaged in your distro.
#It s relatively easy to install them without breaking all your system with virtual env:

mkdir ~/dev/lxxmodule
virtualenv -p /usr/bin/python3 ~/dev/lxxmodule
. ~/dev/lxxmodule/bin/activate

#From now on, we are using a specific version of python where we can install whatever we want without messing with the actual set of python package coming from the distribution.
#You can return to a "normal" environnment running "deactivate". Dont do it now.

~/dev/lxxmodule/bin/python3 -m pip install bs4
~/dev/lxxmodule/bin/python3 -m pip install betacode
~/dev/lxxmodule/bin/python3 -m pip install pygtrie
~/dev/lxxmodule/bin/python3 -m pip install jinja2 

#2) Download the text from ccat.sas.upenn.edu
mkdir original-text
cd original-text 
wget -r -np http://ccat.sas.upenn.edu/gopher/text/religion/biblical/lxxmorph/
cp -r ccat.sas.upenn.edu/gopher/text/religion/biblical/lxxmorph/ .

#Later we will probably have to deal with alternate chapter:  08.JoshA.mlxx 10.JudgesA.mlxx 60.BelTh.mlxx 62.DanielTh.mlxx 64.SusTh.mlxx 23.TobitS.mlxx ../alternate
#There are some error we need to change in the original text:
cd ..
cp original-text/lxxmorph/34.Job.mlxx original-text/lxxmorph/34.Job.mlxx-orig
# job 28:4 
# orig: DIAKOPH\                 N1  NSF    DIAKOPH/ESC)A^N
# wanted: DIAKOPH\                 N1  NSF    DIAKOPH\
tr -d '\16\33' < original-text/lxxmorph/34.Job.mlxx-orig >original-text/lxxmorph/34.Job.mlxx
sed -ri 's|DIAKOPH/\)A|DIAKOPH\\|' original-text/lxxmorph/34.Job.mlxx

#Obadiah having only one chapter, its numbering is a bit different (compare "Obad 3" with "Gen 1:1"
#Let s have it look like the other.
sed -ri 's/Obad ([0-9]+)/Obad 1:\1/' original-text/lxxmorph/43.Obadiah.mlxx
#Same for EpJer
#TODO: we may be loosing the first header here.
sed -ri 's/EpJer ([0-9]+)/Obad 1:\1/' original-text/lxxmorph/55.EpJer.mlxx

#BelOG has 1 chapter only, and the verse 1 is not properly tagged.
sed -ri 's/^Bel\s*$/Bel 1/' original-text/lxxmorph/59.BelOG.mlxx
sed -ri 's/Bel ([0-9]+)/Bel 1:\1/' original-text/lxxmorph/59.BelOG.mlxx

#BelTh has only 1 chapter
sed -ri 's/BelTh ([0-9]+)/BelTh 1:\1/' original-text/lxxmorph/60.BelTh.mlxx

#Sus needs to have chapter 1 and tag only 1 verse per verse. 
#7/8 10/11 13/14 35a 44/45 60-62
sed -ri 's|Sus 7/8|Sus 7|' original-text/lxxmorph/63.SusOG.mlxx
sed -ri 's|Sus 10/11|Sus 10|' original-text/lxxmorph/63.SusOG.mlxx
sed -ri 's|Sus 13/14|Sus 13|' original-text/lxxmorph/63.SusOG.mlxx

#Well, what to do with the 35a verse ? this is probably not ideal:
#sed -ri 's|Sus 35a|Sus 35|' original-text/lxxmorph/63.SusOG.mlxx
#because we will end with 2 verse 35, right ? So, what about just
#putting both of them in a single verse 35 ?
#364 LE/GOUSA                 V1  PAPNSF LE/GW
#365 
#366 Sus 35a                                                   
#let s remove line 365 and 366 then...
sed -i '365,366d' original-text/lxxmorph/63.SusOG.mlxx 


sed -ri 's|Sus 44/45|Sus 44|' original-text/lxxmorph/63.SusOG.mlxx
sed -ri 's|Sus 60-63|Sus 60|' original-text/lxxmorph/63.SusOG.mlxx
sed -ri 's/Sus ([0-9]+)/Sus 1:\1/' original-text/lxxmorph/63.SusOG.mlxx


#3) Convert this to imp.
#
#This text is in a format not directly usable. The next step is to transform it in imp format.
#https://wiki.crosswire.org/DevTools:IMP_Format

cd original-text/lxxmorph/

mkdir rawimp
for i in `ls *mlxx` ; do echo $i ; ../../bin/mlxx2imp.py $i >rawimp/${i/.mlxx/} ;done
cd rawimp
#Lets have normalisation
#https://unix.stackexchange.com/questions/90100/convert-between-unicode-normalization-forms-on-the-unix-command-line
mkdir ../../../imp
for i in `ls *` ; do echo $i; uconv -x Any-NFC $i> ../../../imp/$i.imp ;done
cd ../../..
rm -rf ccat.sas.upenn.edu/



#################################
4) Convert from imp to osis.
```
./bin/imp2osis.sh
./bin/imp2osis-alt.sh
```

Let s clean a bit: 
rm LXX.alt.osis lxx.alt.osis.xml_old LXX.new.osis lxx.osis.xml_old


The resulting file are: 
lxx.osis.xml and lxx.alt.osis.xml


5) Validate the file.

Download the osis schema

```
wget http://www.crosswire.org/osis/osisCore.2.1.1.xsd
```

Validate the files:

```
xmllint --noout --schema osisCore.2.1.1.xsd lxx.osis.xml
xmllint --noout --schema osisCore.2.1.1.xsd lxx.alt.osis.xml
```
This fail at several steps (Josh and Tob)
By example:



6) Create the mod module.

