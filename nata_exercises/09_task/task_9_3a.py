#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Задание 9.3a

Сделать копию функции get_int_vlan_map из задания 9.3.

Дополнить функцию:
    - добавить поддержку конфигурации, когда настройка access-порта выглядит так:
            interface FastEthernet0/20
                switchport mode access
                duplex auto
      То есть, порт находится в VLAN 1

В таком случае, в словарь портов должна добавляться информация, что порт в VLAN 1
      Пример словаря: {'FastEthernet0/12': 10,
                       'FastEthernet0/14': 11,
                       'FastEthernet0/20': 1 }

У функции должен быть один параметр config_filename, который ожидает как аргумент имя конфигурационного файла.

Проверить работу функции на примере файла config_sw2.txt


Ограничение: Все задания надо выполнять используя только пройденные темы.
'''
def get_int_vlan_map( config_filename  ):
	with open(config_filename, "r") as file:
		trunk_dict = {}
		access_dict = {}
		flag_int = False
		flag_acc = False
		for line in file:
			if line.startswith("interface") and flag_int == False:
				flag_int = True
				key = line.split()[1]
			elif "trunk allowed vlan" in line and flag_int == True:
				flag_int = False
				trunk_dict[key] = [ int(item) for item in line.split()[4].split(',')]
			elif "mode access" in line and flag_acc == False:
				flag_acc = True
			elif "access vlan" in line and flag_int == True:
				flag_int = False
				flag_acc = True
				access_dict[key] = int( line.split()[3])
			elif  line.startswith("!") and flag_acc == True and flag_int == True:
				flag_acc = False
				flag_int = False
				access_dict[key] = 1

		return (access_dict, trunk_dict)

#print( get_int_vlan_map("config_sw2.txt"))

				
			
