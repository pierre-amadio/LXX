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

cp concatenated/01-Gen.xml specific/01-Gen.xml
cp concatenated/03.Exod.xml  specific/02-Exod.xml
cp concatenated/04.Lev.xml specific/03-Lev.xml
cp concatenated/05.Num.xml specific/04-Num.xml
cp concatenated/06.Deut.xml specific/05-Deut.xml
./bin/8-specific-combine-subtype.py concatenated/07.JoshB.xml concatenated/08.JoshA.xml  specific/
./bin/8-specific-combine-subtype.py concatenated/09.JudgesB.xml  concatenated/10.JudgesA.xml  specific/
cp concatenated/11.Ruth.xml specific/08-Ruth.xml
cp concatenated/12.1Sam.xml specific/09-1Sam.xml
cp concatenated/13.2Sam.xml specific/10-2Sam.xml
cp concatenated/14.1Kings.xml specific/11-1Kgs.xml
cp concatenated/15.2Kings.xml specific/12-2Kgs.xml
cp concatenated/16.1Chron.xml specific/13-1Chr.xml
cp concatenated/17.2Chron.xml specific/14-2Chr.xml
cp concatenated/18.1Esdras.xml specific/15-1Esd.xml
./bin/8-specific-2esdras.py concatenated/19.2Esdras.xml  specific/
cp concatenated/20.Esther.xml specific/18-Esth.xml
cp concatenated/21.Judith.xml specific/19-Jdt.xml

./bin/8-specific-combine-subtype.py concatenated/22.TobitBA.xml  concatenated/23.TobitS.xml  tmp/
./bin/8-specific-tobit.py tmp/20-Tob.xml specific

cp concatenated/24.1Macc.xml specific/21-1Macc.xml
cp concatenated/25.2Macc.xml specific/22-2Macc.xml
cp concatenated/26.3Macc.xml specific/23-3Macc.xml
cp concatenated/27.4Macc.xml specific/24-4Macc.xml
cp concatenated/28.Psalms.xml specific/25-Ps.xml
#prayer of manashe is already in odes.
#cp concatenated/31.Proverbs.xml specific/27-Prov.xml
./bin/8-specific-proverbs.py concatenated/31.Proverbs.xml specific
cp concatenated/32.Qoheleth.xml specific/28-Eccl.xml
cp concatenated/33.Canticles.xml specific/29-Song.xml
cp concatenated/34.Job.xml specific/30-Job.xml
cp concatenated/35.Wisdom.xml specific/31-Wis.xml
./bin/8-specific-sirach.py concatenated/36.Sirach.xml  specific/
#cp concatenated/37.PsSol.xml specific/37-PssSol.xml
./bin/8-specific-pssol.py concatenated/37.PsSol.xml  specific/
cp concatenated/38.Hosea.xml specific/34-Hos.xml
cp concatenated/40.Amos.xml specific/35-Amos.xml
cp concatenated/39.Micah.xml specific/36-Mic.xml
cp concatenated/41.Joel.xml specific/37-Joel.xml
cp concatenated/43.Obadiah.xml specific/38-Obad.xml
cp concatenated/42.Jonah.xml specific/39-Jonah.xml
cp concatenated/44.Nahum.xml specific/40-Nah.xml
cp concatenated/45.Habakkuk.xml specific/41-Hab.xml
cp concatenated/46.Zeph.xml specific/42-Zeph.xml
cp concatenated/47.Haggai.xml specific/43-Hag.xml
cp concatenated/48.Zech.xml specific/44-Zech.xml
cp concatenated/49.Malachi.xml specific/45-Mal.xml
cp concatenated/50.Isaiah.xml specific/46-Isa.xml
cp concatenated/52.Jer.xml specific/47-Jer.xml
cp concatenated/54.Baruch.xml specific/48-Bar.xml
#cp concatenated/56.Lam.xml specific/49-Lam-Lam.xml
./bin/8-specific-lam.py concatenated/56.Lam.xml  specific
#cp concatenated/55.EpJer.xml specific/50-EpJer.xml
./bin/8-specific-epjer.py concatenated/55.EpJer.xml specific
cp concatenated/57.Ezek.xml specific/51-Ezek.xml
#TODO: what about 52 PrAzar the prayer of azariah in the book of daniel ()
./bin/8-specific-combine-subtype.py concatenated/63.SusOG.xml  concatenated/64.SusTh.xml  tmp/
./bin/8-specific-sus.py tmp/53-Sus.xml specific 

./bin/8-specific-combine-subtype.py concatenated/61.DanielOG.xml  concatenated/62.DanielTh.xml  tmp/
./bin/8-specific-dan.py tmp/54-Dan.xml specific

./bin/8-specific-combine-subtype.py concatenated/59.BelOG.xml  concatenated/60.BelTh.xml  tmp/
./bin/8-specific-bel.py tmp/55-Bel.xml specific

#missing 1Enoch 
./bin/8-specific-odes.py concatenated/30.Odes.xml specific/
