#!/bin/bash
#Let's turn the imp file into xml 

rm -rf xml0
mkdir xml0
./bin/imp2xml.py imp/01.Gen.1.imp imp/02.Gen.2.imp > xml0/01-Gen.xml
./bin/imp2xml.py imp/03.Exod.imp > xml0/03.Exod.xml
./bin/imp2xml.py imp/04.Lev.imp > xml0/04.Lev.xml
./bin/imp2xml.py imp/05.Num.imp > xml0/05.Num.xml
./bin/imp2xml.py imp/06.Deut.imp > xml0/06.Deut.xml
./bin/imp2xml.py imp/07.JoshB.imp > xml0/07.JoshB.xml
./bin/imp2xml.py imp/08.JoshA.imp > xml0/08.JoshA.xml
./bin/imp2xml.py imp/09.JudgesB.imp > xml0/09.JudgesB.xml
./bin/imp2xml.py imp/10.JudgesA.imp > xml0/10.JudgesA.xml
./bin/imp2xml.py imp/11.Ruth.imp > xml0/11.Ruth.xml
./bin/imp2xml.py imp/12.1Sam.imp > xml0/12.1Sam.xml
./bin/imp2xml.py imp/13.2Sam.imp   > xml0/13.2Sam.xml
./bin/imp2xml.py imp/14.1Kings.imp > xml0/14.1Kings.xml
./bin/imp2xml.py imp/15.2Kings.imp > xml0/15.2Kings.xml
./bin/imp2xml.py imp/16.1Chron.imp > xml0/16.1Chron.xml
./bin/imp2xml.py imp/17.2Chron.imp > xml0/17.2Chron.xml
./bin/imp2xml.py imp/18.1Esdras.imp > xml0/18.1Esdras.xml
./bin/imp2xml.py imp/19.2Esdras.imp > xml0/19.2Esdras.xml
./bin/imp2xml.py imp/20.Esther.imp > xml0/20.Esther.xml
./bin/imp2xml.py imp/21.Judith.imp > xml0/21.Judith.xml
./bin/imp2xml.py imp/22.TobitBA.imp > xml0/22.TobitBA.xml
./bin/imp2xml.py imp/23.TobitS.imp > xml0/23.TobitS.xml
./bin/imp2xml.py imp/24.1Macc.imp > xml0/24.1Macc.xml
./bin/imp2xml.py imp/25.2Macc.imp > xml0/25.2Macc.xml
./bin/imp2xml.py imp/26.3Macc.imp > xml0/26.3Macc.xml
./bin/imp2xml.py imp/27.4Macc.imp > xml0/27.4Macc.xml
./bin/imp2xml.py imp/28.Psalms1.imp imp/29.Psalms2.imp > xml0/28.Psalms.xml
./bin/imp2xml.py imp/30.Odes.imp > xml0/30.Odes.xml
./bin/imp2xml.py imp/31.Proverbs.imp > xml0/31.Proverbs.xml
./bin/imp2xml.py imp/32.Qoheleth.imp > xml0/32.Qoheleth.xml
./bin/imp2xml.py imp/33.Canticles.imp > xml0/33.Canticles.xml
./bin/imp2xml.py imp/34.Job.imp > xml0/34.Job.xml
./bin/imp2xml.py imp/35.Wisdom.imp > xml0/35.Wisdom.xml
./bin/imp2xml.py imp/36.Sirach.imp > xml0/36.Sirach.xml
./bin/imp2xml.py imp/37.PsSol.imp > xml0/37.PsSol.xml
./bin/imp2xml.py imp/38.Hosea.imp > xml0/38.Hosea.xml
./bin/imp2xml.py imp/39.Micah.imp > xml0/39.Micah.xml
./bin/imp2xml.py imp/40.Amos.imp > xml0/40.Amos.xml
./bin/imp2xml.py imp/41.Joel.imp > xml0/41.Joel.xml
./bin/imp2xml.py imp/42.Jonah.imp > xml0/42.Jonah.xml
./bin/imp2xml.py imp/43.Obadiah.imp > xml0/43.Obadiah.xml
./bin/imp2xml.py imp/44.Nahum.imp > xml0/44.Nahum.xml
./bin/imp2xml.py imp/45.Habakkuk.imp > xml0/45.Habakkuk.xml
./bin/imp2xml.py imp/46.Zeph.imp > xml0/46.Zeph.xml
./bin/imp2xml.py imp/47.Haggai.imp > xml0/47.Haggai.xml
./bin/imp2xml.py imp/48.Zech.imp > xml0/48.Zech.xml
./bin/imp2xml.py imp/49.Malachi.imp > xml0/49.Malachi.xml
./bin/imp2xml.py imp/50.Isaiah1.imp imp/51.Isaiah2.imp> xml0/50.Isaiah.xml
./bin/imp2xml.py imp/52.Jer1.imp imp/53.Jer2.imp> xml0/52.Jer.xml
./bin/imp2xml.py imp/54.Baruch.imp > xml0/54.Baruch.xml
./bin/imp2xml.py imp/55.EpJer.imp > xml0/55.EpJer.xml
./bin/imp2xml.py imp/56.Lam.imp > xml0/56.Lam.xml
./bin/imp2xml.py imp/57.Ezek1.imp imp/58.Ezek2.imp > xml0/57.Ezek.xml
./bin/imp2xml.py imp/59.BelOG.imp > xml0/59.BelOG.xml
./bin/imp2xml.py imp/60.BelTh.imp > xml0/60.BelTh.xml
./bin/imp2xml.py imp/61.DanielOG.imp > xml0/61.DanielOG.xml
./bin/imp2xml.py imp/62.DanielTh.imp > xml0/62.DanielTh.xml
./bin/imp2xml.py imp/63.SusOG.imp > xml0/63.SusOG.xml
./bin/imp2xml.py imp/64.SusTh.imp > xml0/64.SusTh.xml


