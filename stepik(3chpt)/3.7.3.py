n = int(input())
dictionary = [input().lower() for i in range(n)]
l = int(input())
sentences = [input().lower() for j in range(l)]
words = []
for sentence in sentences:
    words += sentence.split(" ")
words = set(words)
for word in words:
    if word not in dictionary:
        print(word)