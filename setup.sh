#!/bin/bash
# Sets up symlink, config files & modules
 
if ! which python3 >/dev/null && ! $(python --version | grep -P 'python 3\.' ); then
    echo "Python 3 is required"
fi

if ! which pip3 >/dev/null && ! $(pip --version | grep -P 'python 3\.'); then
    echo "Pip for python 3 is required"
fi

if which pip3 >/dev/null; then
    pip3 install -r ./requirements.txt
else
    pip install -r ./requirements.txt
fi

ln -si "$PWD/dataer" "$HOME/.local/bin/dataer"
cp -i ./dataer.ini ~/.dataer.ini
