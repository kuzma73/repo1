#!/usr/bin/env python

list = []
tmp_arr = []
fin_list = []
arr_i = []
arr_j = []
tmp = ""

valid = ["1","2","3","4","5","6","7","8","9","a","b","c","d","e","f","0"]

vlan_num = raw_input("Enter vlan numbrer:(10) ")

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
			list.append(line.rstrip("\n"))
	
	i = 0
	for line in list:
		if (line.split()[0] == vlan_num):
			i += 1
			print line
	if i == 0 :
		print("No such VLAN")	
#	for line in list:
#		print(line)
#	
#	l = len(list)
#	print(l)
#	for i in range(0, 8):
#		j = i + 1
#		for j in range(j, 9):
#			if  ( (int(list[i].split()[0])) > int(list[j].split()[0]) ):
#				tmp = list[i]
#				list[i] = list[j]
# 				list[j] = tmp
#	for line in list:
#		print(line) 
			

#	for line in list:
#		tmp_arr = line.split()
#		l = len(tmp_arr)
#		tmp = ""
#		for i in range(1,l-1):
#			tmp = tmp + " " + tmp_arr[i]
#		print(int(tmp_arr[0]))	
#		fin_list.insert(int(tmp_arr[0]),tmp) 
#	#print(fin_list[100])
#	for line in fin_list:
#		print(fin_list.index(line)),
#		print(" " + line)
#
			
