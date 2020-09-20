#!/bin/bash

while true; do
	ping -qc 1 google.com

	if [ "$?" -eq 0 ]; then
		cd ~/.icons

		rm -rf Yaru++
		rm -rf kYaru++
		rm -rf Yaru++-Color
		rm -rf Yaru++-Dark
		rm -rf Yaru++-Minimal
		rm -rf Yaru++-Smooth

		wget -qO- https://raw.githubusercontent.com/Bonandry/yaru-plus/master/install.sh | env DESTDIR="$HOME/.icons" sh
		
		break
	fi
done

# yaru-theme-gtk