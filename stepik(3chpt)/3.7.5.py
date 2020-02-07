data = {}
lst = []
for i in range(1, 12):
    data[i] = []
with open("dataset_3380_5.txt", 'r') as rfile:
    for aRow in rfile:
        lst.append(aRow.strip().split('\t'))
for grade, surname, height in lst:
    data[int(grade)].append(int(height))
for key, value in data.items():
    if not data[key]:
        print(key, '-')
    else:
        average = float(sum(data[key])/len(data[key]))
        print(key, average)