#counter 
my_list = [1,2,3,4,5,6,7,8,9,10]
count = 0
for item in range(len(my_list)+1):
  count = item + count
for item in my_list:
  count = item + count
print(count)