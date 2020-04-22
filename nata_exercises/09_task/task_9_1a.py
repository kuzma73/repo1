#!/usr/bin/env python
# -*- coding: utf-8 -*-

access_mode_template = [
    'switchport mode access', 'switchport access vlan',
    'switchport nonegotiate', 'spanning-tree portfast',
    'spanning-tree bpduguard enable'
]

port_security_template = [
    'switchport port-security maximum 2',
    'switchport port-security violation restrict',
    'switchport port-security'
]

access_config = {
    'FastEthernet0/12': 10,
    'FastEthernet0/14': 11,
    'FastEthernet0/16': 17
}


def generate_access_config(intf_vlan_mapping, access_template, psecurity=None):
	ports_list = []
	sorted_keys = []
	sorted_keys = sorted(intf_vlan_mapping)
	for key in sorted_keys:
		ports_list.append("interface " + key)
		for line in access_template:
			if "vlan" in line:
				ports_list.append(line + " " + str(intf_vlan_mapping[key]))
			else:
				ports_list.append(line)
		if psecurity != None:
			for line in port_security_template:
				ports_list.append(line)
			
	return ports_list

for line in generate_access_config(access_config, access_mode_template):
#for line in generate_access_config(access_config, access_mode_template, port_security_template):
	print(line)


