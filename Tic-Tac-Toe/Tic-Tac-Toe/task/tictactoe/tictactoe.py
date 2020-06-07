# write your code here
def show_matrix(fields):
    print("---------")
    print(f'| {fields[0]} {fields[1]} {fields[2]} |')
    print(f'| {fields[3]} {fields[4]} {fields[5]} |')
    print(f'| {fields[6]} {fields[7]} {fields[8]} |')
    print("---------")


def state_matrix(fields, new_word):
    # print(new_word.count("X"))
    # print(new_word.count("O"))
    wins = []
    gfn = 0
    if new_word.count("X") + 1 == new_word.count("O") or new_word.count("X") == new_word.count("O") or \
            new_word.count("X") == new_word.count("O") + 1:
        if fields[0][0] == fields[0][1] == fields[0][2] or fields[0][0] == fields[1][0] == fields[2][0]:
            wins.append(fields[0][0])
            # print(len(wins))
        if (fields[1][0] == fields[1][1] == fields[1][2]) or (fields[0][0] == fields[1][1] == fields[2][2]) or \
                (fields[0][2] == fields[1][1] == fields[2][0]) or fields[0][1] == fields[1][1] == fields[2][1]:
            wins.append(fields[1][1])
        if fields[2][0] == fields[2][1] == fields[2][2] or fields[0][2] == fields[1][2] == fields[2][2]:
            wins.append(fields[2][2])
        if new_word.count("X") + new_word.count("O") == 9 or len(wins) > 0:
            if len(wins) == 1:
                print(*wins[0], "wins")
            elif len(wins) == 0:
                print("Draw")
            else:
                print("Impossible")
        else:
            print("Game not finished")
    else:
        print("Impossible")


word = input("Enter cells:")
field = [[[word[0]], [word[1]], [word[2]]], [[word[3]], [word[4]], [word[5]]], [[word[6]], [word[7]], [word[8]]]]
show_matrix(word)
state_matrix(field, word)
