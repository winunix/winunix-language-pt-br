#!/bin/bash

cd /usr/share/applications

ls -1 | while IFS= read -r l; do
	if [ "$(cat "$l" | grep "\[Desktop" | wc -l)" -ne "1" ]; then
		continue
	fi
	echo "$l" | sed "s/.desktop//g"> /tmp/file.txt
	cat "$l" | grep "^Name\[pt_BR\]" | cut -d= -f2 > /tmp/NameBr.txt
	cat "$l" | grep "^GenericName\[pt_BR\]" | cut -d= -f2 > /tmp/GNameBr.txt
	cat "$l" | grep "^Comment\[pt_BR\]" | cut -d= -f2 > /tmp/ComBr.txt
	cat "$l" | grep "^Name\[pt\]" | cut -d= -f2 > /tmp/NamePt.txt
	cat "$l" | grep "^GenericName\[pt\]" | cut -d= -f2 > /tmp/GNamePt.txt
	cat "$l" | grep "^Comment\[pt\]" | cut -d= -f2 > /tmp/ComPt.txt
	cat "$l" | grep "^Name=" | cut -d= -f2 > /tmp/Name.txt
	cat "$l" | grep "^GenericName=" | cut -d= -f2 > /tmp/GName.txt
	cat "$l" | grep "^Comment=" | cut -d= -f2 > /tmp/Com.txt
	
	if [ "$(cat /tmp/file.txt)" != "" ]; then
		A="$(cat /tmp/file.txt)"
		if [ "$(cat /tmp/NameBr.txt)" != "" ]; then
			B="$(cat /tmp/NameBr.txt)"
		elif [ "$(cat /tmp/NamePt.txt)" != "" ]; then
			B="$(cat /tmp/NamePt.txt)"
		elif [ "$(cat /tmp/Name.txt)" != "" ]; then
			B="$(cat /tmp/Name.txt)"
		fi
		
		if [ "$(cat /tmp/GNameBr.txt)" != "" ]; then
			C="$(cat /tmp/GNameBr.txt)"
		elif [ "$(cat /tmp/GNamePt.txt)" != "" ]; then
			C="$(cat /tmp/GNamePt.txt)"
		elif [ "$(cat /tmp/GName.txt)" != "" ]; then
			C="$(cat /tmp/GName.txt)"
		fi
		
		if [ "$(cat /tmp/ComBr.txt)" != "" ]; then
			D="$(cat /tmp/ComBr.txt)"
		elif [ "$(cat /tmp/ComPt.txt)" != "" ]; then
			D="$(cat /tmp/ComPt.txt)"
		elif [ "$(cat /tmp/Com.txt)" != "" ]; then
			D="$(cat /tmp/Com.txt)"
		fi
	fi
	
	echo "[\"$A\",\"$B\",\"$C\",\"$D\"]," >> ~/n.txt
	
	rm /tmp/file.txt
	rm /tmp/NameBr.txt
	rm /tmp/GNameBr.txt
	rm /tmp/ComBr.txt
	rm /tmp/NamePt.txt
	rm /tmp/GNamePt.txt
	rm /tmp/ComPt.txt
	rm /tmp/Name.txt
	rm /tmp/GName.txt
	rm /tmp/Com.txt
done
