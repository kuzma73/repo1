#!/usr/bin/env python

ip = raw_input("Enter ipv4 address and mask:[x.x.x.x/x] ")
tmp = ip.split("/")
ip = tmp[0]
mask = tmp[1]
ip_dec = ip.split(".")
ip_bin = [1,2,3,4]
ip_bin[0] = bin(int(ip_dec[0])).lstrip("0b")
ip_bin[1] = bin(int(ip_dec[1])).lstrip("0b")
ip_bin[2] = bin(int(ip_dec[2])).lstrip("0b")
ip_bin[3] = bin(int(ip_dec[3])).lstrip("0b")

one = "1" * int(mask)
null = "0" * (32  - int(mask))
mask_bin = one + null
print('\n' + "-"*60)
print("Network:")
print("{:15} {:15} {:15} {:15}".format(ip_dec[0], ip_dec[1], ip_dec[2], ip_dec[3]))
print("{:15} {:15} {:15} {:15}".format(ip_bin[0], ip_bin[1], ip_bin[2], ip_bin[3]))
print('\n')
print("Mask")
print("/"),
print(mask)

print("{:15} {:15} {:15} {:15}".format(mask_bin[0:8], mask_bin[9:16], mask_bin[17:24], mask_bin[25:32]))
print("{:15} {:15} {:15} {:15}".format(str(int(mask_bin[0:8],2)), str(int(mask_bin[8:16],2)), str(int(mask_bin[16:24],2)), str(int(mask_bin[24:32],2))))




