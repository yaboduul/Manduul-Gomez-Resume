#Given the below class:
class Cat:
    species = 'mammal'
    def __init__(self, name, age):
        self.name = name
        self.age = age


# 1 Instantiate the Cat object with 3 cats
cat_1 = Cat('Suzzanne', 13)
cat_2 = Cat('Pancho', 2)
cat_3 = Cat('Ava', 25)

# 2 Create a function that finds the oldest cat
def oldestcat(*args):
  return max(*args)

print(f"The oldest cat is {oldestcat(cat_1.age, cat_2.age, cat_3.age)} years old.")
# 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2