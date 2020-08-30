# INSTALL INSTRUCTIONS FOR PROGRAM

## PACKAGES
- mono v.6.10.0.l04 (tarball from website)
	- cmake
		- cmake-data
		- libc6
		- libcurl4
		- libjsoncpp1
		- librhash0

## INSTRUCTIONS
1) Unpack Mono into source directory

2) Unpack dependencies

3) Add to ~/.local folder

4) Instructions in README file

5) Run "./autogen.sh --prefix="/absolute/path/build_directory""

6) Run "./make get-monolite-latest"

7) Run make and then make install

## EXECUTION
8) Make symbolic link from /mono binary folder/mono to ~/.local/bin

9) Copy manpages to ~/.local/share/man

## REFERENCES
- [Compiling Mono on Linux](https://www.mono-project.com/docs/compiling-mono/linux/)