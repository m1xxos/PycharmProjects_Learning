word = input()
i = 0
for char in word:
    if char.isupper() == 1:
        word = word.replace(char, "_" + str(char.lower()), i)

    i += 1
print(word)
