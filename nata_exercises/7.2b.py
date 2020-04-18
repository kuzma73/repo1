#!/usr/bin/env python

from sys import argv

ignore = ["duplex", "alias", "Current configuration"]

with open("config_sw1.txt") as file, open("config_sw1_clear.txt", "w") as dest:
	for line in file:
		flag=0
		for  val in ignore:
			if val in line:
				 flag = 1
				 break
		if line[0] != "!" and flag == 0:
			dest.write(line)

			




