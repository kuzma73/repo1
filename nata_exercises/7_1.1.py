#!/usr/bin/env python

res = {}

with open ("sh_ip_int_br.txt") as src:
	for line in src:
		line = line.split()
		if len(line[1].split(".")) == 4 and line[1][0].isdigit():
			interface, ip, _, _, _, _ = line
			res[interface] = ip
			print("{:<20}{:<20}".format(line[0], line[1]))
	for key, val in res.items():	
		print ("{:<20}{:<20}".format(key, val))


			
