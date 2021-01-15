#!/bin/bash
cp 002_alt_orig 002.alt
#Corrections des noms des livres
sed -ri 's/(\$\$\$[A-Za-z]+)\/([0-9]+)\/([0-9]+)/\1 \2:\3/g' 002.alt
sed -ri 's/\$\$\$([A-Za-z]+) ([0-9]+)$/\$\$\$\1 1:\2/g' 002.alt
sed -ri 's/(\$\$\$SusTh|\$\$\$BelTh)\/([0-9]+)\/([0-9]+)/\1 1:\2-\3/g' 002.alt
sed -ri 's/(\$\$\$SusTh|\$\$\$BelTh)\/([0-9]+)/\1 1:\2/g' 002.alt
#sed -ri 's/(\$\$\$Sus 1:)6$/\11\n\[\]\16/g' 002.alt
sed -ri 's/JoshA/Josh/g' 002.alt
sed -ri 's/JudgA/Judg/g' 002.alt
sed -ri 's/TobS/Tob/g' 002.alt
sed -ri 's/BelTh/Bel/g' 002.alt
sed -ri 's/DanTh/Dan/g' 002.alt
sed -ri 's/SusTh/Sus/g' 002.alt
#Intégration du tag chapitre
#sed -r ':a;N;$!ba;s/(\$\$\$[A-Za-z1-4 ]+ [0-9]+:[0-9]+)\n(<title)/\1 \2/g' 002.alt
#sed -ri 's/(\$\$\$[A-Za-z1-4 ]+ [0-9]+:[0-9]+) (<title*.*$)/\2\n\1/g' 002.alt
#Chapitres
sed -ri 's/\$\$\$(Tob|Bel|Sus|Dan|Judg|Josh) ([0-9]+):1$/<\/seg>\n<\/verse>\n<\/chapter>\n\t<chapter osisID="\1\.\2">\n\t\t<verse osisID="\1\.\2\.1"><seg type="x-variant" subType="x-2">/g'  002.alt
#versets avec tirets
sed -ri 's/\$\$\$([A-Za-z]+) ([0-9]+):([0-9]+)-([0-9]+)/<\/seg>\n<\/verse>\n\t\t<verse osisID="\1\.\2\.\3 \1\.\2\.\4"><seg type="x-variant" subType="x-2">/g' 002.alt
#versets simples
sed -ri 's/\$\$\$([A-Za-z]+) ([0-9]+):([0-9]+)/<\/seg>\n<\/verse>\n\t\t<verse osisID="\1\.\2\.\3"><seg type="x-variant" subType="x-2">/g' 002.alt
sed -ri ':a;N;$!ba;s/(<\/chapter>)\n\t(<chapter osisID=")([A-Za-z/1-4]+)(\.1">)/\1\n\t<\/div>\n\t\t<div type="book" osisID="\3">\n\t\t\2\3\4/g' 002.alt
#Ajout Premier chap pour Josué
sed -ri 's/(<verse osisID="Josh\.15\.21">)/\t<\/div>\n\t\t<div type="book" osisID="Josh">\n<chapter osisID="Josh\.15">\n<verse osisID="Josh\.15\.1">\n\[\]\n<\/verse>\n\1/g' 002.alt
#sed -ri 's/<verse osisID="Bel.1.2">/<verse osisID="Bel.1.1">\n\[\]\n<\/verse>\n<verse osisID="Bel.1.2">/g' 002.alt
sed -ri 's/(<verse osisID="[A-Za-z]+\.[0-9]+\.[0-9]+">)([a-z])/\1\n<milestone type="x-alt-v11n" n="\2"\/>/g' 002.alt
#Ajout nom du livre
sed -ri ':a;N;$!ba;s/(<\/chapter>)\n\t(<chapter osisID=")([A-Za-z1-4]+)(\.1">)/\1\n\t<\/div>\n\t\t<div type="book" osisID="\3">\n\t\t\2\3\4/g' 002.alt
#Tag chapitre avec texte alternatif

#Mettre titre avant tag verset 1
sed -i '1,4d' 002.alt
cat *alt >LXX.alt.osis

sed -ri 's/type="section"/type="chapter"/g' LXX.alt.osis
sed -ri 's/ subtype="x-preverse"//g' LXX.alt.osis
sed -ri 's/(packard:[A-Z1-5]+) +([A-Z])/\1\+\2/g' LXX.alt.osis
sed -ri 's/lemma="/lemma="strong:G lex:/g' LXX.alt.osis
#suppression espace après virgule pour lex
sed -ri 's/, /,/g' LXX.alt.osis
./inversion_lignes.py <LXX.alt.osis >lxx.alt.osis.xml
./fusion.sh codesStrong.strong lxx.alt.osis.xml
mv lxx.alt.osis.xml lxx.alt.osis.xml_old
mv done_lxx.alt.osis.xml lxx.alt.osis.xml
#<seg type="x-variant" subType="x-2">/g'
xmllint --noout --schema ~/.bin/osisCore.2.1.1.xsd lxx.alt.osis.xml
