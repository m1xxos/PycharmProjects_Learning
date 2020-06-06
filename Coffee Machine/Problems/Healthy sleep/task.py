min_sleep = int(input())
max_sleep = int(input())
ann_sleep = int(input())
if ann_sleep < min_sleep:
    print("Deficiency")
elif ann_sleep > max_sleep:
    print("Excess")
else:
    print("Normal")
