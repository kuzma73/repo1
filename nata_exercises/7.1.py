#!/usr/bin/env python


file=open("ospf.txt", "r")
for line in file:
	list = line.split()
	if list[0]=="O":
		print("{:20} {:20}".format("Protocol", "OSPF"))
		print("{:20} {:20}".format("Prefix", list[1]))
		print("{:20} {:20}".format("AD/Metric", list[2]))
		print("{:20} {:20}".format("Next-Hop", list[3] + " " + list[4]))
		print("{:20} {:20}".format("Last update", list[5]))
		print("{:20} {:20}".format("Outbound interface", list[6]))
		print("-"*50)
file.close()
