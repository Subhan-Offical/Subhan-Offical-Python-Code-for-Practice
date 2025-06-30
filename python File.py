import random
def roll_dice():
    return random.randint(1, 6)
while True:
    input("Press Enter to roll the dice....")
    print("Your tolled:", roll_dice())
    again = input("Roll again? (y/s): ")
    if again.lower() != 'y':
        break


