class Stack:
    mas = []

    def __init__(self):
        pass

    def push(self, el):
        Stack.mas.append(el)

    def pop(self):
        value = Stack.mas[-1]
        Stack.mas.pop(-1)
        return value

    def peek(self):
        return Stack.mas[-1]

    def is_empty(self):
        if len(Stack.mas) == 0:
            return True
        else:
            return False
