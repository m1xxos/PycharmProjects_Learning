numbers = input()
new_numbers = [int(x) for x in numbers]
y = 0
i = 0
for x in new_numbers:
    y += x
    new_numbers[i] = y
    i += 1

print(new_numbers)
