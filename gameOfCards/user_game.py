import random

def choose_deck():
    """
    Function to choose the deck of cards randomly.
    """
    
    def cards_deck(option):
        """
        Function with the deck of cards.
        """
        if option == 1:
            hearts = ['2H', '3H', '4H', '5H', '6H', '7H', '8H',
                    '9H', '10H', 'JH', 'QH', 'KH', 'AH']
            return hearts
        if option == 2:
            diamonds = ['2D', '3D', '4D', '5D', '6D', '7D', '8D',
                    '9D', '10D', 'JD', 'QD', 'KD', 'AD']
            return diamonds
        if option == 3:
            clover = ['2C', '3C', '4C', '5C', '6C', '7C', '8C',
                '9C', '10C', 'JC', 'QC', 'KC', 'AC']
            return clover
        if option == 4:
            spades = ['2S', '3S', '4S', '5S', '6S', '7S', '8S',
                '9S', '10S', 'JS', 'QS', 'KS', 'AS']
            return spades
        
    deck_chose = random.randint(1, 4)
    print(f"Deck chosen: {deck_chose}")
    selected_cards = cards_deck(deck_chose)
    return selected_cards

def choose_card(list_cards):
    """
    Function to choose a card randomly from the deck (list of cards).
    """
    card = random.randint(0, len(list_cards)-1)
    selected_card = list_cards[card]
    print(f"Card chosen: {selected_card}")
    
    return selected_card

def save_pc_cards(card, pc_cards):
    """
    Function to save the cards of the computer in a list.
    """
    i = 0
    while i < len(pc_cards):
        if card == pc_cards[i]:
            print("Card already exists in the list.")
            return pc_cards
        i += 1
    pc_cards += [card]
    print(f"PC cards: {pc_cards}")
    return pc_cards

def save_user_cards(card, user_cards):
    """
        Function to save the cards of the user in a list
    """
    i = 0
    while i < len(user_cards):
        if card == user_cards[i]:
            print("Card already exists in the list.")
            # Recursive structure because before the card could repeat again and yea..., 
            new_card_list = request_card(user_cards) 
            return new_card_list
        i += 1
    user_cards += [card]
    print(f"Cartas de Usuario: {user_cards}")
    return user_cards

def request_card(user_cards):
    """
        Function to request a card from the deck and add it to a hand.
    """
    deck = choose_deck()
    card = choose_card(deck)

    # The list is modified
    updated_user_cards = save_user_cards(card, user_cards)
    print(updated_user_cards)
    return updated_user_cards


