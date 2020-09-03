#!/bin/bash

SLEEP_TIME=60

if [ "$(hostname)" -eq "Inspiron-7380" ]; then
	SLEEP_TIME=300
done

CONFIG_DIR="/home/harryl/.gdrive"
SYNC_LIST="$(cat "$CONFIG_DIR/config.ini")"

echo > $CONFIG_DIR/log.txt

while true; do
	echo ------------------------- "$(date)" ------------------------- >> "$CONFIG_DIR/log.txt"
	ping -qc 1 google.com

	if [ "$?" -eq 0 ]; then
		IFS=$'\n'

		for ENTRY in $SYNC_LIST; do
			IFS=" "
			STRING=($ENTRY)

			find "${STRING[0]}" > "$CONFIG_DIR/file_new/${STRING[0]}/file"
			diff "$CONFIG_DIR/file_old/${STRING[0]}" "$CONFIG_DIR/file_new/${STRING[0]}" | grep ">"

			if [ ! "$?" -eq 0 ]; then
				find "${STRING[0]}" > "$CONFIG_DIR/file_old/${STRING[0]}/file"

				echo "----- Syncing remote files to local files: "${STRING[0]}" -----" >> "$CONFIG_DIR/log.txt"
				gdrive sync download --delete-extraneous "${STRING[1]}" "${STRING[0]}" >> "$CONFIG_DIR/log.txt"

				echo >> $CONFIG_DIR/log.txt
			else
				find "${STRING[0]}" > "$CONFIG_DIR/file_old/${STRING[0]}/file"

				echo "------------------------- New files are present at local directory "${STRING[0]}" -------------------------" >> "$CONFIG_DIR/log.txt"
				echo "Aborting ... " >> "$CONFIG_DIR/log.txt"
			fi
		done

		IFS=$'\n'
		for ENTRY in $SYNC_LIST; do
			IFS=" "
			STRING=($ENTRY)

			echo "------------------------- Syncing local files to remote files: "${STRING[0]}" -------------------------" >> "$CONFIG_DIR/log.txt"
			gdrive sync upload --delete-extraneous "${STRING[0]}" "${STRING[1]}" >> "$CONFIG_DIR/log.txt"
			
			echo >> "$CONFIG_DIR/log.txt"
			
			sleep 10
		done
	else
		echo "Wifi connectivity down ... retrying ..." >> "$CONFIG_DIR/log.txt"
	fi
	
	sleep SLEEP_TIME
done
