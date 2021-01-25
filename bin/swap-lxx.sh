#/bin/bash

installmgr -u LXX
oldzip=/home/melmoth/dev/LXX/LXX.zip

rm -rf ./tmp
mkdir ./tmp

if [ $1 = "devel" ]  
then
 echo "devel";
 cp lxx.conf $SWORD_PATH/mods.d
 cp -r mod/ $SWORD_PATH/modules/texts/ztext/lxx
else
 echo "standard";
 cp $oldzip ./tmp
 cd tmp
 unzip LXX.zip
 cp mods.d/lxx.conf $SWORD_PATH/mods.d
 mv modules/texts/ztext/lxx/ $SWORD_PATH/modules/texts/ztext
fi 

