genome = input().upper()
n = len(genome)
numg = genome.count('G')
numc = genome.count('C')
print((numc + numg)/n * 100)