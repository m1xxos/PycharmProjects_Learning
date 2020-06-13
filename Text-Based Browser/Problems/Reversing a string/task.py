n = int(input())
my_stack = []
for i in range(0, n):
    my_stack.append(input())

# print(my_stack)
for i in range(0, n):
    print(my_stack.pop())
