deposit = int(input())
year_counter = 0
while deposit <= 700000:
    deposit += deposit * 0.071
    year_counter += 1
print(year_counter)
