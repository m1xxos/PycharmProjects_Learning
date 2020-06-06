amount = int(input())
answer = [0] * 20
k = 0
for i in range(amount):
    n = int(input())
    if n % 7 == 0:
        answer[k] = n ** 2
        k += 1
for i in range(k):
    print(answer[i])
