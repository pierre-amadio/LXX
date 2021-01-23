#!/bin/bash
rm -rf xml1
mkdir xml1
./bin/imp2xml.py imp/01.Gen.1.imp imp/02.Gen.2.imp > xml1/01-Gen.xml
./bin/imp2xml.py imp/03.Exod.imp > xml1/03.Exod.xml
./bin/imp2xml.py imp/04.Lev.imp > xml1/04.Lev.xml
./bin/imp2xml.py imp/05.Num.imp > xml1/05.Num.xml
./bin/imp2xml.py imp/06.Deut.imp > xml1/06.Deut.xml
./bin/imp2xml.py imp/07.JoshB.imp > xml1/07.JoshB.xml
./bin/imp2xml.py imp/08.JoshA.imp > xml1/08.JoshA.xml
./bin/imp2xml.py imp/09.JudgesB.imp > xml1/09.JudgesB.xml
./bin/imp2xml.py imp/10.JudgesA.imp > xml1/10.JudgesA.xml
./bin/imp2xml.py imp/11.Ruth.imp > xml1/11.Ruth.xml
./bin/imp2xml.py imp/12.1Sam.imp > xml1/12.1Sam.xml
./bin/imp2xml.py imp/13.2Sam.imp   > xml1/13.2Sam.xml
./bin/imp2xml.py imp/14.1Kings.imp > xml1/14.1Kings.xml
./bin/imp2xml.py imp/15.2Kings.imp > xml1/15.2Kings.xml
./bin/imp2xml.py imp/16.1Chron.imp > xml1/16.1Chron.xml
./bin/imp2xml.py imp/17.2Chron.imp > xml1/17.2Chron.xml
./bin/imp2xml.py imp/18.1Esdras.imp > xml1/18.1Esdras.xml
./bin/imp2xml.py imp/19.2Esdras.imp > xml1/19.2Esdras.imp
./bin/imp2xml.py imp/ > xml1/
./bin/imp2xml.py imp/ > xml1/
./bin/imp2xml.py imp/30.Odes.imp > xml1/30.Odes.xml
exit

./bin/imp2xml.py imp/ > xml1/
./bin/imp2xml.py imp/ > xml1/
./bin/imp2xml.py imp/ > xml1/
./bin/imp2xml.py imp/ > xml1/
./bin/imp2xml.py imp/ > xml1/
./bin/imp2xml.py imp/ > xml1/
./bin/imp2xml.py imp/ > xml1/
./bin/imp2xml.py imp/ > xml1/
./bin/imp2xml.py imp/ > xml1/
./bin/imp2xml.py imp/ > xml1/
./bin/imp2xml.py imp/ > xml1/

