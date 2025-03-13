#!/bin/bash

# Making sure concatenated verses such as 1Kgs 2:46a are marked with a mark:
# <milestone marker="(46.a)" type="x-p"/>
#
rm -rf concatenated
mkdir concatenated

for i in $(ls xml-missingv); do 
 ./bin/concatenated.py xml-missingv/$i concatenated 
 #lets get rid of the first <?xml version="1.0" encoding="utf-8"?> line
 sed -i '1d' concatenated/$i
done


