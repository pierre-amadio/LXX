#!/bin/bash
#let s create empty verses even when there actually no existing verses
#Missing verses may confuse some applications.
#https://github.com/crosswire/xiphos/issues/1172

rm -rf xml-missingv 
mkdir xml-missingv

for f in $(ls xml-sorted); do
 ./bin/6-missing-verses.py $f xml-missingv/ ;
done
