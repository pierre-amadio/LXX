#!/bin/bash

rm -rf xml-sorted
mkdir  xml-sorted

for f in $(ls xml0); do
 ./bin/5-sort-verses.py $f xml-sorted/ ;
 sed -i  '/^$/d' xml-sorted/$f
done
