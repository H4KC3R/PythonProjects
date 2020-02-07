a = int(input())
b = int(input())
c = int(input())
if a >= b and a >= c:
    max = a
    if b >= c:
        min = c
        num = b
    else:
        min = b
        num = c
elif b >= c and b >= a :
    max = b
    if a >= c:
        min = c
        num = a
    else:
        min = a
        num = c
elif c >= a and c >= b :
    max = c
    if b > a:
        min = a
        num = b
    else:
        min = b
        num = a

print(max,'\n',min,'\n',num)