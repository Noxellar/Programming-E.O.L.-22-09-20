#!/bin/bash

while true; do
	ping -qc 1 google.com

	if [ "$?" -eq 0 ]; then
		cd /home/harryl/.icons
		
		rm -rf Adwaita++
		rm -rf Adwaita++-Colorful
		rm -rf Adwaita++-Dark
		rm -rf Adwaita++-Light

		wget -qO- https://raw.githubusercontent.com/Bonandry/adwaita-plus/master/install.sh | env DESTDIR="$HOME/.icons" sh

		cd Adwaita++/apps/scalable

		rm firefox-official.svg && rm chromium.svg

		cp google-chrome.svg chromium.svg && cp /home/harryl/.icons/firefox-official.svg firefox-official.svg
		
		break
	fi
done
