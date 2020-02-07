dna = input()
cnt = 1
i = 1
dna_compr = ""
while i < len(dna):
    if dna[i-1] != dna[i]:
        dna_compr += dna[i-1] + str(cnt)
        cnt = 1
        i += 1
    else:
        cnt += 1
        i +=1
dna_compr += dna[len(dna) - 1] + str(cnt)
print(dna_compr)