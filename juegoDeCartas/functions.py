import random
import user_game
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
    print(f"Selected cards: {selected_cards}")
    
    return selected_cards
        


def choose_card(list_cards):
    """
    Function to choose a card randomly from the deck (list of cards).
    """
    
    card = random.randint(0, len(list_cards)-1)
    selected_card = list_cards[card]
    print(f"Card chosen: {selected_card}")
    
    return selected_card

    
pc_cards = []

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
    Function to save the cards of the user in a list.
    """
    i = 0
    while i < len(user_cards):
        if card == user_cards[i]:
            print("Card already exists in the list.")
            new_card=user_game.request_card()
            user_cards += [new_card]
            return user_cards
            
        i += 1

    
    user_cards += [card]
    print(f"Cartas de Usuario: {user_cards}")
    return user_cards
            
            
def sum_cards(cards):
    """
    Function to sum the values of the cards in a list.
    """
    if cards == []:
        return 0
    
    total = 0
    i = 0
    has_ace = False  

    while i <= len(cards) - 1:
        if (cards[i] == 'JH' or cards[i] == 'JD' or 
            cards[i] == 'JC' or cards[i] == 'JS'):
            total += 10

        elif (cards[i] == 'QH' or cards[i] == 'QD' or
              cards[i] == 'QC' or cards[i] == 'QS'):
            total += 10

        elif (cards[i] == 'KH' or cards[i] == 'KD' or 
              cards[i] == 'KC' or cards[i] == 'KS'):
            total += 10

        elif (cards[i] == 'AH' or cards[i] == 'AD' or 
              cards[i] == 'AC' or cards[i] == 'AS'):
            total += 1
            has_ace = True  

        elif (cards[i] == '10H' or cards[i] == '10D' or 
              cards[i] == '10C' or cards[i] == '10S'):
            total += 10

        else:
            total += int(cards[i][0])

        i += 1

    if has_ace == True and total <= 10:
        total += 10
    
    return total

def check_points(cards_list):
    """
    Function to check the type of points in the list.
    """
    num_aces = 0
    num_figures = 0
    num_small_cards = 0
    num_sevens = 0
    five_of_diamonds = 0
    i = 0

    # Verificar si la primera carta es 5 de rombos
    if len(cards_list) > 0 and cards_list[0] == "5D":
        five_of_diamonds += 1

    # Solo si no se pasa de 21
    if sum_cards(cards_list) <= 21:
        while i < len(cards_list):
            card = cards_list[i]

            # Si es 10 (porque empieza con "1" y segundo carácter es "0")
            if len(card) >= 2 and card[0] == "1" and card[1] == "0":
                num_small_cards += 1

            elif card[0] == "A":
                num_aces += 1

            elif card[0] == "7":
                num_sevens += 1
                print("Se agrega un 7;", num_sevens)

            elif card[0] == "J" or card[0] == "Q" or card[0] == "K":
                num_figures += 1

            elif (card[0] == "2" or card[0] == "3" or card[0] == "4" or
                  card[0] == "5" or card[0] == "6" or card[0] == "8" or
                  card[0] == "7" or card[0] == "9"):
                num_small_cards += 1
                print("Num cartas menores;", num_small_cards)

            i += 1

        total = sum_cards(cards_list)
        points = 0

        if total == 21 and num_sevens == 3:
            print("Triple 7")
            points += 5
        if num_aces == 2 and len(cards_list) == 2:
            print("Doble As")
            points += 4
        if five_of_diamonds == 1:
            print("5 de rombos")
            points += 3
        if len(cards_list) == 5 and num_figures == 0:
            print("5 menores")
            points += 2
        if total == 21 and num_figures >= 1 and num_aces >= 1 and len(cards_list) == 2:
            print("21 Duro (Black Jack)")
            points += 1
        if total == 21:
            print("21 Suave")
            points += 1
        if points == 0:
            print("Sin combinación especial")

    print(points)
    return points    