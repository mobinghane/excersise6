n = int(input())
sentence = input().split()
word = input().strip()

for i in sentence:
    if i.endswith("_"):
        i = i[:-1]
    if len(i) != len(word):
        i += "_" * (len(word) - len(i))
    if sum([i[j] != word[j] for j in range(len(word))]) <= n:
        print(i)

