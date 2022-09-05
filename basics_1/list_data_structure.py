a = [1, 2, 3, 4, 5]
b = (1, 2, 3, 4, 5)
print(a)
print(b)
print("Add new element in a ")
a.insert(5, 6)
a.extend(b)
print(a)
print("Get a particular element in a")
print("A2 is " + str(a[2]))
print("Loop through each element of list")
for item in a:
    print(item)
