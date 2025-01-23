# list
list1 = [1, 5, 4.25, True]
print("list 1 is:", list1, " and type:", type(list1))
fruits = ["apple", "mango", "grapes"]
print("fruits list is:", fruits)

# changing value of fruits
print("changing the first value of fruits")
fruits[0] = "banana"
print(fruits)

# list inside a list
nested_list = [fruits, list1]
print("\n <-- the below list has 'fruits' and list 'list' inside -->")
print(nested_list)
print("\n")
# adding value using append method
added_fruit = str(input("Enter one fruit to add: "))
fruits.append(added_fruit)
print("the new fruit list is ", fruits)
