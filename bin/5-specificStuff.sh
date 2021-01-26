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

rm -rf tmp
mkdir tmp

cp xml1/01-Gen.xml specific/01-Gen.xml
cp xml1/03.Exod.xml  specific/02-Exod.xml
cp xml1/04.Lev.xml specific/03-Lev.xml
cp xml1/05.Num.xml specific/04-Num.xml
cp xml1/06.Deut.xml specific/05-Deut.xml
./bin/5-specific-combine-subtype.py xml1/07.JoshB.xml xml1/08.JoshA.xml  specific/
./bin/5-specific-combine-subtype.py xml1/09.JudgesB.xml  xml1/10.JudgesA.xml  specific/
cp xml1/11.Ruth.xml specific/08-Ruth.xml
cp xml1/12.1Sam.xml specific/09-1Sam.xml
cp xml1/13.2Sam.xml specific/10-2Sam.xml
cp xml1/14.1Kings.xml specific/11-1Kgs.xml
cp xml1/15.2Kings.xml specific/12-2Kgs.xml
cp xml1/16.1Chron.xml specific/13-1Chr.xml
cp xml1/17.2Chron.xml specific/14-2Chr.xml
cp xml1/18.1Esdras.xml specific/15-1Esd.xml
./bin/5-specific-2esdras.py xml1/19.2Esdras.xml  specific/
cp xml1/20.Esther.xml specific/18-Esth.xml
cp xml1/21.Judith.xml specific/19-Jdt.xml
./bin/5-specific-combine-subtype.py xml1/22.TobitBA.xml  xml1/23.TobitS.xml  specific/
cp xml1/24.1Macc.xml specific/21-1Macc.xml
cp xml1/25.2Macc.xml specific/22-2Macc.xml
cp xml1/26.3Macc.xml specific/23-3Macc.xml
cp xml1/27.4Macc.xml specific/24-4Macc.xml
cp xml1/28.Psalms.xml specific/25-Ps.xml
#prayer of manashe is already in odes.
cp xml1/31.Proverbs.xml specific/27-Prov.xml
cp xml1/32.Qoheleth.xml specific/28-Eccl.xml
cp xml1/33.Canticles.xml specific/29-Song.xml
cp xml1/34.Job.xml specific/30-Job.xml
cp xml1/35.Wisdom.xml specific/31-Wis.xml
./bin/5-specific-sirach.py xml1/36.Sirach.xml  specific/
#cp xml1/37.PsSol.xml specific/37-PssSol.xml
./bin/5-specific-pssol.py xml1/37.PsSol.xml  specific/
cp xml1/38.Hosea.xml specific/34-Hos.xml
cp xml1/40.Amos.xml specific/35-Amos.xml
cp xml1/39.Micah.xml specific/36-Mic.xml
cp xml1/41.Joel.xml specific/37-Joel.xml
cp xml1/43.Obadiah.xml specific/38-Obad.xml
cp xml1/42.Jonah.xml specific/39-Jonah.xml
cp xml1/44.Nahum.xml specific/40-Nah.xml
cp xml1/45.Habakkuk.xml specific/41-Hab.xml
cp xml1/46.Zeph.xml specific/42-Zeph.xml
cp xml1/47.Haggai.xml specific/43-Hag.xml
cp xml1/48.Zech.xml specific/44-Zech.xml
cp xml1/49.Malachi.xml specific/45-Mal.xml
cp xml1/50.Isaiah.xml specific/46-Isa.xml
cp xml1/52.Jer.xml specific/47-Jer.xml
cp xml1/54.Baruch.xml specific/48-Bar.xml
cp xml1/56.Lam.xml specific/49-Lam-Lam.xml
#cp xml1/55.EpJer.xml specific/50-EpJer.xml
./bin/5-specific-epjer.py xml1/55.EpJer.xml specific
cp xml1/57.Ezek.xml specific/51-Ezek.xml
#TODO: what about 52 PrAzar the prayer of azariah in the book of daniel ()
./bin/5-specific-combine-subtype.py xml1/63.SusOG.xml  xml1/64.SusTh.xml  specific/

./bin/5-specific-combine-subtype.py xml1/61.DanielOG.xml  xml1/62.DanielTh.xml  tmp/
./bin/5-specific-dan.py tmp/54-Dan.xml specific

./bin/5-specific-combine-subtype.py xml1/59.BelOG.xml  xml1/60.BelTh.xml  specific/
#missing 1Enoch 
./bin/5-specific-odes.py xml1/30.Odes.xml specific/
