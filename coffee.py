import math

print("This machine only takes 50p, 20p, 10p and 5p")


while True:
    current_value = int(input("Insert coin "))
    if current_value == 5 or current_value == 10 or current_value == 20 or current_value == 50:
        break
    else:
        print("Please enter a coin this machine accepts")


remaining = 75 - current_value


while current_value < 75:
    print(f"You still need to insert {remaining}p")
    
    while True:
        coins = int(input("Insert coin "))
        if coins == 5 or coins == 10 or coins == 20 or coins == 50:
            break
        else:
            print("Please enter a coin this machine accepts")
    
    current_value = current_value + coins
    remaining = 75 - current_value


print(f"Heres your coffee and your change of {-remaining}p")