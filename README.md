This repository store the information needed to build the septuagin module LXX for the Sword engine.

It is based on the following informations:

#actual LXX text:
http://ccat.sas.upenn.edu/gopher/text/religion/biblical/lxxmorph/

#existing scripts from Cyrille.
https://git.crosswire.org/cyrille/lxx

#This java code used by Cyrille's scripts.
#https://crosswire.org/svn/sword-tools/trunk/modules/lxxm/src/lxxm/LXXMConv.java
#It require the following class: http://www.mneuhold.at/antike/grkconv_en.html
#I failed to recompile all this from scratch so i re implemeted it in python.

1) Prepare your environnement.

You will need several python module that may not be packaged in your distro.
It s relatively easy to install them without breaking all your system with virtual env:

mkdir ~/dev/lxxmodule
virtualenv -p /usr/bin/python3 ~/dev/lxxmodule
. ~/dev/lxxmodule/bin/activate

From now on, we are using a specific version of python where we can install whatever we want without messing with the actual set of python package coming from the distribution.
You can return to a "normal" environnment running "deactivate". Dont do it now.

~/dev/lxxmodule/bin/python3 -m pip install bs4
~/dev/lxxmodule/bin/python3 -m pip install betacode
~/dev/lxxmodule/bin/python3 -m pip install pygtrie


2) Download the text from ccat.sas.upenn.edu

cd original-text 
wget -r -np http://ccat.sas.upenn.edu/gopher/text/religion/biblical/lxxmorph/
cp -r ccat.sas.upenn.edu/gopher/text/religion/biblical/lxxmorph/ .
# Lets create a directory for the alternative verse too
# and put the alternate chapters there.
mkdir alternate
cd lxxmorph
mv 08.JoshA.mlxx 10.JudgesA.mlxx 60.BelTh.mlxx 62.DanielTh.mlxx 64.SusTh.mlxx 23.TobitS.mlxx ../alternate

3) Convert to imp.

This text is in a format not directly usable. The next step is to imp format.
https://wiki.crosswire.org/DevTools:IMP_Format


