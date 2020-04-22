#!/usr/bin/env python
# -*- coding: utf-8 -*-

access_mode_template = [
    'switchport mode access', 'switchport access vlan',
    'switchport nonegotiate', 'spanning-tree portfast',
    'spanning-tree bpduguard enable'
]

access_config = {
    'FastEthernet0/12': 10,
    'FastEthernet0/14': 11,
    'FastEthernet0/16': 17
}


def generate_access_config(intf_vlan_mapping, access_template):
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
	return ports_list
for line in generate_access_config(access_config, access_mode_template):
	print(line)


'''
    intf_vlan_mapping - словарь с соответствием интерфейс-VLAN такого вида:
        {'FastEthernet0/12':10,
         'FastEthernet0/14':11,
         'FastEthernet0/16':17}
    access_template - список команд для порта в режиме access

    Возвращает список всех портов в режиме access с конфигурацией на основе шаблона
'''

