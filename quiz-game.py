questions = ("What is the chemical symbol for water: ",
             "Which planet is known as the Red Planet: "
             "What gas do plants absorb during photosynthesis: ",
             "What is the center of an atom called: ",
             "Which organ pumps blood through the human body: ",
             "What force keeps us on the ground: ",
             "What is the boiling point of water at sea level: ",
             "Which part of the plant carries out photosynthesis: ",
             "What is the largest planet in our solar system: ",
             "What do humans breathe in to survive: "
             )

options = (("A. CO₂", "B. H₂O", "C. O₂", "D. H₂"),
           ("A. Venus", "B. Mars", "C. Jupiter", "D. Mercury"),
           ("A. Oxygen", "B. Nitrogen", "C. Carbon dioxide", "D. Helium"),
           ("A. Electron", "B. Neutron", "C. Nucleus", "D. Proton"),
           ("A. Brain", "B. Heart", "C. Liver", "D. Kidney"),
           ("A. Magnetism", "B. Friction", "C. Gravity", "D. Pressure"),
           ("A. 50°C", "B. 75°C", "C. 100°C", "D. 150°C"),
           ("A. Roots", "B. Stem", "C. Flower", "D. Leaves"),
           ("A. Earth", "B. Saturn", "C. Jupiter", "D. Neptune"),
           ("A. Carbon monoxide", "B. Oxygen", "C. Hydrogen", "D. Argon")
           )

answers = ("B", "B", "C", "C", "B", "C", "C", "D", "C", "B")

guesses = []
score = 0
question_num = 0

for question in questions:
    print("--------------------")
    print(f"{question_num+1}. {question}")
    for option in options[question_num]:
        print(option, end=", ")
    guess = input("Enter (A, B, C, D): ").strip().upper()
    guesses.append(guess)
    print(answers[question_num])
    if guess == answers[question_num]:
        score += 1
        print("Correct answer")
    else:
        print("Incorrect answer")
    question_num += 1
    print()
print("-------------------------------")
print(f"You scored {score} out of 10")
print("-------------------------------")