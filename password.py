# password for 3 trial
i = 0
while i < 3:
	password = input('Please input your password: ')
	if password == 'a123456':
		print('Login successfully!')
		break
	else: 
		n = 2-i
		print('Wrong password! you have', n, ' more chance')
		i = i + 1
		

	