
def sum_cards(cards):
    """
    Function to calculate the total value of a list of cards.

    E: cards (list): list of card strings -> ['5H', '10S', 'AD']
    S: int: total value of the cards based on Blackjack rules
    R: cards must be a list of strings representing valid cards
    """
    if not isinstance(cards, list):
        return "Error: cards must be a list"

    total = 0
    ace_count = 0
    i = 0

    while i < len(cards):
        card = cards[i]
        
        # Jacks
        if (card == 'JH' or card == 'JD' or card == 'JC' or card == 'JS'):
            total += 10
        # Queens
        elif (card == 'QH' or card == 'QD' or card == 'QC' or card == 'QS'):
            total += 10
        # Kings
        elif (card == 'KH' or card == 'KD' or card == 'KC' or card == 'KS'):
            total += 10
        # Aces
        elif (card == 'AH' or card == 'AD' or card == 'AC' or card == 'AS'):
            total += 1
            ace_count += 1
        # Tens
        elif (card == '10H' or card == '10D' or card == '10C' or card == '10S'):
            total += 10
        # Numbers 2–9
        else:
            total += int(card[0])
        
        i += 1

    if ace_count > 0 and total + 10 <= 21:
        total += 10

    return total

def check_points(cards_list):
    """
    Function to check the type of points in the list.

    E: cards_list (list) - list of card strings (e.g., '7H', 'AD')
    S: int - point type according to special card combinations
             5 -> Triple 7
             4 -> Double Ace
             3 -> 5 of Diamonds starts the hand
             2 -> Five small cards without figures
             1 -> 21 (Blackjack or soft)
             0 -> No special combination
    R: cards_list must be a list of card strings
    """
    if not isinstance(cards_list, list):
        return "Error: cards_list must be a list"
    
    num_aces = 0
    num_figures = 0
    num_small_cards = 0
    num_sevens = 0
    five_of_diamonds = 0
    i = 0

    # Verify is the first card is 5 of diamonds
    if len(cards_list) > 0 and cards_list[0] == "5D":
        five_of_diamonds += 1

    #  Check if it does not go over 21
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

        if total == 21 and num_sevens == 3:
            print("Triple 7")
            return 5
        if num_aces == 2 and len(cards_list) == 2:
            print("Doble As")
            return 4
        if five_of_diamonds == 1:
            print("5 de rombos")
            return 3
        if len(cards_list) == 5 and num_figures == 0:
            print("5 menores")
            return 2
        if total == 21 and num_figures >= 1 and num_aces >= 1 and len(cards_list) == 2:
            print("21 Duro (Black Jack)")
            return 1
        if total == 21:
            print("21 Suave")
            return 1
        else:
            print("Sin combinación especial")
            return 0
        
def total_winner(cards_user, cards_pc):
    """
    Determines the winner by first comparing special points (check_points).
    If there is a tie in special points, then compares the sums and standard Blackjack rules.

    Returns:
    0 -> both lost (busted)
    1 -> PC wins
    2 -> User wins
    3 -> tie
    """
    if not isinstance(cards_user, list):
        return "Error: cards_user must be a list"
    if not isinstance(cards_pc, list):
        return "Error: cards_pc must be a list"

    # Get special points
    user_special = check_points(cards_user)
    pc_special = check_points(cards_pc)

    # First: if one has higher special points, they win
    if user_special == None:
        user_special=0
        
    if pc_special == None:
        pc_special=0
        
    if pc_special > user_special:
        print("PC gana por puntos especiales mayores")
        return 1
    elif user_special > pc_special:
        print("Usuario gana por puntos especiales mayores")
        return 2
    else:
        # Tie in special points, now compare sums normally
        user_sum = sum_cards(cards_user)
        pc_sum = sum_cards(cards_pc)

        # Both busted
        if user_sum > 21 and pc_sum > 21:
            print("Ambos se pasaron")
            return 0

        # Only user busted
        if user_sum > 21:
            print("Gana PC porque usuario se pasó")
            return 1

        # Only PC busted
        if pc_sum > 21:
            print("Gana usuario porque PC se pasó")
            return 2

        # Both have 21, use winner function for tie-break
        if user_sum == 21 and pc_sum == 21:
            return winner(cards_user, cards_pc)

        # One has 21
        if user_sum == 21:
            return 2
        if pc_sum == 21:
            return 1

        # Closest to 21 wins
        if user_sum > pc_sum:
            return 2
        if pc_sum > user_sum:
            return 1

        # Tie by same score
        return 3

    
    
def winner(cards_user, cards_pc):
    """
    Function to decide the winner based on Blackjack rules.

    E: cards_user (list), cards_pc (list) - lists of card strings for user and PC
    S: int - result of the comparison:
             1 -> PC wins
             2 -> User wins
             3 -> tie
    R: both cards_user and cards_pc must be lists of card strings
    """
    if not isinstance(cards_user, list):
        return "Error: cards_user must be a list"
    
    if not isinstance(cards_pc, list):
        return "Error: cards_pc must be a list"
    
    user_points = check_points(cards_user)
    pc_points = check_points(cards_pc)

    if pc_points > user_points:
        print("La computadora tiene más puntos y es el ganador")
        return 1
    elif user_points > pc_points:
        print("El usuario tiene más puntos y es el ganador")
        return 2
    else:
        print("Tienen el mismo 21, es un empate")
        return 3