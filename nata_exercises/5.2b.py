#!/usr/bin/env python
from sys import argv

#ip = raw_input("Enter ipv4 address and mask:[x.x.x.x/x] ")

tmp = argv[1].split("/")
ip = tmp[0]
mask = tmp[1]
ip_dec = ip.split(".")

ip_bin1 = "0"*(8 - len(bin(int(ip_dec[0])).lstrip("0b"))) + bin(int(ip_dec[0])).lstrip("0b")
ip_bin2 = "0"*(8 - len(bin(int(ip_dec[1])).lstrip("0b"))) + bin(int(ip_dec[1])).lstrip("0b")
ip_bin3 = "0"*(8 - len(bin(int(ip_dec[2])).lstrip("0b"))) + bin(int(ip_dec[2])).lstrip("0b")
ip_bin4 = "0"*(8 - len(bin(int(ip_dec[3])).lstrip("0b"))) + bin(int(ip_dec[3])).lstrip("0b")
ip_bin = ip_bin1 + ip_bin2 + ip_bin3 + ip_bin4

one = "1" * int(mask)
nul = "0" * (32  - int(mask))
ip_bin = ip_bin[0:(int(mask))] + nul
mask_bin = one + nul
print(mask_bin)

print('\n' + "-"*60)
print("Network:")
print("{:15} {:15} {:15} {:15}".format(str(int(ip_bin[0:8],2)), str(int(ip_bin[8:16],2)), str(int(ip_bin[16:24],2)), str(int(ip_bin[24:32],2))))
print("{:15} {:15} {:15} {:15}".format(ip_bin[0:8], ip_bin[8:16], ip_bin[16:24], ip_bin[24:32]))

#print("{:15} {:15} {:15} {:15}".format(ip_bin[0], ip_bin[1], ip_bin[2], ip_bin[3]))
print('\n')
print("Mask")
print("/"),
print(mask)

print("{:15} {:15} {:15} {:15}".format(mask_bin[0:8], mask_bin[8:16], mask_bin[16:24], mask_bin[24:]))
print("{:15} {:15} {:15} {:15}".format(str(int(mask_bin[0:8],2)), str(int(mask_bin[8:16],2)), str(int(mask_bin[16:24],2)), str(int(mask_bin[24:],2))))




