#!/bin/bash

config_dir="/home/harryl/.gdrive"
sync_list=$(cat "$config_dir/config.ini")

echo > $config_dir/log.txt

while true; do
	echo ------------------------- $(date) ------------------------- >> "$config_dir/log.txt"
	ping -qc 1 google.com

	if [ "$?" -eq 0 ]; then
		IFS=$'\n'
		for path in $sync_list; do
			IFS=" "
			string=($path)

			find "${string[0]}" > "$config_dir/file_new/${string[0]}/file"
			diff "$config_dir/file_old/${string[0]}" "$config_dir/file_new/${string[0]}" | grep ">"

			if [ ! "$?" -eq 0 ]; then
				find "${string[0]}" > "$config_dir/file_old/${string[0]}/file"
				echo "----- Syncing remote files to local files: "${string[0]}" -----" >> "$config_dir/log.txt"
				gdrive sync download --delete-extraneous "${string[1]}" "${string[0]}" >> "$config_dir/log.txt"
				echo >> $config_dir/log.txt
			else
				find "${string[0]}" > "$config_dir/file_old/${string[0]}/file"
				echo "------------------------- New files are present at local directory "${string[0]}" -------------------------" >> "$config_dir/log.txt"
				echo "Aborting ... " >> "$config_dir/log.txt"
			fi
		done

		IFS=$'\n'
		for path in $sync_list; do
			IFS=" "
			string=($path)
			echo "------------------------- Syncing local files to remote files: "${string[0]}" -------------------------" >> "$config_dir/log.txt"
			gdrive sync upload --delete-extraneous "${string[0]}" "${string[1]}" >> "$config_dir/log.txt"
			sleep 10
			echo >> "$config_dir/log.txt"
		done
	else
		echo "Wifi connectivity down ... retrying ..." >> "$config_dir/log.txt"
	fi
	
	sleep 60
done
