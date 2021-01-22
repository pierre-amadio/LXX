#!/bin/bash

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
