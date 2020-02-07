X = int(input())
H = 60 * int(input())
M = H + int(input())
X += M
b =   X // 60
print(b)
print(X - 60 *b)