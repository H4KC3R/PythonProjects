n = int(input())
lst = [input() for i in range(n)]
teams = dict()
matches = []
for elem in lst:
    matches += [elem.split(";")]
print(matches)
for team1, result1, team2, result2 in matches:
    teams[team1] = [0, 0, 0, 0, 0]
    teams[team2] = [0, 0, 0, 0, 0]
for team1, result1, team2, result2 in matches:
    if int(result1) > int(result2):
        teams[team1] = [x + y for x, y in zip([1, 1, 0, 0, 2], teams[team1])]
        teams[team2] = [x + y for x, y in zip([1, 0, 0, 1, 0], teams[team2])]
    elif int(result1) == int(result2):
        teams[team1] = [x + y for x, y in zip([1, 0, 1, 0, 1], teams[team1])]
        teams[team2] = [x + y for x, y in zip([1, 0, 1, 0, 1], teams[team2])]
    elif int(result1) < int(result2):
        teams[team1] = [x + y for x, y in zip([1, 0, 0, 1, 0], teams[team1])]
        teams[team2] = [x + y for x, y in zip([1, 1, 0, 0, 2], teams[team2])]
for keys, values in teams.items():
    print(keys, end=":")
    for value in values:
        print(value, end=" ")
    print()