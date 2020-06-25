from json import load, dump
from os import system
from time import sleep

import feature

statusLoading = feature.loadData() #True

system('cls')

if statusLoading:
	#print('Pass')
	passLogin = feature.login() #True
	if passLogin:
		print('Welcome!')
		sleep(2)
		system('cls')
		menu_choice = ''
		
		while menu_choice != '5':
			system('cls')
			feature.print_menu()
			menu_choice = input('Type in a number : ').lower()
			
			if menu_choice == '1':
				feature.print_contact()
				input('ENTER to Exit')

			elif menu_choice == '2':
				feature.add_contact()
				input('ENTER to Exit')

			elif menu_choice == '3':
				feature.remove_contact()
				input('ENTER to Exit')

			elif menu_choice == '4':
				feature.lookup_contact()
				input('ENTER to EXit')

			elif menu_choice == '5':
				break

			else:
				print('Input menu choice correctly.')

	else:
		print('Failed to login.')
else:
	print('App cannot run.')