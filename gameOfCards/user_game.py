import random


def choose_deck():
    """
    Choose a random deck of cards among four suits 
    (hearts, diamonds, clovers, spades).
    
    E: None
    S: list:A list containing 13 cards from one
    randomly selected suit.
    R: None
    """

    def cards_deck(option):
        """
        Return the list of cards corresponding to the selected suit.

        E: option (int): An integer between 1 and 4, inclusive.
        S: list - A list of 13 cards (strings) corresponding to the selected suit:
                  1 -> Hearts, 2 -> Diamonds, 3 -> Clovers, 4 -> Spades
        R: option must be an integer between 1 and 4. 
           Other values will raise a error.
        """
        if not isinstance(option, int):
            return "Error: the option must be an integer"

        elif option < 1 or option > 4:
            return "Error: the option must be between 1 and 4"
        
        elif option == 1:
            return ['2H', '3H', '4H', '5H', '6H', '7H', '8H',
                    '9H', '10H', 'JH', 'QH', 'KH', 'AH']
        elif option == 2:
            return ['2D', '3D', '4D', '5D', '6D', '7D', '8D',
                    '9D', '10D', 'JD', 'QD', 'KD', 'AD']
        elif option == 3:
            return ['2C', '3C', '4C', '5C', '6C', '7C', '8C',
                    '9C', '10C', 'JC', 'QC', 'KC', 'AC']
        elif option == 4:
            return ['2S', '3S', '4S', '5S', '6S', '7S', '8S',
                    '9S', '10S', 'JS', 'QS', 'KS', 'AS']

    deck_chose = random.randint(1, 4)
    print(f"Deck chosen: {deck_chose}")
    selected_cards = cards_deck(deck_chose)
    return selected_cards


def choose_card(list_cards):
    """
    Function to choose a card randomly from the deck (list of cards).

    E: list_cards (list):A non-empty list containing card strings.
    S: str - One card selected at random from the list.
    R: list_cards must be list type.
    """
    if not isinstance(list_cards, list):
        return "Error: input must be a list"
    
    card = random.randint(0, len(list_cards)-1)
    selected_card = list_cards[card]
    print(f"Carta elegida: {selected_card}")
    
    return selected_card

def save_pc_cards(card, pc_cards):
    """
    Function to save the cards of the computer in a list.

    E: card (str), pc_cards (list): card to save, and list where the card will be stored
    S: list: the updated list with the new card if it was not already present
    R: card must be a string, pc_cards must be a list of strings, and the same
    card cannot be added twice
    """
    if not isinstance(card, str):
        return "Error: card must be a string"
    
    if not isinstance(pc_cards, list):
        return "Error: pc_cards must be a list"
    
    card_exists = False

    # Check if the card is already in pc_cards
    for c in pc_cards:
        if card == c:
            card_exists = True
            print("La carta ya existe en la lista.")
            break

    # While the card exists, keep requesting a new one until it's unique
    while card_exists:
        card = request_card(pc_cards)
        card_exists = False
        for c in pc_cards:
            if card == c:
                card_exists = True
                print("La carta ya existe en la lista.")
                break

    # Add the card to the list 
    pc_cards += [card]
    print(f"Cartas de Usuario: {pc_cards}")
    return pc_cards

def save_user_cards(card, user_cards):
    """
    Function to save the cards of the user in a list

    E: card (str), user_cards (list): card to be saved and list of the user's 
    current cards
    S: list: the updated list with the new card, after ensuring no duplicates
    R: card must be a string, user_cards must be a list of strings, and the same
    card cannot be added twice
    """
    if not isinstance(card, str):
        return "Error: card must be a string"
    
    if not isinstance(user_cards, list):
        return "Error: user_cards must be a list"

    card_exists = False

    # Check if the card is already in user_cards
    for c in user_cards:
        if card == c:
            card_exists = True
            print("La carta ya existe en la lista.")
            break

    # While the card exists, request a new one until it's unique
    while card_exists:
        card = request_card(user_cards)
        card_exists = False
        for c in user_cards:
            if card == c:
                card_exists = True
                print("La carta ya existe en la lista.")
                break

    # Add the new card to the list 
    user_cards += [card]
    print(f"Cartas de Usuario: {user_cards}")
    return user_cards


def request_card(user_cards):
    """
    Function to request a card from the deck and add it to a hand.

    E: user_cards (list):current list of user's cards
    S: list: the updated list with one new card added, making sure it's not duplicated
    R: user_cards must be a list
    """
    if not isinstance(user_cards, list):
        return "Error: user_cards must be a list"

    deck = choose_deck()
    card = choose_card(deck)

    # The list modified
    updated_user_cards = save_user_cards(card, user_cards)
    print(updated_user_cards)
    return updated_user_cards

