#!/bin/bash

# Making sure concatenated verses such as 1Kgs 2:46a are marked with a pilcrow mark.
#
#
rm -rf pilcrow
mkdir pilcrow

for i in $(ls strong); do 
 ./bin/concatenated.py strong/$i pilcrow
 #lets get rid of the first <?xml version="1.0" encoding="utf-8"?> line
 sed -i '1d' pilcrow/$i
done


