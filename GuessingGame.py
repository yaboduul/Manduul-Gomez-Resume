from random import randint
# generate a number 1~10
answer =  randint(1, 10)
#input from user?
# check that input is a number 1~10
while True:
  try:
    print(answer)
    guess = int(input('Guess a Number 1-10:  '))
    if 0 > guess < 11:
      if guess == answer:
        print('You are a genius')
        break
    else:
      print('Please enter number 1-10')
  except ValueError:
    print('please enter a number')
    continue