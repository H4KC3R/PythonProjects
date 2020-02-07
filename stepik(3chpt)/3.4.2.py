with open("dataset_3363_3.txt", 'r') as rfile:
    lst = rfile.read().split()
line = ""
maximum = 0
d = {}
number = 0
for elem in lst:
    number = lst.count(elem)
    d[elem] = number
for key, value in d.items():
    if value > maximum:
        maximum = value
        line = key
    elif value == maximum:
        if key < line:
            maximum = value
            line = key
print(line, maximum)