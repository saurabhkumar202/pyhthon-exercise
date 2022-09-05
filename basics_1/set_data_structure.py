a = {1, 2, 3, 4, 5, 6}
print(type(a))
for item in a:
    print(item)
a.add(7)
print(a)
b = [1, 2, 3, 4]
b.extend(a)
print(b)
