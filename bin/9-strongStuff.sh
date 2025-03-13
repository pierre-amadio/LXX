#!/bin/bash

rm -rf strong
mkdir strong

for i in `ls specific`; do
  #echo $i;
  if test -f "strong/$i"; then
      echo "strong/$i already exists."
  else
  time ./bin/addStrongNbr.py specific/$i ./strong
  #lets get rid of the first <?xml version="1.0" encoding="utf-8"?> line
  sed -i '1d' ./strong/$i
  sleep 1
  fi

done;




