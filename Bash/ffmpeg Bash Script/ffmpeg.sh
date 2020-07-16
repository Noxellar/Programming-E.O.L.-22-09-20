#!/bin/bash

# Loop through multiple files named 0.extension to 5.extension
for i in {0..5}; do
	# Convert .webm to .mp4 and vice versa for other extensions: ffmpeg -i $i.webm $i.mp4
	# Make a create a timelapse from a video and put in folder ./out: ffmpeg -i $i.mp4 -filter:v "setpts=0.5*PTS" -an ./out/$i.mp4
	# Convert highres video to lowres (856x480) video and put in folder ./out: ffmpeg -i $i.mp4 -s 854x480 ./out/$i.mp4
	# Increase audio by 10dB: ffmpeg -i $i.mp3 -filter:a "volume=10dB" ./out/$i.mp3
done

