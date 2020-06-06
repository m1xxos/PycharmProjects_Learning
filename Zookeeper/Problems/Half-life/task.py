n = int(input())
r = int(input())
answer = 0
while(n > r):
    n -= n/2
    answer += 12
print(answer)