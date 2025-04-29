thislist = ["apple", "banana", "cherry"]
print(thislist)
print()

mylist = ["apple", "banana", "cherry"]
print(type(mylist))
print(len(mylist))
print()

thislist1 = list(("apple", "banana", "cherry"))
print(thislist1)
print()

thislist2 = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist2[2:5])
print()

thislist3 = ["apple", "banana", "cherry"]
if "apple" in thislist3:
  print("Yes, 'apple' is in the fruits list")

thislist4 = ["apple", "banana", "cherry"]
thislist4[1] = "blackcurrant"
print(thislist4)
print()

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)
print()