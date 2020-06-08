dictionary = ['all', 'an', 'and', 'as', 'closely', 'correct', 'equivocal',
              'examine', 'indication', 'is', 'means', 'minutely', 'or', 'scrutinize',
              'sign', 'the', 'to', 'uncertain']
sentence = input().split()
misspells = 0
for word in sentence:
    if word not in dictionary:
        print(word)
        misspells += 1
if misspells == 0:
    print("OK")
print(sentence)
