This repository store the information needed to build the septuagin module LXX for the Sword engine.

It is based on the following informations:

actual LXX text:
http://ccat.sas.upenn.edu/gopher/text/religion/biblical/lxxmorph/

existing scripts from Cyrille.
https://git.crosswire.org/cyrille/lxx

This is java code used by Cyrille's scripts.
https://crosswire.org/svn/sword-tools/trunk/modules/lxxm/src/lxxm/LXXMConv.java
It require the following class: http://www.mneuhold.at/antike/grkconv_en.html
I failed to recompile all this from scratch so i re implemeted it in python (mlxx2imp.py)

1) Prepare your environnement.

You will need several python module that may not be packaged in your distro.
It s relatively easy to install them without breaking all your system with virtual env:
```
mkdir ~/dev/lxxmodule
virtualenv -p /usr/bin/python3 ~/dev/lxxmodule
. ~/dev/lxxmodule/bin/activate
```
From now on, we are using a specific version of python where we can install whatever we want without messing with the actual set of python package coming from the distribution.
You can return to a "normal" environnment running "deactivate". Dont do it now.

```
~/dev/lxxmodule/bin/python3 -m pip install bs4
~/dev/lxxmodule/bin/python3 -m pip install betacode
~/dev/lxxmodule/bin/python3 -m pip install pygtrie
```

2) Download the text from ccat.sas.upenn.edu
```
cd original-text 
wget -r -np http://ccat.sas.upenn.edu/gopher/text/religion/biblical/lxxmorph/
cp -r ccat.sas.upenn.edu/gopher/text/religion/biblical/lxxmorph/ .
# Lets create a directory for the alternative verse too
# and put the alternate chapters there.
mkdir alternate
cd lxxmorph
mv 08.JoshA.mlxx 10.JudgesA.mlxx 60.BelTh.mlxx 62.DanielTh.mlxx 64.SusTh.mlxx 23.TobitS.mlxx ../alternate
```
3) Convert this to imp.

This text is in a format not directly usable. The next step is to transform it in imp format.
https://wiki.crosswire.org/DevTools:IMP_Format

You should still be in LXX/original-text/lxxmorph with your virtualenv activated.
```
rm lxxm-decomp.imp
for i in `ls *mlxx`; do echo $i; ../../bin/mlxx2imp.py $i >> ../lxxm-decomp.imp ;done
cd ..
#Lets have normalisation
#https://unix.stackexchange.com/questions/90100/convert-between-unicode-normalization-forms-on-the-unix-command-line
uconv -x Any-NFC lxxm-decomp.imp > lxxm.imp
rm lxxm-decomp.imp
mv lxxm.imp ../002.txt
```

Let s do the same for the alternates versions.
```
cd ../original-text/alternate
rm lxxm-decomp-alternate.imp
for i in `ls *mlxx`; do echo $i; ../../bin/mlxx2imp.py $i >> ../lxxm-decomp-alternate.imp ; done
cd ..
uconv -x Any-NFC lxxm-decomp-alternate.imp > lxxm-alternate.imp
rm lxxm-decomp-alternate.imp
mv lxxm-alternate.imp ../002.alt
cd ..
```
We now have the main LXX in 002.txt and some alternate version in 002.alt 

There are some error we need to change in the original text:
```
cp original-text/lxxmorph/34.Job.mlxx original-text/lxxmorph/34.Job.mlxx-orig
# job 28:4 
# orig: DIAKOPH\                 N1  NSF    DIAKOPH/ESC)A^N
# wanted: DIAKOPH\                 N1  NSF    DIAKOPH\
tr -d '\16\33' < original-text/lxxmorph/34.Job.mlxx-orig >original-text/lxxmorph/34.Job.mlxx
sed -ri 's|DIAKOPH/\)A|DIAKOPH\\|' original-text/lxxmorph/34.Job.mlxx
```



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

