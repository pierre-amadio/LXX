#!/bin/bash
#installmgr -u LXX
#echo yes |installmgr -ri CrossWire LXX
rm -rf original-text imp mod pilcrow specific strong xml0 xml1 tmp
./bin/2-downloadRawText.sh
./bin/3-convertToImp.sh
./bin/4-convertToXml.sh
./bin/5-specificStuff.sh
./bin/6-strongStuff.sh
./bin/7-marking-concatenated-verses.sh
./bin/8-concatenate.sh


