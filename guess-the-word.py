import random

FRUITS = ["Apple", "Banana", "Mango", "Orange", "Pineapple", "Grapes", "Papaya", "Watermelon",
    "Muskmelon", "Strawberry", "Blueberry", "Raspberry", "Blackberry", "Kiwi", "Guava",
    "Pomegranate", "Cherry", "Peach", "Plum", "Pear", "Lychee", "Dragonfruit", "Apricot",
    "Fig", "Coconut", "Avocado", "Lemon", "Lime", "Tangerine", "Grapefruit", "Jackfruit",
    "Starfruit", "Passionfruit", "Custard Apple", "Sapota", "Mulberry", "Cranberry",
    "Dates", "Persimmon", "Nectarine", "Olive", "Jujube", "Longan", "Rambutan", "Durian",
    "Breadfruit", "Tamarind", "Gooseberry", "Blackcurrant", "Redcurrant"]
VEGETABLES = [
    "Potato", "Tomato", "Onion", "Garlic", "Ginger", "Carrot", "Beetroot", "Radish",
    "Cabbage", "Cauliflower", "Broccoli", "Spinach", "Lettuce", "Kale", "Peas",
    "Green Beans", "Brinjal", "Okra", "Bitter Gourd", "Bottle Gourd", "Pumpkin",
    "Zucchini", "Cucumber", "Capsicum", "Chili Pepper", "Sweet Potato", "Yam",
    "Turnip", "Celery", "Asparagus", "Leek", "Mushroom", "Corn", "Artichoke",
    "Fennel", "Parsley", "Coriander", "Mint", "Dill", "Spring Onion", "Chives",
    "Drumstick", "Cluster Beans", "Fenugreek Leaves", "Mustard Greens", "Arugula",
    "Swiss Chard", "Radicchio", "Watercress", "Taro"
]
COUNTRIES = ["India", "United States", "United Kingdom", "Canada", "Australia", "Germany",
    "France", "Italy", "Spain", "Portugal", "Netherlands", "Belgium", "Switzerland",
    "Austria", "Sweden", "Norway", "Denmark", "Finland", "Russia", "China",
    "Japan", "South Korea", "Brazil", "Argentina", "Mexico", "Chile", "Colombia",
    "Peru", "South Africa", "Egypt", "Nigeria", "Kenya", "Ethiopia", "Saudi Arabia",
    "United Arab Emirates", "Turkey", "Israel", "Iran", "Iraq", "Thailand",
    "Vietnam", "Indonesia", "Malaysia", "Singapore", "Philippines", "New Zealand",
    "Bangladesh", "Pakistan", "Sri Lanka"]

print("Welcome to the Guess The Word game")
category_selection = input('''
    Choose the category to play
    Type (1) for Fruits
    (2) for Vegetables
    (3) for Countries
    (q) for quit the game
''')

if category_selection == 'q':
    print("You quit the game, Bye!!!")
elif category_selection == '1':
    secret = random.choice(FRUITS)
elif category_selection == '2':
    secret = random.choice(VEGETABLES)
elif category_selection == '3':
    secret = random.choice(COUNTRIES)
else:
    print("Invalid selection")

attempts = 0
print("\n Guess the secret password")

while True:
    print(secret)
    guess = input("Enter your guess: ").title()
    attempts += 1

    if guess == secret:
        print("You won the game")
        break

    hint = ""
    for i in range(len(secret)):
        if i < len(guess) and guess[i] == secret[i]:
            hint += guess[i]
        else:
            hint += "_"
    print(hint)        