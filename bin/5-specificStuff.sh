#!/bin/bash
#Let s also reorder book according to sword-1.9.0/include/canon_lxx.h
#01 Gen #02 Exod #03 Lev #04 Num #05 Deut #06 Josh #07 Judg #08 Ruth #09 1Sam 
#10 2Sam #11 1Kgs #12 2Kgs #13 1Chr #14 2Chr #15 1Esd #16 Ezra #17 Neh #18 Esth #19 Jdt 
#20 Tob #21 1Macc #22 2Macc #23 3Macc #24 4Macc #25 Ps #26 PrMan #27 Prov #28 Eccl #29 Song 
#30 Job #31 Wis #32 Sir #33 PssSol #34 Hos #35 Amos #36 Mic #37 Joel #38 Obad #39 Jonah 
#40 Nah #41 Hab #42 Zeph #43 Hag #44 Zech #45 Mal #46 Isa #47 Jer #48 Bar #49 Lam 
#50 EpJer #51 Ezek #52 PrAzar #53 Sus #54 Dan #55 Bel #56 1En #57 Odes 


rm -rf specific
mkdir specific

#Odes has some missing first chapters.
./bin/5-specific-odes.py xml1/30.Odes.xml specific/
