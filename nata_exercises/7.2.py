#!/usr/bin/env python

from sys import argv

with open("config_sw1.txt") as file:
	for line in file:
		if line[0] != "!":
			print( line.rstrip() )




