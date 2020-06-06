# Write your code here
class CoffeeMachine:
    def __init__(self):
        self.water = 400
        self.milk = 540
        self.beans = 120
        self.cups_amount = 9
        self.money = 550

    def buy(self):
        coffee_id = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:\n")
        if coffee_id == '1':
            if self.water >= 250 and self.beans >= 16 and self.cups_amount > 0:
                self.water -= 250
                self.beans -= 16
                self.money += 4
                self.cups_amount -= 1
                print("I have enough resources, making you a coffee!")
            else:
                print("ERROR: not enough ingredients")
        elif coffee_id == '2':
            if self.water >= 350 and self.beans >= 20 and self.cups_amount > 0 and self.milk >= 75:
                self.water -= 350
                self.beans -= 20
                self.money += 7
                self.milk -= 75
                self.cups_amount -= 1
                print("I have enough resources, making you a coffee!")
            else:
                print("ERROR: not enough ingredients")
        elif coffee_id == '3':
            if self.water >= 200 and self.beans >= 12 and self.cups_amount > 0 and self.milk >= 100:
                self.water -= 200
                self.beans -= 12
                self.money += 6
                self.milk -= 100
                self.cups_amount -= 1
                print("I have enough resources, making you a coffee!")
            else:
                print("ERROR: not enough ingredients")
        elif coffee_id == "back":
            return 0
        else:
            print("ERROR: wrong argument")

    def show_info(self):
        # global water, milk, beans ,cups_amount ,money
        print("The coffee machine has:")
        print(self.water, " of water")
        print(self.milk, " of milk")
        print(self.beans, " of coffee beans")
        print(self.cups_amount, " of disposable cups")
        print(self.money, " of money")

    def fill(self):
        self.water += int(input("Write how many ml of water do you want to add:\n"))
        self.milk += int(input("Write how many ml of milk do you want to add:\n"))
        self.beans += int(input("Write how many grams of coffee beans do you want to add:\n"))
        self.cups_amount += int(input("Write how many disposable cups of coffee do you want to add:\n"))

    def take(self):
        print("I gave you", self.money)
        self.money = 0


coffee_machine = CoffeeMachine()
while True:
    action = input("Write action (buy, fill, take, remaining, exit):\n")
    if action == "exit":
        break
    elif action == "buy":
        coffee_machine.buy()
    elif action == "fill":
        coffee_machine.fill()
    elif action == "take":
        coffee_machine.take()
    elif action == "remaining":
        coffee_machine.show_info()
    else:
        print("Wrong action")
