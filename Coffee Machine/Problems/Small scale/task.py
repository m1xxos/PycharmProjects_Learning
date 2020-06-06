numbers = []
i = 0
while True:
    number = input()
    if number != '.':
        numbers.append(float(number))
        i += 1
    else:
        break
print(min(numbers))
