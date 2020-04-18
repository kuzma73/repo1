#!/usr/bin/env python

res = {}

with open("sh_ip_interface.txt") as src:
	for line in src:
		if "line protocol" in line:
			interface = line.split()[0]
			#print("1")
		elif "MTU" in line:
			#print("2")
			res[interface] = line.split()[-2]

	for key, val in res.items():
		print("{:<20}{:<20}".format(key, val))
	
