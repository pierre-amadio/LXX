#!/bin/bash
installmgr -u LXX
echo yes |installmgr -ri CrossWire LXX
./bin/2-downloadRawText.sh
./bin/3-convertToImp.sh
./bin/4-convertToXml.sh
./bin/5-specificStuff.sh
./bin/6-strongStuff.sh
./bin/7-concatenate.sh

