#!/bin/bash

cat <<EOF > lxx.osis.xml 
<?xml version="1.0" encoding="UTF-8" ?>
<osis xmlns="http://www.bibletechnologies.net/2003/OSIS/namespace" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.bibletechnologies.net/2003/OSIS/namespace http://www.crosswire.org/~dmsmith/osis/osisCore.2.1.1-cw-latest.xsd">
<osisText osisIDWork="LXX" osisRefWork="OT" xml:lang="grc">
	<header>
	      <revisionDesc resp="cyrille">
        <date>2025.02.20T22.15.53</date>
        <p>Converted from lxxm.imp</p>
       </revisionDesc>
		<work osisWork="LXX">
			<title>Septuagint, Morphologically Tagged Rahlfs'</title>
			<identifier type="OSIS">Bible.LXX</identifier>
	  </work>
		<work osisWork="LXX">
			<refSystem>Bible.LXX</refSystem>
		</work>
	</header>
EOF

for i in `ls strong/` ; do 
 echo $i;
 cat strong/$i >> lxx.osis.xml
done

echo  "</osisText></osis>">>lxx.osis.xml
