# Write your code here
water = 400
milk = 540
beans = 120
cups_amount = 9
money = 550


def show_info():
    # global water, milk, beans ,cups_amount ,money
    print("The coffee machine has:")
    print(water, " of water")
    print(milk, " of milk")
    print(beans, " of coffee beans")
    print(cups_amount, " of disposable cups")
    print(money, " of money")


def buy():
    global water, milk, beans, cups_amount, money
    coffee_id = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:\n")
    if coffee_id == '1':
        if water >= 250 and beans >= 16 and cups_amount > 0:
            water -= 250
            beans -= 16
            money += 4
            cups_amount -= 1
            print("I have enough resources, making you a coffee!")
        else:
            print("ERROR: not enough ingredients")
    elif coffee_id == '2':
        if water >= 350 and beans >= 20 and cups_amount > 0 and milk >= 75:
            water -= 350
            beans -= 20
            money += 7
            milk -= 75
            cups_amount -= 1
        else:
            print("ERROR: not enough ingredients")
    elif coffee_id == '3':
        if water >= 200 and beans >= 12 and cups_amount > 0 and milk >= 100:
            water -= 200
            beans -= 12
            money += 6
            milk -= 100
            cups_amount -= 1
        else:
            print("ERROR: not enough ingredients")
    elif coffee_id == "back":
        return 0
    else:
        print("ERROR: wrong argument")


def fill():
    global water, milk, beans, cups_amount, money
    water += int(input("Write how many ml of water do you want to add:\n"))
    milk += int(input("Write how many ml of milk do you want to add:\n"))
    beans += int(input("Write how many grams of coffee beans do you want to add:\n"))
    cups_amount += int(input("Write how many disposable cups of coffee do you want to add:\n"))


def take():
    global money
    print("I gave you", money)
    money = 0


while True:
    action = input("Write action (buy, fill, take, remaining, exit):\n")
    if action == "exit":
        break
    elif action == "buy":
        buy()
    elif action == "fill":
        fill()
    elif action == "take":
        take()
    elif action == "remaining":
        show_info()
    else:
        print("Wrong action")
