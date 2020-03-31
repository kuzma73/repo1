#!/usr/bin/env python

access_template = [
    'switchport mode access', 'switchport access vlan {}',
    'switchport nonegotiate', 'spanning-tree portfast',
    'spanning-tree bpduguard enable'
]

trunk_template = [
    'switchport trunk encapsulation dot1q', 'switchport mode trunk',
    'switchport trunk allowed vlan {}'
]
trunk = "Enter valid vlans:(4,10,18) "
access = "Enter vlan number:(15) "

mode = raw_input("Enter interface mode:(trunk/access) ")
i = raw_input("Enter type and number of interface:(Gi1/0/1) ")
vlans = raw_input(locals().get(mode))
#mode = "access"
#i = "f0/0"
#vlans = "1,2,3,4,5"
mode_name = mode + "_" + "template"

print("\n"+"-"*30 + "\n")
print("interface {}".format(i))
true_list = locals().get(mode_name)
print("\n".join(true_list).format(vlans))



