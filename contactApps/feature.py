from json import load, dump
from os import system
from getpass import getpass
from time import sleep

fileUser = 'user.json'
fileContact = 'contact.json'
fileEmail = 'email.json'
fileIdent = 'ident.json'

user = {}
contact = {}
email = {}
ident = {}

def loadData():
	global user, contact, email, ident

	with open(fileUser) as f:
		user = load(f)

	with open(fileContact) as f:
		contact = load(f)

	with open(fileEmail) as f:
		email = load(f)

	with open(fileIdent) as f:
		ident = load(f)

	return True

def saveData():
	global user, contact, email, ident

	with open(fileUser, 'w') as f:
		dump(user, f)

	with open(fileContact, 'w') as f:
		dump(contact, f)

	with open(fileEmail, 'w') as f:
		dump(email, f)

	with open(fileIdent, 'w') as f:
		dump(ident, f)

	return True

def login():
	counter = 1
	username = input('Enter username : ')
	password = getpass('Enter password : ')
	dataCheck = False
	passLogin = False
	if username in user:
		dataCheck = True
		passLogin = (user[username] == password)
	else:
		dataCheck = False
		passLogin = False

	while (not dataCheck) or (not passLogin):
		counter += 1
		if counter > 3:
			return False
		print('Combination of username and password is incorrect.')
		username = input('Enter username : ')
		password = getpass('Enter password : ')
		if username in user:
			dataCheck = True
			passLogin = (user[username] == password)
		else:
			dataCheck = False
			passLogin = False
	else:
		print('Login successful.')
		return True

def print_menu():
	print('Welcome to the Alcon App! Connect with school alumni with just a single click!')
	print('1. Print Contact')
	print('2. Add A Contact')
	print('3. Remove A Contact')
	print('4. Lookup A Contact')
	print('5. Quit')

def print_contact():
	if len(contact) > 0:
		for info in contact:
			print(f'Name \t: {info}\t Phone \t: {contact[info]}\t E-mail \t: {email[info]}\t ID \t: {ident[info]}  ')
	else:
		print('There is no contact available right now.')

def add_contact():
	print('Add your contact\n')	

	nama_depan = input('First name \t:')
	nama_belakang = input('Surname \t:')
	name = nama_depan + " " + nama_belakang
	phone = input('Phone \t:')
	emailku = f"{nama_depan}.{nama_belakang}@igs.com"
	identifier = f"igs-{phone[0:5]}"

	contact[name] = phone
	email[name] = emailku
	ident[name] = identifier
	saveData()
	print('Saving Data ...')
	sleep(1.5)
	print('Data Saved.')

def remove_contact():
	print('Remove a contact\n')	

	name = input('Name \t:')
	
	if name in contact:
		del contact[name]
		del email[name]
		del ident[name]
		saveData()
		print('Removing Data')
		sleep(1.5)
		print('Data removed.')
	else:
		print(f'{name} does not exist in contact.')

def lookup_contact():
	print('Looking up a contact\n')	

	name = input('Name \t:')

	if name in contact:
		print(f'Name \t: {name}\t Phone \t: {contact[name]}\t E-mail \t: {email[name]}\t ID \t: {ident[name]}')
	else:
		print(f'{name} does not exist in contact.')