#!/usr/bin/env python

print("Hello!")
access_template = [
    'switchport mode access', 'switchport access vlan',
    'spanning-tree portfast', 'spanning-tree bpduguard enable'
]

trunk_template = [
    'switchport trunk encapsulation dot1q', 'switchport mode trunk',
    'switchport trunk allowed vlan'
]

access = {
    '0/12': '10',
    '0/14': '11',
    '0/16': '17',
    '0/17': '150'
}
trunk = {
        '0/1': ['add', '10', '20', '99'],
        '0/2': ['only', '11', '30', '100'],
        '0/4': ['del', '17', '101']
    }
'''
for intf, vlan in access.items():
    print('interface FastEthernet' + intf)
    for command in access_template:
        if command.endswith('access vlan'):
            print(' {} {}'.format(command, vlan))
        else:
            print(' {}'.format(command))
'''
for intf, tr_list in trunk.items():
	print("interface FastEthernet" + intf)
	for str1 in trunk_template:
		if str1.endswith("vlan"):
			tmp_str = str1 
			for el_tr_list in tr_list:
				if el_tr_list == "add":
					tmp_str += " add"
				elif el_tr_list == "del":
					tmp_str += " remove"
				elif el_tr_list == "only":
					continue 
				else: 
					 tmp_str +=  " " + el_tr_list
			print(tmp_str)
		else:
			print(str1)
	
			
