#!/bin/bash

sleep 2

for i in {1..19}; do
	xdotool key shift+F10
	xdotool key m
	sleep 1
	xdotool key Tab Up Tab Tab Tab Tab Up
	xdotool key Return
	xdotool key Down
	sleep 1
done
