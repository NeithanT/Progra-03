import random
import functions

# Function for the computer's turn
def computer_round():
    list_cards = []
    user_cards = []  # List to store the computer's cards
    profile = random.randint(1, 4)
    print("El perfil:", profile)
    sum_cards = 0

    if profile == 1:
        print("El perfil seleccionado es el 1")
        while True:
            deck = functions.choose_deck()
            card = functions.choose_card(deck)

            if sum_cards <= 18 or sum_cards == 0:
                list_cards = functions.save_pc_cards(card, user_cards)
                sum_cards = functions.sum_cards(user_cards)
                print(list_cards)

            elif sum_cards >= 19 and sum_cards <= 20:
                conditional = random.randint(0, 1)  # Random decision
                if conditional == 1:
                    print("Condicional 1: Pido una carta")
                    list_cards = functions.save_pc_cards(card, user_cards)
                    sum_cards = functions.sum_cards(user_cards)
                    print(list_cards)
                else:
                    print("Condicional 0")
                    print("No pido más cartas, me planto")
                    break

            if sum_cards == 21:
                print("No pido más cartas, tengo 21")
                break

            elif sum_cards > 21:
                print("Demasiadas cartas, tienes", sum_cards)
                break

    # Profile 2 logic
    elif profile == 2:
        print("El perfil seleccionado es el 2")
        while True:
            deck = functions.choose_deck()
            card = functions.choose_card(deck)

            if sum_cards <= 15 or sum_cards == 0:
                list_cards = functions.save_pc_cards(card, user_cards)
                sum_cards = functions.sum_cards(user_cards)
                print(list_cards)

            elif sum_cards >= 16 and sum_cards <= 21:
                print("No pido más cartas, me quedo con", sum_cards)
                break

            elif sum_cards > 21:
                print("Demasiadas cartas, tienes", sum_cards)
                break

    # Profile 3 logic
    elif profile == 3:
        print("El perfil seleccionado es el 3")
        while True:
            deck = functions.choose_deck()
            card = functions.choose_card(deck)

            if sum_cards <= 15 or sum_cards == 0:
                list_cards = functions.save_pc_cards(card, user_cards)
                sum_cards = functions.sum_cards(user_cards)
                print(list_cards)

            elif sum_cards >= 16 and sum_cards <= 19:
                conditional = random.randint(0, 1)
                if conditional == 1:
                    print("Condicional 1: Pido una carta")
                    list_cards = functions.save_pc_cards(card, user_cards)
                    sum_cards = functions.sum_cards(user_cards)
                    print(list_cards)
                else:
                    print("Condicional 0")
                    print("No pido más cartas, me planto")
                    break

            elif sum_cards == 20 or sum_cards == 21:
                print("No pido más cartas, tengo", sum_cards)
                break

            elif sum_cards > 21:
                print("Demasiadas cartas, tienes", sum_cards)
                break

    # Profile 4 logic
    elif profile == 4:
        print("El perfil seleccionado es el 4")
        print("No pediré cartas, me planto con", sum_cards)

    print("La suma final es:", sum_cards)
    print(list_cards)
    return list_cards
