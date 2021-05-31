# password for 3 trial
password = input('Please input your password: ')
i = 1
if password == 'a123456':
	print('Login successfully!')
else:
	while i < 3:
		n = 3-i
		print('Wrong password! you have', n, ' more chance')
		password = input('Please input your password: ')
		if password == 'a123456':
			break
		else:
			i = i + 1
		

	