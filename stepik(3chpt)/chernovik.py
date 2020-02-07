first =[1,2,3]
second = [4,5,6]
third = [x + y for x, y in zip(first, second)]
print(third)