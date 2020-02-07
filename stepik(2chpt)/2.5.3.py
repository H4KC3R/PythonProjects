num = [int(i) for i in input().split()]
num.sort()
repetitive_num = []
if len(num) == 1:
    print()
else:
    for i in range(len(num) - 1):
        if (num[i] == num[i+1]) and (num[i]  not in repetitive_num):
            repetitive_num.append(num[i])
for num in repetitive_num:
    print(num,end=" ")