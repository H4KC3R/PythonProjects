data = []
with open("dataset_3363_4.txt", 'r') as rfile:
    lst = rfile.read().split()
for elem in lst:
    data += [elem.split(";")]
print(data)
for surname, math, physics, language in data:
    print((int(math) + int(physics) + int(language))/3)
print(sum(int(math) for surname, math, physics, language in data)/len(data), sum(int(physics) for surname, math, physics,language in data)/len(data),sum(int(language) for surname, math, physics, language in data)/len(data))
