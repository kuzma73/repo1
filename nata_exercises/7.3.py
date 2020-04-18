#!/usr/bin/env python

valid = ["1","2","3","4","5","6","7","8","9","a","b","c","d","e","f","0"]

with open("CAM_table.txt") as src: 
	for line in src:
		line_as_arr=line.split()
		if len(line_as_arr) > 1:
			mac_parts=line_as_arr[1].split(".")
			if len(mac_parts) == 3:
				for val in mac_parts:
					for char in val:
						if char not in valid:
							str_bad=1
					
			else:
				str_bad=1
		else:
			str_bad=1

		if str_bad == 1:
			str_bad=0
		else:
			print(line.rstrip("\n"))
