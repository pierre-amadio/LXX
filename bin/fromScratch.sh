#!/bin/bash
#installmgr -u LXX
#echo yes |installmgr -ri CrossWire LXX
rm -rf original-text imp mod concatenated specific strong xml0 tmp xml-missingv xml-sorted 
./bin/2-downloadRawText.sh
./bin/3-convertToImp.sh
./bin/4-convertToXml.sh
./bin/5-sort-verses.sh 
./bin/6-missing-verses.sh 
./bin/7-marking-concatenated-verses.sh
./bin/8-specificStuff.sh 
./bin/9-strongStuff.sh 
./bin/10-concatenate.sh


