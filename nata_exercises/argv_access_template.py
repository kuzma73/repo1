#!/usr/bin/env python

from sys import argv

interface = argv[1]
vlan = argv[2]

access_template = [ "switchport mode access", 
	"switchport access vlan {}",
	"switchport nonegotiate",
	"spanning-tree portfast",
	"spanning-tree bpduguard enable"]

print ("Interface {}".format(interface))
print('\n'.join(access_template).format(vlan)) 
