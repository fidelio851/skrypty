#!/usr/bin/python

import os

path =  os.getcwd()
filenames = os.listdir(path)

for filename in filenames:
    os.rename(filename, filename.replace("jpg", "png").lower())