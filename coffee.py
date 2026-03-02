import math

# This program takes an integer input and keeps it as an iteger the entire time
# When printing the results, or an updates in price, it uses a print(f) command to read the integer and output it
# Program should only accept an integer input at any point but should be able to check if input is or isn't an integer

print("This machine only takes 50p, 20p, 10p and 5p")


while True:
    try:
        current_value = int(input("Insert coin : "))
        if current_value == 5 or current_value == 10 or current_value == 20 or current_value == 50:
            break
        else:
            print("Please enter a coin this machine accepts")
    except ValueError:
        print("Invalid! Input must be a whole number")


remaining = 75 - current_value

while current_value < 75:
    coins = 0
    try:
        print(f"You still need to insert {remaining}p")
        
        while True:
            coins = int(input("Insert coin : "))
            if coins == 5 or coins == 10 or coins == 20 or coins == 50:
                break
            else:
                print("Please enter a coin this machine accepts")

    except ValueError:
        print("Invalid! Input must be a whole number")
    
    current_value = current_value + coins
    remaining = 75 - current_value


print(f"Heres your coffee and your change of {-remaining}p")