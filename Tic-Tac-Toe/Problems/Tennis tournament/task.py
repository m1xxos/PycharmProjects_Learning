n = int(input())
winners = []
win_count = 0
for i in range(n):
    string = input()
    string = string.split()
    if string[1] == "win":
        winners.append(string[0])
        win_count += 1
print(winners)
print(win_count)
