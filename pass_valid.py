import bcrypt                             # module for password cryptogtaphy
import hashlib                            # module to encode strings
import getpass                            # module to handle password input
min_pass_length = 9                       # set a minimum password length
max_pass_length = 29                      # set a maxiumum password length
min_user_length = 4                       # set a minimum username length
max_user_length = max_pass_length         # set max username length
digits = [0,1,2,3,4,5,6,7,8,9]            # declare digits
digits = str(digits)                      # modify integer into string
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'] # declare lower letters
upper_letters = [x.upper() for x in letters] # create list of upper letter from lower letters
_credentials = []                         # establish list for credentials, include a default
_credentials = [{'username':'defaultusername', 'hash':bcrypt.hashpw(b'defaultpassword!', bcrypt.gensalt())}]
password = getpass.getpass(prompt='enter password: ', stream= None)
while len(password) < min_pass_length or len(password) >= max_pass_length: # password length checks
	print(f'password length invalid')
	password = getpass.getpass(prompt='enter password: ', stream= None)
while digits not in password: # password format checks
	print('password invalid')
	password = getpass.getpass(prompt='enter password: ', stream= None)
while letters not in password: # password format checks
	print('password invalid')
	password = getpass.getpass(prompt='enter password: ', stream= None)
while upper_letters not in password: # password format checks
	print('password invalid')
	password = getpass.getpass(prompt='enter password: ', stream= None)
salt = bcrypt.gensalt()                   # salt the password
hashed = bcrypt.hashpw(b'password', salt) # hash the password
encoded_pass = hashlib.sha512(password.encode()).hexdigest() # encode the password
print(f'password\t{encoded_pass[0:10]}')  # display first 10 character os encoded pass
print(f'salt\t{salt[0::2]}')              # display salt in 2-step
print(f'hashed\t{hashed[0::2]}')          # display hashed pass in 2-step
username = str(input('enter username: ')) # input username
while len(username) < min_user_length or len(username) >= max_pass_length: # username length checks
	print('username length invalid. plase use another username')
	username = str(input('enter your username: '))
_credentials.append({'username':username, 'hash':hashed})
for users in _credentials:
	if username == users['username']:
		print('validated\t',username)
		if hashed == users['hash']:
			print(f'welcome, {username}!')
		else:
			print('invalid password')
# for hashed in _credentials:
# 	print('\t', hashed['hash'])
