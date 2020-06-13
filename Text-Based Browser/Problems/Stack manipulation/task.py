n = int(input())
stack = []
for i in range(n):
    action = input().split()
    if action[0] == "PUSH":
        stack.append(action[1])
    elif action[0] == "POP":
        stack.pop()
stack.reverse()
print(*stack, sep="\n")
