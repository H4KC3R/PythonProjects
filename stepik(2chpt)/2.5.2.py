num = [int(i) for i in input().split()]
Sum = []
if len(num) == 1:
    Sum = num
else:
    for i in range(len(num)):
        if i == len(num) - 1:
            Sum.append(num[i-1] + num[0])
        else:
            Sum.append(num[i-1] + num[i+1])
for num in Sum:
    print(num,end=" ")
