# INSTALL INSTRUCTIONS FOR PROGRAM

## PACKAGES
- apt-get download audacity audacity-data libasound2 libavcodec58 libavcodec-extra58 libavformat58 libavutil56 libc6 libexpat1 libflac++6v5 libflac8 libgcc-s1 libgdk-pixbuf2.0-0 libglib2.0-0 libgtk-3-0 libid3tag0 liblilv-0-0 libmad0 libmp3lame0 libogg0 libportaudio2 libportsmf0v5 libsndfile1 libsoundtouch1 libsoxr0 libstdc++6 libsuil-0-0 libtwolame0 libvamp-hostsdk3v5 libvorbis0a libvorbisenc2 libvorbisfile3 libwxbase3.0-0v5 libwxgtk3.0-gtk3-0v5
	- audacity
	- audacity-data
	- libasound2
	- libavcodec58
	- libavcodec-extra58
	- libavformat58
	- libavutil56
	- libc6
	- libexpat1
	- libflac++6v5
	- libflac8
	- libgcc-s1
	- libgdk-pixbuf2.0-0
	- libglib2.0-0
	- libgtk-3-0
	- libid3tag0
	- liblilv-0-0
	- libmad0
	- libmp3lame0
	- libogg0
	- libportaudio2
	- libportsmf0v5
	- libsndfile1
	- libsoundtouch1
	- libsoxr0
	- libstdc++6
	- libsuil-0-0
	- libtwolame0
	- libvamp-hostsdk3v5
	- libvorbis0a
	- libvorbisenc2
	- libvorbisfile3
	- libwxbase3.0-0v5
	- libwxgtk3.0-gtk3-0v5

## INSTRUCTIONS
1) Unpack .deb files into source directory

2) Move ./lib and ./lib64 to ./usr

3) cd to ./usr/share

4) Remove ./locale, ./glib-2.0, ./gdb, and ./gcc-10

5) Copy source directory to ~/.local

## EXECUTION
6) In audacity.desktop, change execution to:
	> sh -c "env LD_LIBRARY_PATH="$LD_LIBRARY_PATH:$HOME/.local/lib:$HOME/.local/lib32:$HOME/.local/lib/x86_64-linux-gnu:$HOME/.local/lib/i386-linux-gnu" audacity %F"
