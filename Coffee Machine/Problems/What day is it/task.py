time = input()
if 10.30 + float(time) <= 0:
    print("Monday")
elif 10.30 + float(time) >= 24:
    print("Wednesday")
else:
    print("Tuesday")

