#!/usr/bin/sh
chmod 775 writerprompt
chmod 555 writerprompt-scifi-genre.txt
chmod 555 writerprompt-scifi-words.txt
BINLOC=/usr/bin
DATALOC=/etc/writerprompt
mkdir -p $BINLOC
mkdir -p $DATALOC
cp -f writerprompt $BINLOC
cp -f writerprompt-scifi-genre.txt $DATALOC
cp -f writerprompt-scifi-words.txt $DATALOC