
def sum_cards(cards):
    """_summary_

    Args:
        cards (_type_): _description_

    Returns:
        _type_: _description_
    """
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
        else:
            total += int(card[0])
        i += 1


    if ace_count > 0 and total + 10 <= 21:
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
        
def total_winner(cards_user,cards_pc):
    """
    Funcion that shows the winner of the game 
    """  
    # 0 - both lost
    # 1 - pc wins
    # 2 - user wins
    # 3- tie
    user_sum=sum_cards(cards_user)
    pc_sum=sum_cards(cards_pc)
    # Ambos se pasan de 21
    if user_sum > 21 and pc_sum > 21:
        print("Ambos se pasaron")
        return 0

    # Solo el usuario se pasa
    elif user_sum > 21:
        print("Gana PC")
        return 1

    # Solo la PC se pasa
    elif pc_sum > 21:
        print("Gana Usuario")
        return 2
      
    
    if user_sum == 21 and pc_sum == 21:
        win = winner(cards_user, cards_pc)
        if win == 1:
            return 1
        elif win == 2:
            return 2
        else:
            return 3

    # Si alguno tiene 21 exacto
    elif user_sum == 21:
        return 2
    elif pc_sum == 21:
        return 1

    # Ninguno se pasa, gana el que más se acerque a 21
    elif user_sum > pc_sum:
        return 2
    elif pc_sum > user_sum:
        return 1

    #This doesnt make sense but ñe
    else:
        return 3
    
    
def winner(cards_user, cards_pc):
    """
    Function to decide the winner based on Blackjack rules.
    """
    user_points = check_points(cards_user)
    pc_points = check_points(cards_pc)

    if pc_points > user_points:
        print("La computadora tiene mas puntos y es el gandaor")
        return 1
    elif user_points > pc_points:
        print("El usuario tiene mas puntos y es el gandaor")
        return 2
    
    elif pc_points == user_points:
        print("Tienen el mismo 21 es un empate")
        return 3