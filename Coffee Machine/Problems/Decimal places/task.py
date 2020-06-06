number = float(input())
rounder = int(input())
new_number = float(number) - int(number)
print(f'{number:.{rounder}f}')
