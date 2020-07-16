#!/bin/bash

read -p "Tar XZ path: " file_out
read -p "File(s) to tar (separate files by spaces): " file_in

echo $file_out
echo $file_in

XZ_OPT=-9e tar -cJf $file_out $file_in

