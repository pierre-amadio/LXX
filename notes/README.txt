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
sed -ri 's|Sus 44/45|Sus 44|' original-text/lxxmorph/63.SusOG.mlxx
sed -ri 's|Sus 60-63|Sus 60|' original-text/lxxmorph/63.SusOG.mlxx
sed -ri 's/Sus ([0-9]+)/Sus 1:\1/' original-text/lxxmorph/63.SusOG.mlxx

#SusTh has only 1 chapter.
sed -ri 's/SusTh ([0-9]+)/SusTh 1:\1/' original-text/lxxmorph/64.SusTh.mlxx 

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


sed -ri 's/JoshB/Josh/g' imp/07.JoshB.imp
sed -ri 's/JudgB/Judg/g' imp/09.JudgesB.imp
sed -ri 's/2Sam\/K/2Sam/g' imp/13.2Sam.imp
sed -ri 's/1Sam\/K/1Sam/g' imp/12.1Sam.imp
sed -ri 's/1\/3Kgs/1Kgs/g' imp/14.1Kings.imp
sed -ri 's/2\/4Kgs/2Kgs/g' imp/15.2Kings.imp
sed -ri 's/Mac/Macc/g' imp/27.4Macc.imp
sed -ri 's/TobBA/Tob/g' imp/22.TobitBA.imp
sed -ri 's/Qoh/Eccl/g' imp/32.Qoheleth.imp
sed -ri 's/Cant/Song/g' imp/33.Canticles.imp 
sed -ri 's/PsSol/PssSol/g' imp/37.PsSol.imp 
sed -ri 's/Od/Odes/g' imp/30.Odes.imp 


#4) Transform imp in xml.

rm -rf xml1
mkdir xml1
./bin/imp2xml.py imp/01.Gen.1.imp imp/02.Gen.2.imp > xml1/01-Gen.xml
./bin/imp2xml.py imp/03.Exod.imp > xml1/03.Exod.xml
./bin/imp2xml.py imp/04.Lev.imp > xml1/04.Lev.xml
./bin/imp2xml.py imp/05.Num.imp > xml1/05.Num.xml
./bin/imp2xml.py imp/06.Deut.imp > xml1/06.Deut.xml
./bin/imp2xml.py imp/07.JoshB.imp > xml1/07.JoshB.xml
./bin/imp2xml.py imp/08.JoshA.imp > xml1/08.JoshA.xml
./bin/imp2xml.py imp/ > xml1/
./bin/imp2xml.py imp/ > xml1/
./bin/imp2xml.py imp/ > xml1/
./bin/imp2xml.py imp/ > xml1/
./bin/imp2xml.py imp/ > xml1/
./bin/imp2xml.py imp/ > xml1/
./bin/imp2xml.py imp/ > xml1/
./bin/imp2xml.py imp/ > xml1/
./bin/imp2xml.py imp/ > xml1/
./bin/imp2xml.py imp/ > xml1/
./bin/imp2xml.py imp/ > xml1/
./bin/imp2xml.py imp/ > xml1/


#5) Add stong numbers.
# Be sure you have the python Sword module installed, as well as the previous Sword LXX module (2.5)



echo "more things left TODO"
exit


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

