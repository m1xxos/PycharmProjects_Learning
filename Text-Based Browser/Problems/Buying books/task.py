n = int(input())
stack = []
new_stack = []
for i in range(n):
    action = input().split(" ", 1)
    if action[0] == "BUY":
        stack.append(action[1])
    elif action[0] == "READ":
        new_stack.append(stack[-1])
new_stack.reverse()
print(*new_stack, sep="\n")
