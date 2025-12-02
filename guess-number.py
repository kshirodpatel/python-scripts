import random
MIN_NUMBER = 10 # Min Number to guess
MAX_NUMBER = 200 # Max Number to guess
MAX_CHANCE = 5 # Max chance a user will get to guess
computer_picks = random.randint(MIN_NUMBER, MAX_NUMBER)
user_chance = 0
while True:
    user_picks = input(f"Please select a number in between {MIN_NUMBER} and {MAX_NUMBER}, You have {MAX_CHANCE} chance: ")

    if not user_picks.isdigit():
        print("You need to select a number")
        break
    
    user_picks = int(user_picks)

    if user_chance == MAX_CHANCE:
        print('You have consumed all the chance')
        break

    if computer_picks > user_picks :
        print(f"You selected a lower number, You have {MAX_CHANCE - user_chance} chances left  ")
        user_chance += 1;
    elif user_picks > computer_picks:
        print(f"You selected a large number, You have {MAX_CHANCE - user_chance} chances left")
        user_chance += 1;
    else:
        print("You won")
        break