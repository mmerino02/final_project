import random

#French Menu

from French import french_vocabulary

def f_menu():
    print(f"Bienvenu au French Language Center!")
    category = input(
        f"Which vocabulary category do you want to learn today? (colors, animals, professions, family, house, sports, school, food, clothes, body): ")
    category = category.lower()

    if category not in french_vocabulary:
        print(f"Sorry this category is not offered by our program. Please try again.")
        return
    rounds = int(input(f"How many rounds do you want to play? (Please insert the value as an integer): "))
    score = 0

    words = list(french_vocabulary[category].keys())
    random.shuffle(words)

    for i in range(rounds):
        word = words[i]
        translation = input("Translate '{}': ".format(word))

        if translation.lower() == french_vocabulary[category][word].lower():
            print(f"Correct!")
            score += 1
        else:
            print("Incorrect. The correct translation is '{}'.".format(french_vocabulary[category][word]))

    print("Total score: {}/{}".format(score, rounds))

    choice = input(f"Press 'M' to go back to the French menu or 'L' to go back to the language menu: ")
    if choice.lower() == "m":
        f_menu()
    elif choice.lower() == "l":
        l_menu()
    else:
        print(f"Invalid choice. Exiting...")


# Main Menu
def l_menu():
    print(f"Welcome to the Language Learning Center! What language do you want to learn today?")
    print(f"French (press F)")

    choice = input("I want to learn: ")
    choice = choice.lower()

    if choice == "f":
        f_menu()
    else:
        print(f"Sorry, {choice} is not offered by the Language Center. Exiting...")

l_menu()

