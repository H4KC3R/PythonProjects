num = int(input())
if (num % 100 == 10) or (num % 100 == 11) or (num % 100 == 12) or (num % 100 == 13) or (num % 100 == 14) :
    print(num, "программистов")
else:
    if num % 10 == 1:
        print(num, "программист")
    elif (num % 10 == 2) or (num % 10 == 3) or (num % 10 == 4):
        print(num, "программиста")
    else:
        print(num, "программистов")