#!/bin/bash
#Written by Matthieu Villebrun (https://gitlab.com/Matrixd) for lafricain79
# First you have to put the note in a file named "notes" and the text named "text"

#sed -ri ':a;N;$!ba;s/\n([^[])/ \1/g' notes

awk_args=()
for f in "$@"; do
	if ! [ -f "$f" ]; then
		echo "Wrong args: one is not an existing file..." >&2
		exit 1
	fi
	awk_args+=("$f")
done

awk '
# Définition des motifs d’expressions régulières pour le repérage dans les fichiers
BEGIN{
	greekItem="[0-9]+#+.*\r*"
	strongInText="lemma=\"strong\:G"
	lexInText="lex\:.*\r*"
	excluded_tags="\\\\(add|ca|cp|fig|it|nd|qt|va|vp|x)"
}

# FIRST FILE: Dictionnary to array
(FILENAME ~ ".*\.strong"){
	if(FNR == 0){
		delete greek
	}
	if ($0 ~ greekItem){
		n=split($0,tab,"#");
		num=int(tab[1])
		greek[tab[2]]=num
		#printf "%s\n", greek[tab[2]];
		next
	}
}

# SECCOND FILE: insert values in strong tag
(FILENAME ~ ".*\.xml"){
	printf "" > "done_" FILENAME
	if (num > max_notes) max_notes=num
	n=0;
}
{

	if($0 ~ inTextLemma){
		for(i=1;i<=NF;i++){
			if(i==1){
				lastchar=" "
			}else if (i==NF){
				lastchar="\n"
			}
			if($i ~ strongInText){
				currentitem=$i; nextitem=$(i+1);
				sub("lex:", "", nextitem)
				if(match(nextitem, ",+")){
					#the next one is also lex
					nextnextitem=$(i+2)
					sub("\"", "", nextnextitem)
					sub(",", "", nextitem)
					nextindex=greek[nextitem]
					nextnextindex=greek[nextnextitem]
					#printf "%s\n", nextitem;
					printf("%s%i,G%i", currentitem, nextindex, nextnextindex) >> "done_" FILENAME
					printf(" %s %s%s", $(i+1), $(i+2), lastchar) >> "done_" FILENAME
					i=i+2
				}else{
					sub("\"", "", nextitem)
					nextindex=greek[nextitem]
					printf("%s%i", currentitem, nextindex) >> "done_" FILENAME
					printf(" %s%s", $(i+1), lastchar) >> "done_" FILENAME
					i=i+1
				}
				#printf("%s%s", $i, lastchar) >> "done_" FILENAME
			}else {
				#printf "%s", $i
				#printf "%s", lastchar
				printf("%s%s", $i, lastchar) >> "done_" FILENAME
			}
		}
		next
	}
	else {#There is no lemma on that line
		printf("%s\n", $0) >> "done_" FILENAME
		next
	}
}
{ print >> "done_" FILENAME }
' "${awk_args[@]}"
#
