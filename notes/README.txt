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

echo "more things left TODO"
exit

#TODO: deal with 36.Sirach.imp prolog as a milestone
#those 36 verses are supposed to be milestone _before_ verse1.
# <milestone type="x-alt-v11n" n="1"/>
#right now, those are set as milestones in verses Sir1:0 
#things should be fixabled later on parsing the whole xml file.
#https://wiki.crosswire.org/OSIS_Bibles#OSIS_Milestones


#TODO: what to do with Proverbs funny chapter numbering (ok up to 24, then 24/22a 24/22b 24/22c 24/22d 24/22e and 30/1 then 24/ again.
#Excerpt from "Septuaginta, a reader's edition", p334:
#some witnesses to the greek version of proverbs contain portion of chs 30-31 inserted within ch24 as reflected in rahlfs-hannhart.
#the reason for this textual divergence remains unclear and we have retained teh versifications of the masoretic text for simplicity.
#I think this is what cyrille's script is doing too when it change chp 32-36 to 25-29 here:
#Correction du chapitrage dans Prov
#sed -ri 's/(\$\$\$Prov\/)32(\/)/\125\2/g' 002.txt
#sed -ri 's/(\$\$\$Prov\/)33(\/)/\126\2/g' 002.txt
#sed -ri 's/(\$\$\$Prov\/)34(\/)/\127\2/g' 002.txt
#sed -ri 's/(\$\$\$Prov\/)35(\/)/\128\2/g' 002.txt
#sed -ri 's/(\$\$\$Prov\/)36(\/)/\129\2/g' 002.txt

#TODO: some bookname have to be changed.

#TODO: chapter and verses osis id formating.

#TODO: add missing verses in Odes so frontend are not confused.

#TODO: how to deal with title such as 55.EpJer.imp 37.PsSol.imp 30.Odes.imp 56.Lam.imp 61.DanielOG.imp
# 55 EpJer   1 chapter, title for both book and chapter...
# 37 PsSol  psalm title... i wonder if they are supposed to be considered are belonging to verse 1
# 30 Odes http://www.textexcavation.com/lxxodes.html seems to be also chapter titles.
# 56 Lam , several chapters, seems to be a book title.
# 61 DanielOG chapter 5 only
#not the same kind of title (sometimes verse, sometime chapter)-> it will be dealt on on per book case later.


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

