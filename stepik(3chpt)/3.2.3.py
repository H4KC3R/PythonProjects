n = int(input())
arg = [int(input()) for i in range(n)]
d = {}
for x in arg:
    if x not in d:
        d[x] = f(x)
for x in arg:
    print(d[x])