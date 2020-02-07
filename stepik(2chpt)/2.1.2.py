a = int(input())
b = int(input())
flag = True
num = 1
while flag:
    if ((num % a == 0) and (num % b == 0)):
        flag = False
    else:
        num += 1
print(num)