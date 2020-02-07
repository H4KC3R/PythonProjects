cypher1 = input()
cypher2 = input()
message1 = input()
message2 = input()
coding = ''
decoding = ''
for char in message1:
    if char in cypher1:
        coding += cypher2[cypher1.index(char)]
    else:
        coding += char
for char in message2:
    if char in cypher2:
        decoding += cypher1[cypher2.index(char)]
    else:
        coding += char
print(coding)
print(decoding)