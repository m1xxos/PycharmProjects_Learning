import random
rating = 0
new_file_text = []
player_id = 0


def check_state():
    global rating
    computer_option_name = options[computer_option]
    options_mid = (len(options) - 1) / 2
    new_options = []
    for i in range(human_option + 1, len(options)):
        new_options.append(options[i])
    for i in range(0, human_option):
        new_options.append(options[i])
    win_options = new_options[0:int(options_mid)]
    lose_options = new_options[int(options_mid):len(new_options)]
    if computer_option == human_option:
        print(f"There is a draw ({computer_option_name})")
        rating += 50
    elif computer_option_name in win_options:
        print(f"Sorry, but computer chose {computer_option_name}")
    elif computer_option_name in lose_options:
        print(f"Well done. Computer chose {computer_option_name} and failed")
        rating += 100


def check_file(player_name):
    global rating, new_file_text, player_id
    file_r = open("rating.txt", "r")
    file_text = file_r.readlines()
    file_r.close()
    for line in file_text:
        new_line = line.split()
        if new_line[0] == player_name:
            rating = int(new_line[1])
            player_id = int(file_text.index(line)) + 1
        new_file_text.append(new_line)


def create_file(player_name):
    global rating
    file_w = open("rating.txt", "w")
    if player_id != 0:
        new_file_text[player_id - 1][1] = rating
    else:
        new_file_text.append([player_name, rating])
    for line in new_file_text:
        print(*line, file=file_w)
    file_w.close()


options = ['rock', 'paper', 'scissors']
options_revers = []
name = input("Enter your name: ")
print(f"Hello, {name}")
check_file(name)
option_input = input()
print("Okay, let's start")
if option_input != "":
    options = option_input.split(",")
while True:
    option_input = input()
    computer_option = random.randint(0, len(options) - 1)
    if option_input == "!exit":
        break
    elif option_input == "!rating":
        print(f"Your rating: {rating}")
        continue
    try:
        human_option = options.index(option_input)
        check_state()
    except ValueError:
        print("Invalid input")
create_file(name)
print("Bye!")
