import random
from gameOfCards.functions import sum_cards
from gameOfCards.user_game import choose_card, choose_deck, save_pc_cards

profile = random.randint(1, 4)
    
def computer_round(current_pc_hand):
    """
        Simulates the computer's turn on a random profile
    """
    
    pc_hand = list(current_pc_hand) # Create a Copy
    print("El perfil:", profile)
    sum_of_cards = sum_cards(pc_hand)

    if profile == 1: # Aggressive profile
        print("El perfil seleccionado es el 1")
        
        if sum_of_cards <= 18:
            should_draw = True
        elif 19 <= sum_of_cards <= 20:
            if random.randint(0, 1) == 1:
                print("Condicional 1: Pido una carta")
                should_draw = True
            else:
                print("Condicional 0 - Me planto")
                should_draw = False

        if sum_of_cards > 21 or sum_of_cards == 21:
            print("Ya no pido mas cartas")
            should_draw = False

        if should_draw:
            deck = choose_deck()
            card = choose_card(deck)
            pc_hand = save_pc_cards(card, pc_hand)
            sum_of_cards = sum_cards(pc_hand)

    elif profile == 2: # Cautious profile
        print("El perfil seleccionado es el 2")
        if sum_of_cards <= 15:
            deck = choose_deck()
            card = choose_card(deck)
            pc_hand = save_pc_cards(card, pc_hand)
            sum_of_cards = sum_cards(pc_hand)

    elif profile == 3: # Mixed profile
        print("El perfil seleccionado es el 3")
        
        if sum_of_cards <= 15:
            should_draw = True
        elif 16 <= sum_of_cards <= 19:
            if random.randint(0, 1) == 1:
                print("Condicional 1: Pido una carta")
                should_draw = True
            else:
                print("Condicional 0 - Me planto")
                should_draw = False
        else:  # >= 20
            should_draw = False

        if should_draw:
            deck = choose_deck()
            card = choose_card(deck)
            pc_hand = save_pc_cards(card, pc_hand)
            sum_of_cards = sum_cards(pc_hand)

    elif profile == 4: # Stand pat profile
        print("El perfil seleccionado es el 4")
        print("No pediré cartas, me planto con", sum_of_cards)

    print("La suma final del PC es:", sum_cards(pc_hand))
    print("Mano final del PC:", pc_hand)
    return pc_hand