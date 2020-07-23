#!/bin/bash

for i in ./*.deb ; do
	dpkg-deb -x $i ./
done
