username = input('What would you like to be your username?!')
password = input('What would you like to be your password?!')
pass_length = len(password)
hidden_pass = '*' * pass_length
print(f'password is {hidden_pass} is letter {len(password)} long')