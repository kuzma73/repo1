#!/usr/bin/env python
london_co = {
    'r1': {
        'location': '21 New Globe Walk',
        'vendor': 'Cisco',
        'model': '4451',
        'ios': '15.4',
        'ip': '10.255.0.1'
    },
    'r2': {
        'location': '21 New Globe Walk',
        'vendor': 'Cisco',
        'model': '4451',
        'ios': '15.4',
        'ip': '10.255.0.2'
    },
    'sw1': {
        'location': '21 New Globe Walk',
        'vendor': 'Cisco',
        'model': '3850',
        'ios': '3.6.XE',
        'ip': '10.255.0.101',
        'vlans': '10,20,30',
        'routing': True
    }
}
#device = raw_input("Enter device:[r1, r2 or sw1] ")
#print( "\n" + "-"*30 )
#print(london_co[device])

#if "fast" in "fastEthernet":
#	print("TRUE")

#print(type(london_co["r1"].items()))

#for name in london_co["r1"].items():
#	print(name)
def test_f(par1, pass1, name):
	print("name - {}\npass - {}\npar1 - {}".format(name, pass1, par1))

test_f("zxc", name="my_name", pass1="123") 

 
 

