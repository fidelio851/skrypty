#!/usr/bin/python

import re
import sys

input_file = sys.argv[1]
output_text=[]

with open(input_file) as file:
	text = file.readlines()

for s in text:

#s = "Nigdy sie nie zmienie i nie wazne dlaczego oraz po co"
	#s2 = s.replace(" sie ", " ")
	s = s.replace(" sie ", " ")
	s = s.replace(" i ", " ")
	s = s.replace(" oraz ", " ")
	s = s.replace(" nigdy ", " ")
	s = s.replace(" dlaczego ", " ")
	output_text.append(s)

for s in output_text:
	print(s)