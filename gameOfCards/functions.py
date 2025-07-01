
   
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
