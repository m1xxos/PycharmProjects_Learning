cats_amount = []
cafe_name = []
while True:
    cat = input()
    if cat == "MEOW":
        break
    else:
        cat = cat.split()
        cats_amount.append(int(cat[1]))
        cafe_name.append(cat[0])
print(cafe_name[cats_amount.index(max(cats_amount))])
