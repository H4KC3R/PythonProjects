num = int(input())
a = num //100000
b = (num - a * 100000) // 10000
c = (num - a * 100000 - b * 10000 ) // 1000
d = (num - a * 100000 - b * 10000 - c * 1000) // 100
e = (num - a * 100000 - b * 10000 - c * 1000 - d * 100 ) // 10
f = (num - a * 100000 - b * 10000 - c * 1000 - d * 100  - e * 10)

if (a+b+c) == (d+e+f) :
    print("Счастливый")
else:
    print("Обычный")