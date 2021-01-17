#!/bin/bash

#Correction du chapitrage dans Prov
sed -ri 's/(\$\$\$Prov\/)32(\/)/\125\2/g' 002.txt
sed -ri 's/(\$\$\$Prov\/)33(\/)/\126\2/g' 002.txt
sed -ri 's/(\$\$\$Prov\/)34(\/)/\127\2/g' 002.txt
sed -ri 's/(\$\$\$Prov\/)35(\/)/\128\2/g' 002.txt
sed -ri 's/(\$\$\$Prov\/)36(\/)/\129\2/g' 002.txt
#Correction des versets avec fusionnés dans suzanne
sed -ri 's/(\$\$\$Sus)\/([0-9]+)\/([0-9]+)/\1 1:\2-\3/g' 002.txt 
#Remplacement de / par :
sed -ri 's/(\$\$\$[A-Za-z/1-4]+)\/([0-9]+)\/([0-9]+)/\1 \2:\3/g' 002.txt 
#Corrections des noms des livres
sed -ri 's/\$\$\$2Esdr 1([1-9])/\$\$\$Neh \1/g' 002.txt
sed -ri 's/\$\$\$2Esdr 2([0-9])/\$\$\$Neh 1\1/g' 002.txt
sed -ri 's/\$\$\$2Esdr /\$\$\$Ezra /g' 002.txt
sed -ri 's/\$\$\$Sir\/Prolog\//\$\$\$Sir 0:/g' 002.txt


sed -ri 's/\$\$\$([A-Za-z]+)\//\$\$\$\1 1:/g' 002.txt
sed -ri 's/(\$\$\$Sus 1:)6$/\11\n\[\]\16/g' 002.txt
sed -ri 's/JoshB/Josh/g' 002.txt
sed -ri 's/JudgB/Judg/g' 002.txt
sed -ri 's/2Sam\/K/2Sam/g' 002.txt
sed -ri 's/1Sam\/K/1Sam/g' 002.txt
sed -ri 's/1\/3Kgs/1Kgs/g' 002.txt
sed -ri 's/2\/4Kgs/2Kgs/g' 002.txt
sed -ri 's/Mac/Macc/g' 002.txt
sed -ri 's/TobBA/Tob/g' 002.txt
sed -ri 's/1Esdr/1Esd/g' 002.txt
sed -ri 's/2Esdr/Ezra/g' 002.txt
sed -ri 's/Proverbs/Prov/g' 002.txt
sed -ri 's/Qoh/Eccl/g' 002.txt
sed -ri 's/Cant/Song/g' 002.txt
sed -ri 's/PsSol/PssSol/g' 002.txt
sed -ri 's/Od/Odes/g' 002.txt


#Ajout de la mention alt pour les variante de versification
sed -ri 's/\$\$\$1Kgs 6:1([a-d])/<milestone type="x-alt-v11n" n="\1"\/>/g' 002.txt
sed -ri 's/\$\$\$Esth 5:1([a-d])/<milestone type="x-alt-v11n" n="\1"\/>/g' 002.txt
sed -ri 's/\$\$\$Prov 7:1([a-d])/<milestone type="x-alt-v11n" n="\1"\/>/g' 002.txt

#versets alt pour Esth
sed -ri 's/\$\$\$([A-Za-z1-4 ]+) ([0-9]+):1(a)$/<\/verse>\n<\/chapter>\n\t<chapter osisID="\1\.\2">\n\t\t<verse osisID="\1\.\2\.1">\n<milestone type="x-alt-v11n" n="\3"\/>/g' 002.txt
#Ajout du tag chap pour Bel
sed -ri 's/\$\$\$Bel 1:2$/\$\$\$Bel 1:1\n\[\]\n\$\$\$Bel 1:2/g' 002.txt
#Tag chapitre avec texte alternatif
sed -ri 's/\$\$\$(Tob|Bel|Sus|Dan|Judg|Josh) ([0-9]+):1$/<\/seg>\n<\/verse>\n<\/chapter>\n\t<chapter osisID="\1\.\2">\n\t\t<verse osisID="\1\.\2\.1"><seg type="x-variant" subType="x-1">/g' 002.txt

#Verset avec texte alternatif
sed -ri 's/\$\$\$(Tob|Bel|Sus|Dan|Judg|Josh) ([0-9]+):([0-9]+)/<\/seg>\n<\/verse>\n<verse osisID="\1\.\2\.\3"><seg type="x-variant" subType="x-1">/g' 002.txt
sed -ri 's/\$\$\$(Tob|Bel|Sus|Dan|Judg|Josh) ([0-9]+):([0-9]+)-([0-9]+)/<\/seg>\n<\/verse>\n\t\t<verse osisID="\1\.\2\.\3 \1\.\2\.\4"><seg type="x-variant" subType="x-1">/g' 002.txt


#Tag chapitre 
sed -ri 's/\$\$\$([A-Za-z1-4]+) ([0-9]+):1$/<\/verse>\n<\/chapter>\n\t<chapter osisID="\1\.\2">\n\t\t<verse osisID="\1\.\2\.1">/g' 002.txt

#Traitement des versets avec tirets
sed -ri 's/\$\$\$([A-Za-z1-4]+) ([0-9]+):([0-9]+)-([0-9]+)/<\/verse>\n\t\t<verse osisID="\1\.\2\.\3 \1\.\2\.\4">/g' 002.txt
#Traitement des versets simples
sed -ri 's/\$\$\$([A-Za-z1-4]+) ([0-9]+):([0-9]+)/<\/verse>\n\t\t<verse osisID="\1\.\2\.\3">/g' 002.txt
#Ajout du tag div
sed -ri ':a;N;$!ba;s/(<\/chapter>)\n\t(<chapter osisID=")([A-Za-z1-4]+)(\.1">)/\1\n\t<\/div>\n\t\t<div type="book" osisID="\3">\n\t\t\2\3\4/g' 002.txt

sed -ri 's/(<verse osisID="[A-Za-z/1-4 ]+\.[0-9]+\.[0-9]+">)([a-z])/\1\n<milestone type="x-alt-v11n" n="\2"\/>/g' 002.txt
#Ajoute du verset 1 fictif pour les chap des Odes sans versets 1, sinon le fichier n'est pas lu correctement par les frontends
sed -ri 's/(<verse osisID="Odes\.5\.9">)/<\/chapter>\n<chapter osisID="Odes\.5">\n<verse osisID="Odes\.5\.1">\n\[\]\n<\/verse>\n\1/g' 002.txt
sed -ri 's/(<verse osisID="Odes\.6\.3">)/<\/chapter>\n<chapter osisID="Odes\.6">\n<verse osisID="Odes\.6\.1">\n\[\]\n<\/verse>\n\1/g' 002.txt
sed -ri 's/(<verse osisID="Odes\.7\.26">)/<\/chapter>\n<chapter osisID="Odes\.7">\n<verse osisID="Odes\.7\.1">\n\[\]\n<\/verse>\n\1/g' 002.txt
sed -ri 's/(<verse osisID="Odes\.8\.52">)/<\/chapter>\n<chapter osisID="Odes\.8">\n<verse osisID="Odes\.8\.1">\n\[\]\n<\/verse>\n\1/g' 002.txt
sed -ri 's/(<verse osisID="Odes\.9\.46">)/<\/chapter>\n<chapter osisID="Odes\.9">\n<verse osisID="Odes\.9\.1">\n\[\]\n<\/verse>\n\1/g' 002.txt
sed -ri 's/(<verse osisID="Odes\.11\.10">)/<\/chapter>\n<chapter osisID="Odes.11">\n<verse osisID="Odes\.11\.1">\n\[\]\n<\/verse>\n\1/g' 002.txt
sed -ri 's/(<verse osisID="Odes\.13\.29">)/<\/chapter>\n<chapter osisID="Odes\.13">\n<verse osisID="Odes\.13\.1">\n\[\]\n<\/verse>\n\1/g' 002.txt
#sed -ri 's/(<verse osisID="Odes\.14\.5">)/<\/chapter>\n<chapter osisID="Odes\.14">\n<verse osisID="Odes\.14\.1">\n\[\]\n<\/verse>\n\1/g' 002.txt



#Traitement de ProlSir (Prologue de Siracide)

#This original line does not actually does anything. 
#sed -ri ':a;N;$!ba;s/<\/verse>\n<\/chapter>\n\t<\/div>\n\t\t<div type="book" osisID="Sir">\n\t\t\t<chapter osisID="Sir\.1">//g' 002.txt
#it is supposed to ged rid of extra </verse></chapter> before the first chapter of Sir (after last chapter of Wis).
#looks like it would work better with 2 tab instead of three
sed -ri ':a;N;$!ba;s/<\/verse>\n<\/chapter>\n\t<\/div>\n\t\t<div type="book" osisID="Sir">\n\t\t<chapter osisID="Sir\.1">//g' 002.txt

sed -ri 's/<chapter osisID="Sir\.0">/<\/div>\n\t\t<div type="book" osisID="Sir">\n\t\t\t<chapter osisID="Sir\.1">/g' 002.txt
sed -ri ':a;N;$!ba;s/<\/verse>\n\t\t<verse osisID="Sir\.0\.([0-9]+)">/<milestone type="x-alt-v11n" n="\1"\/>/g' 002.txt
sed -ri 's/<verse osisID="Sir\.0\.1">/<milestone type="x-alt-v11n" n="1"\/>/g' 002.txt

#Correction de certains caractères non conforme et de tags en trop.
sed -ri 's/̓α//g' 002.txt
sed -i '1,4d' 002.txt
##Ajoute de deux tag de fermetures manquants
sed -ri ':a;N;$!ba;s/(Νινευη<\/w>)\n(<\/verse>\n<\/chapter>\n\t<\/div>)/\1<\/seg>\n\2/g' 002.txt
sed -ri ':a;N;$!ba;s/(ἐποίει<\/w>)\n(<\/verse>)/\1<\/seg>\n\2/g' 002.txt
#sed -ri ':a;N;$!ba;s/(Ισραηλ<\/w>)\n</seg>\n(<\/verse>\n<\/chapter>\n\t<\/div>)\1\n\2/g' 002.txt
#Fusion des fichiers text en un
cat *txt >LXX.new.osis

sed -ri 's/type="section"/type="chapter"/g' LXX.new.osis
sed -ri 's/ subtype="x-preverse"//g' LXX.new.osis
##Traitement de la morpho de packard
sed -ri 's/(packard:[A-Z1-5]+) +([A-Z])/\1\+\2/g' LXX.new.osis
##Traitement des lemmes
sed -ri 's/lemma="/lemma="strong:G lex:/g' LXX.new.osis
#suppression des lignes en trop
sed -ri ':a;N;$!ba;s/(ὄνομα<\/w> <w lemma="strong:G lex:αὐτός" morph="packard:RD\+GSF" xlit="betacode:AU\)TH=S">αὐτῆς<\/w>)\n<\/seg>/\1/g' LXX.new.osis
#suppression espace après virgule pour lex
sed -ri 's/, /,/g' LXX.new.osis
./bin/inversion_lignes.py <LXX.new.osis >lxx.osis.xml

#sed -i '90032d' lxx.osis.xml #A revoir

#This line get rid of Sir 1.6 and Sir 1.8 (and doing so, generate some extra </verse> tag. 
#
#sed -i '68582,68586d' lxx.osis.xml #Sir 1.1
#
#When the script was using the java code to handle the betacode transliteration, 
#it was supposed to get rid of <verse></chapter></div><div type="book" osisID="Sir"><chapter osisID="Sir.1"> here
#68580 <milestone type="x-alt-v11n" n="36"/>
#68581 <w lemma="strong:G lex:ἐννόμως" morph="packard:D" xlit="betacode:E)NNO/MWS">ἐννόμως</w> <w lemma="strong:G lex:βιοτεύω" morph="packard:V1+PAN" xlit="betacode:BIOTEU/EIN">βιοτεύειν</w>
#68582<verse>
#68583 </chapter>
#68584     </div>
#68585         <div type="book" osisID="Sir">
#68586         <chapter osisID="Sir.1">
#68587         <verse osisID="Sir.1.1">
#
#With the python betacode we have something slighlty different:
#

#68490         <verse osisID="Wis.19.22">
#68491 <w lemma="strong:G l........παριστάμενος</w>
#68492 </verse>
#68493 </chapter>
#68494     </div>
#68495         <div type="book" osisID="Sir">
#68496             <chapter osisID="Sir.1">
#68497         <milestone type="x-alt-v11n" n="1"/>
# ....
# ....
#68567 <milestone type="x-alt-v11n" n="36">
#68568 <w lemma="strong:G lex:ἐννόμως" morph="packard:D" xlit="betacode:E)NNO/MWS">ἐννόμως</w> <w lemma="strong:G lex:βιοτεύω" morph="packard:V1+PAN" xlit="betacode:BIOTEU/EIN">βιοτεύειν</w>
#68569 
#68570         <verse osisID="Sir.1.1">
#It looks like there is no nee to "fix" anything.


#Next, why is it that we need to remove line 43327 ?
#Here is what s in the 002.txt file at this stage with the original java betacode decoder:
#43325 </verse>
#43326 <verse osisID="Tob.1.5"><seg type="x-variant" subType="x-1">
#43327 <w lemma="καί" morph="packard:C" xlit="betacode:KAI\">καὶ</w> <w lemma="πᾶς" morph="packard:A1S NPF" xlit="betacode:PA=SAI">πᾶσαι</w> <w lemma="ὁ" morph="packard:RA  NPF" xlit="betacode:AI(">αἱ</w> <w lemm      a="φυλή" morph="packard:N1  NPF" xlit="betacode:FULAI\">φυλαὶ</w> <w lemma="ὁ" morph="packard:RA  NPF" xlit="betacode:AI(">αἱ</w> <w lemma="ἵστημι, ἀπο" morph="packard:VH  AAPNPF" xlit="betacode:SUNAPOSTA=      SAI">συναποστᾶσαι</w> <w lemma="θύω" morph="packard:V1I IAI3P" xlit="betacode:E)/QUON">ἔθυον</w> <w lemma="ὁ" morph="packard:RA  DSF" xlit="betacode:TH=|">τῇ</w> <w lemma="Βααλ" morph="packard:N   DSF" xli      t="betacode:*BAAL">Βααλ</w> <w lemma="ὁ" morph="packard:RA  DSF" xlit="betacode:TH=|">τῇ</w> <w lemma="δάμαλις" morph="packard:N3I DSF" xlit="betacode:DAMA/LEI">δαμάλει</w> <w lemma="καί" morph="packard:C"       xlit="betacode:KAI\">καὶ</w> <w lemma="ὁ" morph="packard:RA  NSM" xlit="betacode:O(">ὁ</w> <w lemma="οἶκος" morph="packard:N2  NSM" xlit="betacode:OI)=KOS">οἶκος</w> <w lemma="Νεφθαλιμ" morph="packard:N         GSM" xlit="betacode:*NEFQALIM">Νεφθαλιμ</w> <w lemma="ὁ" morph="packard:RA  GSM" xlit="betacode:TOU=">τοῦ</w> <w lemma="πατήρ" morph="packard:N3  GSM" xlit="betacode:PATRO/S">πατρός</w> <w lemma="ἐγώ" mor      ph="packard:RP  GS" xlit="betacode:MOU">μου</w> 
#43328 </seg>
#43329 </verse>
#43330 <verse osisID="Tob.1.6"><seg type="x-variant" subType="x-1">
#It looks like the content of Tob1.5 is being removed.
sed -i '43327d' lxx.osis.xml #fin de judith début tob

# Removing a div book node, why ?
#17800         <verse osisID="Deut.34.12">
#17801 <w lemma="strong:G lex: ......
#17802 </seg>
#17803 </verse>
#17804 </chapter>
#17805     </div>
#17806         <div type="book" osisID="Josh">
#17807         <chapter osisID="Josh.1">
#17808         <verse osisID="Josh.1.1"><seg type="x-variant" subType="x-1"> ....
sed -i '17806d' lxx.osis.xml #fin de Deut début Jos


#Inversion de lignes pour validation xmllint
sed -i "90033{h;s/.*/sed -n 90034p lxx.osis.xml/e};90034g" lxx.osis.xml #Bel.1.2
sed -i "90996{h;s/.*/sed -n 90997p lxx.osis.xml/e};90997g" lxx.osis.xml #Dan.5.1
sed -ri 's/(verse osisID=")(Bel\.)(31)(\.32")/\1\21\.\3 \21\4/g' lxx.osis.xml
#Addition of the strong numbers fusion.sh utilise le fichier avec les nombres de strong et le mot équivalent codesStrong.strong


./bin/fusion.sh codesStrong.strong lxx.osis.xml
#Renommage pour des fichiers et néttoyage
mv lxx.osis.xml lxx.osis.xml_old
mv done_lxx.osis.xml lxx.osis.xml
#Check osis file
#xmllint --noout --schema ~/.bin/osisCore.2.1.1.xsd lxx.osis.xml
#osis2mod ~/.sword/modules/texts/ztext/lxxnv/ lxx.osis.xml -z -v LXX #>build_LXX.log
