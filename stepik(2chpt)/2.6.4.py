data = []
matrix = []
while True:
    data = [str(i) for i in input().split()]
    if data == ["end"]:
        break
    else:
        num = [int(item) for item in data]
        matrix.append(num)
if matrix:
    row ,column= len(matrix),len(matrix[0])
    result = [[0 for j in range(column)] for i in range(row)]
    for i in range(row):
        for j in range(column):
            result[i][j] = matrix[i + 1 - row][j] + matrix[i - 1][j] + matrix[i][j + 1 - column] + matrix[i][j - 1]
    for row in result:
        for elem in row:
            print(elem, end=' ')
        print()