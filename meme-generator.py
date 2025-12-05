import random

characters = ["Shahrukh Khan", "Virat Kohli", "Nirmala Sitharaman", "A group of cows", "Sachin Tendulkar", "Messi"]
places = ["in Vande bharat", "at swimming pool", "a plate of samosa", "a dozen of banana", "inside the toilet", "in a metro train", "in a running bus"]
actions = ["cancels", "rides", "eats", "runs", "sleeps", "reads", "drinks"]

def generate_meme():
    random_characters = random.choice(characters)
    random_places = random.choice(places)
    random_actions = random.choice(actions)

    print(f"BREAKING NEWS: {random_characters} {random_actions} {random_places}") 

while True:
    random_characters = random.choice(characters)
    random_places = random.choice(places)
    random_actions = random.choice(actions)

    headline = f" BREAKING NEWS: {random_characters} {random_actions} {random_places}"
    print("\n" + headline)

    user_input = input("\n Do you want a new headline? (y/n) ").strip().lower()

    if user_input == "n":
        print("\n Thanks for using the meme generator. Good Bye!!!")
        break