# write your code here
def show_matrix():
    print("---------")
    print(f'| {field[0][0]} {field[0][1]} {field[0][2]} |')
    print(f'| {field[1][0]} {field[1][1]} {field[1][2]} |')
    print(f'| {field[2][0]} {field[2][1]} {field[2][2]} |')
    print("---------")


def state_matrix(fields):
    # print(new_word.count("X"))
    # print(new_word.count("O"))
    wins = []
    # if new_word.count("X") + 1 == new_word.count("O") or new_word.count("X") == new_word.count("O") or \
    #       new_word.count("X") == new_word.count("O") + 1:
    # print(fields[].count(" "))
    if fields[0][0] == fields[0][1] == fields[0][2] != " " \
            or fields[0][0] == fields[1][0] == fields[2][0] != " ":
        wins.append(fields[0][0])
        # print(len(wins))
    if fields[1][0] == fields[1][1] == fields[1][2] != " " or \
            fields[0][0] == fields[1][1] == fields[2][2] != " " or \
            fields[0][2] == fields[1][1] == fields[2][0] != " " or \
            fields[0][1] == fields[1][1] == fields[2][1] != " ":
        wins.append(fields[1][1])
    if fields[2][0] == fields[2][1] == fields[2][2] != " " or\
            fields[0][2] == fields[1][2] == fields[2][2] != " ":
        wins.append(fields[2][2])
    if fields[0].count(" ") + fields[1].count(" ") + fields[2].count(" ") == 0 or len(wins) > 0:
        if len(wins) == 1:
            print(*wins[0], "wins")
            return 1
        elif len(wins) == 0:
            print("Draw")
            return 2
        # else:
        #    print("Impossible")
    else:
        return 0
    # else:
    #   print("Impossible")


def add_matrix(symbol):
    while True:
        coordinates = input("Enter the coordinates: ").split()
        try:
            x = int(coordinates[0]) - 1
            y = 3 - int(coordinates[1])
            if int(coordinates[0]) > 3 or int(coordinates[1]) > 3:
                print("Coordinates should be from 1 to 3!")
            elif field[y][x] != " ":
                print("This cell is occupied! Choose another one!")
            else:
                field[y][x] = symbol
                # print(field[int(coordinates[0]) - 1][int(coordinates[1]) - 1])
                return 0
        except ValueError:
            print("You should enter numbers!")


word = "         "
field = [[word[0], word[1], word[2]], [word[3], word[4], word[5]], [word[6], word[7], word[8]]]
move = 0
show_matrix()
while True:
    if move % 2 == 0:
        mover = "X"
    else:
        mover = "O"
    add_matrix(mover)
    show_matrix()
    if state_matrix(field) != 0:
        break
    move += 1
