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
```
We now have the main LXX in 002.txt and some alternate version in 002.alt 

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

```
lxx.osis.xml:11804: parser error : Opening and ending tag mismatch: verse line 11802 and seg
</seg> </verse> </div> <div type="book" osisID="Josh">

Looking in the file:

<verse osisID="Deut.34.12">
<w lemma="strong:G3588 lex:ὁ" morph="packard:RA+APN" xlit="betacode:TA\">τὰ</w><w lemma="strong:G2297 lex:θαυμάσιος" morph="packard:A1A+APN" xlit="betacode:QAUMA/SIA">θαυμάσια</w><w lemma="strong:G3588 lex:ὁ" morph="packard:RA+APN" xlit="betacode:TA\">τὰ</w><w lemma="strong:G3173 lex:μέγας" morph="packard:A1+APN" xlit="betacode:MEGA/LA">μεγάλα</w><w lemma="strong:G2532 lex:καί" morph="packard:C" xlit="betacode:KAI\">καὶ</w><w lemma="strong:G3588 lex:ὁ" morph="packard:RA+ASF" xlit="betacode:TH\N">τὴν</w><w lemma="strong:G5495 lex:χείρ" morph="packard:N3+ASF" xlit="betacode:XEI=RA">χεῖρα</w><w lemma="strong:G3588 lex:ὁ" morph="packard:RA+ASF" xlit="betacode:TH\N">τὴν</w><w lemma="strong:G2900 lex:κραταιός" morph="packard:A1A+ASF" xlit="betacode:KRATAIA/N">κραταιάν</w><w lemma="strong:G3739 lex:ὅς" morph="packard:RR+APN" xlit="betacode:A(\">ἃ</w><w lemma="strong:G4160 lex:ποιέω" morph="packard:VAI+AAI3S" xlit="betacode:E)POI/HSEN">ἐποίησεν</w><w lemma="strong:G0 lex:Μωυσῆς" morph="packard:N+NSM" xlit="betacode:*MWUSH=S">Μωυσῆς</w><w lemma="strong:G1725 lex:ἔναντι" morph="packard:P" xlit="betacode:E)/NANTI">ἔναντι</w><w lemma="strong:G3956 lex:πᾶς" morph="packard:A3+GSM" xlit="betacode:PANTO\S">παντὸς</w><w lemma="strong:G2474 lex:Ἰσραήλ" morph="packard:N+GSM" xlit="betacode:*ISRAHL">Ισραηλ</w>
</seg> </verse> </div> <div type="book" osisID="Josh">
<chapter osisID="Josh.1">

And in a correct one:

<verse osisID="Deut.34.12">
<w lemma="strong:G3588 lex:ὁ" morph="packard:RA+APN" xlit="betacode:TA\">τὰ</w> <w lemma="strong:G2297 lex:θαυμάσιος" morph="packard:A1A+APN" xlit="betacode:QAUMA/SIA">θαυμάσια</w> <w lemma="strong:G3588 lex:ὁ" morph="packard:RA+APN" xlit="betacode:TA\">τὰ</w> <w lemma="strong:G3173 lex:μέγας" morph="packard:A1+APN" xlit="betacode:MEGA/LA">μεγάλα</w> <w lemma="strong:G2532 lex:καί" morph="packard:C" xlit="betacode:KAI\">καὶ</w> <w lemma="strong:G3588 lex:ὁ" morph="packard:RA+ASF" xlit="betacode:TH\N">τὴν</w> <w lemma="strong:G5495 lex:χείρ" morph="packard:N3+ASF" xlit="betacode:XEI=RA">χεῖρα</w> <w lemma="strong:G3588 lex:ὁ" morph="packard:RA+ASF" xlit="betacode:TH\N">τὴν</w> <w lemma="strong:G2900 lex:κραταιός" morph="packard:A1A+ASF" xlit="betacode:KRATAIA/N">κραταιάν</w> <w lemma="strong:G3739 lex:ὅς" morph="packard:RR+APN" xlit="betacode:A(\">ἃ</w> <w lemma="strong:G4160 lex:ποιέω" morph="packard:VAI+AAI3S" xlit="betacode:E)POI/HSEN">ἐποίησεν</w> <w lemma="strong:G0 lex:Μωυσῆς" morph="packard:N+NSM" xlit="betacode:*MWUSH=S">Μωυσῆς</w> <w lemma="strong:G1725 lex:ἔναντι" morph="packard:P" xlit="betacode:E)/NANTI">ἔναντι</w> <w lemma="strong:G3956 lex:πᾶς" morph="packard:A3+GSM" xlit="betacode:PANTO\S">παντὸς</w> <w lemma="strong:G2474 lex:Ἰσραήλ" morph="packard:N+GSM" xlit="betacode:*ISRAHL">Ισραηλ</w>
</verse> </chapter> </div> <div type="book" osisID="Josh">
<chapter osisID="Josh.1">

we have 

</seg> </verse> </div> <div type="book" osisID="Josh">
instead of
</verse> </chapter> </div> <div type="book" osisID="Josh">


If i look in cyrille's repository's 002.txt file , when the Deut chapter close, there also is a </seg> closure. (line 17787)
i do not find the opening seg there.

This seems to be caused by this line in imp2osis.sh

#Tag chapitre avec texte alternatif
sed -ri 's/\$\$\$(Tob|Bel|Sus|Dan|Judg|Josh) ([0-9]+):1$/<\/seg>\n<\/verse>\n<\/chapter>\n\t<chapter osisID="\1\.\2">\n\t\t<verse osisID="\1\.\2\.1"><seg type="x-variant" subType="x-1">/g' 002.txt

This remove 
$$$Josh 1:1

and replace it with

</seg>
<verse>
</chapter>
<chapter osisId="Josh.1">
 <verse osisID="Josh.1.1"><seg type="x-variant" subType="x-1">

It should not have included the </seg> tag.


```

also, no trace of the book of Sus in the new lxx.osis.xml
There is howeverr original-text/lxxmorph/63.SusOG.mlxx , but mlxx2imp.py does not generate any output with it...




6) Create the mod module.

