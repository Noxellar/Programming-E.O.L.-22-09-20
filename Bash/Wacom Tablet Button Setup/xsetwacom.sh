#!/bin/bash

# Stylus (Buttons in order from pen tip to pen end)

## Sets BUTTON 1 to UNDO
xsetwacom set "Wacom Intuos S Pen stylus" BUTTON 2 "key ctrl z"
## Sets BUTTON 2 to REDO
xsetwacom set "Wacom Intuos S Pen stylus" BUTTON 3 "key ctrl shift z"

# Pad (BUTTONs in order from left to right)

## Sets BUTTON 1 to SAVE
xsetwacom set "Wacom Intuos S Pad pad" BUTTON 1 "key tab"
## Sets BUTTON 2 to REDO
xsetwacom set "Wacom Intuos S Pad pad" BUTTON 2 3
## Sets BUTTON 3 to ZOOM OUT
xsetwacom set "Wacom Intuos S Pad pad" BUTTON 3 "key minus"
## Sets BUTTON 4 to ZOOM IN
xsetwacom set "Wacom Intuos S Pad pad" BUTTON 8 "key plus"

# NOTES:
	# SAVE manually, loser
