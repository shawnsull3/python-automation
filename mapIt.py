#! /usr/bin/env python3
# mapIt.py - Launches a map in the browser using an address from the command line or clipboard.

import webbrowser, sys, pyperclip

if len(sys.argv) > 1:
    address = ' '.join(sys.argv[1:])
    print(address)
else:
    address = pyperclip.paste()
    print(address)

webbrowser.open('https://www.google.com/maps/place/' + address)