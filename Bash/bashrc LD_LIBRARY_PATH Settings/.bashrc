# ~/.bashrc: executed by bash(1) for non-login shells.
# see /usr/share/doc/bash/examples/startup-files (in the package bash-doc)
# for examples

# set LD_LIBRARY_PATH so it includes user's private lib if it exists
if [ -d "$HOME/.local/lib" ] ; then
    export LD_LIBRARY_PATH="$LD_LIBRARY_PATH:$HOME/.local/lib"
fi

# set LD_LIBRARY_PATH so it includes user's private lib if it exists
if [ -d "$HOME/.local/lib32" ] ; then
    export LD_LIBRARY_PATH="$LD_LIBRARY_PATH:$HOME/.local/lib32"
fi

# set LD_LIBRARY_PATH so it includes user's private lib if it exists
if [ -d "$HOME/.local/lib/x86_64-linux-gnu" ] ; then
    export LD_LIBRARY_PATH="$LD_LIBRARY_PATH:$HOME/.local/lib/x86_64-linux-gnu"
fi

# set LD_LIBRARY_PATH so it includes user's private lib if it exists
if [ -d "$HOME/.local/lib/i386-linux-gnu" ] ; then
    export LD_LIBRARY_PATH="$LD_LIBRARY_PATH:$HOME/.local/lib/i386-linux-gnu"
fi

# The above does not work for .desktop files. Use this instead and replace program with your program name
Exec=sh -c "env LD_LIBRARY_PATH="$LD_LIBRARY_PATH:$HOME/.local/lib:$HOME/.local/lib32:$HOME/.local/lib/x86_64-linux-gnu:$HOME/.local/lib/i386-linux-gnu" program %alphabet :)"
