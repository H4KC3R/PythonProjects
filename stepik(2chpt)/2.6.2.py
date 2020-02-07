N = int(input())
k = 1
i = 0
while i < N:
    j = 0
    if i + k < N:
        while j < k:
            print(k, end=" ")
            j += 1
        i += k
        k += 1
    else:
        while j < N - i:
            print(k, end=" ")
            j += 1
        i += k