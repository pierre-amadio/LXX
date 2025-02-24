#This repository store the information needed to build the septuagin module LXX for the Sword engine.

# You will need the following installed before starting:
# sword 
# the 2.5 version of the LXX module for sword (used as a reference for the strong number)
# python 3.6 with the maching sword module
# virtualenv

#1) Prepare your environnement.

#You will need several python module that may not be packaged in your distro.
#It s relatively easy to install them without breaking all your system with virtual env

mkdir ~/dev/lxxmodule
virtualenv -p /usr/bin/python3 ~/dev/lxxmodule --system-site-packages
. ~/dev/lxxmodule/bin/activate

#From now on, we are using a specific version of python where we can install whatever we want without messing with the actual set of python package coming from the distribution.
#You can return to a "normal" environnment running "deactivate". Dont do it now.

~/dev/lxxmodule/bin/python3 -m pip install bs4
~/dev/lxxmodule/bin/python3 -m pip install betacode
~/dev/lxxmodule/bin/python3 -m pip install pygtrie
~/dev/lxxmodule/bin/python3 -m pip install jinja2 
~/dev/lxxmodule/bin/python3 -m pip install lxml

#2) Download the text from ccat.sas.upenn.edu
./bin/2-downloadRawText.sh
#Result stored in ./original-text/lxxmorph/

#3) Convert this to imp.
#https://wiki.crosswire.org/DevTools:IMP_Format
./bin/3-convertToImp.sh
#Result stored in ./imp/

#4) Transform imp in xml.
./bin/4-convertToXml.sh
#Result stored in ./xml1

#5) Apply specific modification.
./bin/5-specificStuff.sh
#Result stored in ./specific

#6) Add stong numbers.
# Be sure you have the python Sword module installed, as well as the previous Sword LXX module (2.5)
./bin/6-strongStuff.sh
#Result stored in ./strong

#7) Mark concatenated verses with a pilcrow mark.
./bin/7-marking-concatenated-verses.sh
#Result stored in ./pilcrow

#8) Concatenate stuff
./bin/8-concatenate.sh
#Result stored in ./lxx.osis.xml

#9) Validate the file.

#Download the osis schema
wget http://www.crosswire.org/~dmsmith/osis/osisCore.2.1.1-cw-latest.xsd

#Validate the files:
xmllint --noout --schema osisCore.2.1.1-cw-latest.xsd lxx.osis.xml

#10) Create the mod module.
# https://wiki.crosswire.org/Osis2mod
#https://www.crosswire.org/sword/develop/swordmodule/
rm -rf mod
mkdir mod
# 1 text so far
# 8 book and chapter introduction are determined
# 32 milestone
# 64 extra canonical issues
# 513 : general 
osis2mod mod lxx.osis.xml -z z -v LXX -d 618


