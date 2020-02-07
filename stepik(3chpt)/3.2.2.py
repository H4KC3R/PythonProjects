lst = input().lower().split()
d = {}
number = 0
for elem in lst:
    number = lst.count(elem)
    d[elem] = number
for key, value in d.items():
    print(key,value)