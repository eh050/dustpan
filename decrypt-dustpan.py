#!/usr/bin/env python3

import os
from cryptography.fernet import Fernet

dirFiles = []

for file in os.listdir():
	if file == "dustpan.py" or file == "thekey.key" or file == "decrypt-dustpan.py":
		continue
	if os.path.isfile(file):
		dirFiles.append(file)


with open("thekey.key", "rb") as key:
	decryption_key = key.read()


for file in dirFiles:
	with open(file, "rb") as thefile:
		contents = thefile.read()
	contents_decrypted = Fernet(decryption_key).decrypt(contents)
	with open(file, "wb") as thefile:
		thefile.write(contents_decrypted)
