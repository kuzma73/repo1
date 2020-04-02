#!/usr/bin/env python

ip = raw_input("Type ip address, please:(10.1.1.1) " )
#ip = "192.168.1.1"
f_dig = True
f_num = 0

ip_list = ip.split(".")

for tmp in ip_list:
	if tmp.isdigit() and int(tmp) >= 0 and int(tmp) <= 255:
		f_num += 1
		continue
	else: 
		f_dig = False
		break

if f_num == 4 and f_dig == True:
	if int(ip_list[0]) >= 1 and int(ip_list[0]) <= 223:
		print("unicast")
	elif int(ip_list[0]) >= 224 and int(ip_list[0]) <= 239:
		print("multicast")
	elif int(ip_list[0]) == 255 and int(ip_list[1]) == 255 and int(ip_list[2]) == 255 and int(ip_list[3]) == 255:
		print("local broadcast")
	elif int(ip_list[0]) == 0 and int(ip_list[1]) == 0 and int(ip_list[2]) == 0 and int(ip_list[3]) == 0:
		print("unassigned")
	else:
		print("unused")
else:
	print("Bad ip")
 

