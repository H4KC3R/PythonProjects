figure = str(input())
if figure == "треугольник" :
    a = int(input())
    b = int(input())
    c = int(input())
    p = float((a + b + c) / 2)
    s = ((p * (p - a) * (p - b) * (p - c)) ** 0.5)
    print(s)
elif figure == "прямоугольник":
    a = float(input())
    b = float(input())
    print(a*b)
elif figure == "круг" :
    r = float(input())
    print(3.14 * r * r)