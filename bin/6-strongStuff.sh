#!/bin/bash

#rm -rf strong
#mkdir strong

for i in `ls specific`; do
  #echo $i;
  if test -f "strong/$i"; then
      echo "strong/$i already exists."
  else
  time ./bin/addStrongNbr.py specific/$i ./strong
  sleep 1
  fi

done;



#./bin/addStrongNbr.py specific/57-Odes.xml ./strong
#./bin/addStrongNbr.py xml1/08.JoshA.xml ./strong

