import math

# This program takes an integer input and keeps it as an iteger the entire time
# When printing the results, or an updates in price, it uses a print(f) command to read the integer and output it
# Program should only accept an integer input at any point but should be able to check if input is or isn't an integer

def main():
    print("This machine only takes 50p, 20p, 10p and 5p")
    current = 0
    while current < 75:
        coin = get_coin()
        current = update_total(current, coin)
    dispense_product(current)
    

def get_coin():
    while True:
        try:
            current_value = int(input("Insert coin : "))
            if current_value == 5 or current_value == 10 or current_value == 20 or current_value == 50:
                break
            else:
                print("Please enter a coin this machine accepts")
        except ValueError:
            print("Invalid! Input must be a whole number")
    return current_value


def update_total(current, coin):
    current = current + coin
    remaining = 75 - current
    print(f"You still need to insert {remaining}p")
    return current


def dispense_product(current):
    remaining = 75 - current
    print(f"Heres your coffee and your change of {-remaining}p")

main()