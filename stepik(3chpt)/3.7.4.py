d = {'север': [0, 1], 'запад': [-1, 0], 'юг': [0, -1], 'восток': [1, 0]}
n = int(input())
xy = [0, 0]
direction = [input().split() for i in range(n)]
for side, dist in direction:
    distance = [elem * int(dist) for elem in d[side]]
    xy = [x + y for x, y in zip(xy, distance)]
for elem in xy:
    print(elem, end=" ")