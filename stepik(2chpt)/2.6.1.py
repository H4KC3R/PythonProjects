num = int(input())
Sum = 0
Sum_quad = 0
Sum += num
Sum_quad += num ** 2
while Sum != 0:
    num = int(input())
    Sum += num
    Sum_quad += num ** 2
print(Sum_quad)