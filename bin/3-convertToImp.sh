#!/bin/bash

cd original-text/lxxmorph/

rm -rf rawimp
mkdir rawimp
for i in `ls *mlxx` ; do echo $i ; ../../bin/mlxx2imp.py $i >rawimp/${i/.mlxx/} ;done
cd rawimp
#Lets have normalisation
#https://unix.stackexchange.com/questions/90100/convert-between-unicode-normalization-forms-on-the-unix-command-line
rm -rf ../../../imp
mkdir ../../../imp
for i in `ls *` ; do echo $i; uconv -x Any-NFC $i> ../../../imp/$i.imp ;done
cd ../../..
rm -rf ccat.sas.upenn.edu/

sed -ri 's/JoshA/Josh/g' imp/08.JoshA.imp
sed -ri 's/JoshB/Josh/g' imp/07.JoshB.imp
sed -ri 's/JudgB/Judg/g' imp/09.JudgesB.imp
sed -ri 's/JudgA/Judg/g' imp/10.JudgesA.imp
sed -ri 's/2Sam\/K/2Sam/g' imp/13.2Sam.imp
sed -ri 's/1Sam\/K/1Sam/g' imp/12.1Sam.imp
sed -ri 's/1\/3Kgs/1Kgs/g' imp/14.1Kings.imp
sed -ri 's/2\/4Kgs/2Kgs/g' imp/15.2Kings.imp
sed -ri 's/Mac/Macc/g' imp/24.1Macc.imp
sed -ri 's/Mac/Macc/g' imp/25.2Macc.imp
sed -ri 's/Mac/Macc/g' imp/26.3Macc.imp
sed -ri 's/Mac/Macc/g' imp/27.4Macc.imp
sed -ri 's/TobBA/Tob/g' imp/22.TobitBA.imp
sed -ri 's/TobS/Tob/g' imp/23.TobitS.imp 
sed -ri 's/Qoh/Eccl/g' imp/32.Qoheleth.imp
sed -ri 's/Cant/Song/g' imp/33.Canticles.imp
sed -ri 's/PsSol/PssSol/g' imp/37.PsSol.imp
sed -ri 's/Od/Odes/g' imp/30.Odes.imp
sed -ri 's/1Esdr/1Esd/g' imp/18.1Esdras.imp
sed -ri 's/DanTh/Dan/g' imp/62.DanielTh.imp 
sed -ri 's/SusTh/Sus/g' imp/64.SusTh.imp
sed -ri 's/BelTh/Bel/g' imp/60.BelTh.imp


# what to do with Proverbs chapter numbering. 
#Excerpt from "Septuaginta, a reader's edition", p334:
#some witnesses to the greek version of proverbs contain portion of chs 30-31 inserted within ch24 as reflected in rahlfs-hannhart.
#the reason for this textual divergence remains unclear and we have retained teh versifications of the masoretic text for simplicity.
sed -ri 's/(\$\$\$Prov\/)32(\/)/\125\2/g' imp/31.Proverbs.imp
sed -ri 's/(\$\$\$Prov\/)33(\/)/\126\2/g' imp/31.Proverbs.imp 
sed -ri 's/(\$\$\$Prov\/)34(\/)/\127\2/g' imp/31.Proverbs.imp
sed -ri 's/(\$\$\$Prov\/)35(\/)/\128\2/g' imp/31.Proverbs.imp
sed -ri 's/(\$\$\$Prov\/)36(\/)/\129\2/g' imp/31.Proverbs.imp

#Let's use dash instead of space as a separator in packard morphcode
# http://crosswire.org/pipermail/sword-devel/2021-February/048659.html
for i in `ls imp`;
	do 
   #sed -ri 's/(packard:[A-Z1-5]+) +([A-Z])/\1\-\2/g' imp/$i ;
   #sed -ri 's/(packard:[V1-9]+) +([A-Z])/\1\-\2/g' imp/$i;
   sed -ri 's/(packard:\S+) +([A-Z])/\1\-\2/g' imp/$i;
done

