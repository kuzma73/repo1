#!/usr/bin/env python

interface = input("Enter interface number, please:[1] ")
vlan = input("Enter VLAN number, please:[1] ")

access_template = [ "switchport mode access", 
	"switchport access vlan {}",
	"switchport nonegotiate",
	"spanning-tree portfast",
	"spanning-tree bpduguard enable"]

print ("Interface {}".format(interface))
print('\n'.join(access_template).format(vlan)) 

