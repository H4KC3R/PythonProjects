lst = [int(i) for i in input().split()]
x = int(input())
hasX = False
i = 0
for i in range(len(lst)):
    if lst[i] == x:
        print(i, end=" ")
        hasX = True
if not hasX:
    print("Отсутствует")