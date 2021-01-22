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
./bin/imp2xml.py imp/ > xml1/

