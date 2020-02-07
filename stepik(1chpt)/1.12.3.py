a = float(input())
b = float(input())
oper = str(input())
if oper == "mod" :
    if b == 0:
        print("Деление на 0!")
    else:
        print(a % b)
elif oper == "div":
    if b == 0 :
        print("Деление на 0!")
    else:
        print(a//b)
elif oper == "pow":
        print(a**b)
elif oper == "+":
        print(a+b)
elif oper == "-":
        print(a-b)
elif oper == "/":
    if b == 0:
        print("Деление на 0!")
    else:
        print(a / b)
elif oper == "*":
        print(a*b)