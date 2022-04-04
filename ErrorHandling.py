#Error Handling
while True:
  try:
    age = int(input("what is your age?"))
    10/age
  except ValueError:
    print('please enter a number')
    continue
  except ValueError:
    print('please enter a number')
    break
  else:
    print('thank you!')
    break
  finally:
    print('ok, i am finally done')
  