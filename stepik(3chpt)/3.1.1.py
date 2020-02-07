def f(x):
    if x <= -2:
        func = 1 - ((x+2)**2)
        return func
    elif -2 < x <= 2:
        func = -x/2
        return func
    elif 2 < x :
        func = ((x-2)**2) + 1
        return func