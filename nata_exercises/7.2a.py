#!/usr/bin/env python

from sys import argv

ignore = ["duplex", "alias", "Current configuration"]

with open("config_sw1.txt") as file:
	for line in file:
		flag=0
		for  val in ignore:
			if val in line:
				 flag = 1
				 break
		if line[0] != "!" and flag == 0:
			print( line.rstrip() )
			




