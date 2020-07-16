#!/bin/bash

DIR=.local/bin

while true; do
	ping -qc 1 google.com
	
	if [ "$?" -eq 0 ]; then
		read -n 5 -p "Download Version: " version
		while true; do
			wget "https://download.kde.org/stable/krita/$version/krita-$version-x86_64.appimage" -P $DIR
			
			if [ "$?" -eq 0 ]; then
				rm -f krita
				mv $DIR/krita-$version-x86_64.appimage $DIR/krita
				chmod +x $DIR/krita
				break
			else
				echo "Download failed ... retrying ... "
			fi
		done
		break
	else
		echo "Wifi connectivity down ... retrying ..."
	fi
done
