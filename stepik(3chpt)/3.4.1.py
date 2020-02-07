genome = []
letter = []
number = ""
with open("dataset_3363_2.txt", 'r') as rfile:
    line = rfile.readline().strip()
for i in range(len(line)):
    if line[i].isalpha():
        letter = line[i]
        number = '0'
    elif (i+1 in range(len(line))) and (not line[i+1].isalpha()):
        number += line[i]
    else:
        number += line[i]
        genome.append(letter*int(number))
with open("dataset_3363_2.txt", 'w') as wfile:
    for letter in genome:
        wfile.write(str(letter))