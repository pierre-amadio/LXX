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

./bin/2-downloadRawText.txt

#3) Convert this to imp.
#
#This text is in a format not directly usable. The next step is to transform it in imp format.
#https://wiki.crosswire.org/DevTools:IMP_Format

./bin/3-convertToImp.sh



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

