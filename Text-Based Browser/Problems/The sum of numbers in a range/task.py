def range_sum(numbers, a, b):
    summ = 0
    for x in numbers:
        if a <= int(x) <= b:
            summ += int(x)
            # print(summ)
    return summ


numbers = input().split()
a, b = input().split()
print(range_sum(numbers, int(a), int(b)))
