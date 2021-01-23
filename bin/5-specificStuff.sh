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

cp xml1/01-Gen.xml specific/01-Gen.xml
cp xml1/03.Exod.xml  specific/02-Exod.xml
cp xml1/04.Lev.xml specific/03-Lev.xml
cp xml1/05.Num.xml specific/04-Num.xml
cp xml1/06.Deut.xml specific/
#TODO:07.JoshB.xml and 08.JoshA.xml
#TODO: 09.JudgesB.xml 10.JudgesA.xml
cp xml1/11.Ruth.xml specific/
cp xml1/12.1Sam.xml specific/
cp xml1/13.2Sam.xml specific/
cp xml1/14.1Kings.xml specific/
cp xml1/15.2Kings.xml specific/
cp xml1/16.1Chron.xml specific/
cp xml1/17.2Chron.xml specific/
cp xml1/18.1Esdras.xml specific/
#TODO 19.2Esdras.xml
cp xml1/20.Esther.xml specific/
cp xml1/21.Judith.xml specific/
#TODO: 22.TobitBA.xml 23.TobitS.xml
cp xml1/24.1Macc.xml specific/
cp xml1/25.2Macc.xml specific/
cp xml1/26.3Macc.xml specific/
cp xml1/27.4Macc.xml specific/
cp xml1/28.Psalms.xml specific/
#prayer of manashe is already in odes.
cp xml1/31.Proverbs.xml specific/
cp xml1/32.Qoheleth.xml specific/
cp xml1/33.Canticles.xml specific/
cp xml1/34.Job.xml specific/
cp xml1/35.Wisdom.xml specific/
cp xml1/36.Sirach.xml specific/
cp xml1/37.PsSol.xml specific/
cp xml1/38.Hosea.xml specific/
cp xml1/40.Amos.xml specific/
cp xml1/39.Micah.xml specific/
cp xml1/41.Joel.xml specific/
cp xml1/43.Obadiah.xml specific/
cp xml1/42.Jonah.xml specific/
cp xml1/44.Nahum.xml specific/
cp xml1/45.Habakkuk.xml specific/
cp xml1/46.Zeph.xml specific/
cp xml1/47.Haggai.xml specific/
cp xml1/48.Zech.xml specific/
cp xml1/49.Malachi.xml specific/
cp xml1/50.Isaiah.xml specific/
cp xml1/52.Jer.xml specific/
cp xml1/54.Baruch.xml specific/
cp xml1/56.Lam.xml specific/
cp xml1/55.EpJer.xml specific/
cp xml1/57.Ezek1.xml specific/
#TODO: what about 52 PrAzar the prayer of azariah in the book of daniel ()
#TODO 63.SusOG.xml 64.SusTh.xml
#TODO: 61.DanielOG.xml 62.DanielTh.xml
#TODO: 59.BelOG.xml 60.BelTh.xml
#missing 1Enoch 
#Odes has some missing first chapters.
./bin/5-specific-odes.py xml1/30.Odes.xml specific/
