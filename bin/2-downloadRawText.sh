#!/bin/bash

rm -rf original-text
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
sed -ri 's/EpJer ([0-9]+)/EpJer 1:\1/' original-text/lxxmorph/55.EpJer.mlxx

#BelOG has 1 chapter only, and the verse 1 is not properly tagged.
sed -ri 's/^Bel\s*$/Bel 1/' original-text/lxxmorph/59.BelOG.mlxx
sed -ri 's/Bel ([0-9]+)/Bel 1:\1/' original-text/lxxmorph/59.BelOG.mlxx
#Verse 1:31 and 1:32 are mixed together, let s call it 1:31
sed -ri 's|Bel 1:31/32|Bel 1:31|g' original-text/lxxmorph/59.BelOG.mlxx


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


#In Gen10:6 and Gen10:13, the morph code has a space in the right part: 
# N   N M    *MESRAIM
#This end up as a non valid key entry for the Teil packard module.
#let s change it to 
# N   NDM    *MESRAIM
sed -ri 's/N   N M    \*MESRAIM/N   NDM    \*MESRAIM/g' original-text/lxxmorph/01.Gen.1.mlxx                                                                                                                                           
#Jeremy has two verse merged : Jer 7:27/28
sed -ri 's|Jer 7:27/28|Jer 7:27|' original-text/lxxmorph/52.Jer1.mlxx

