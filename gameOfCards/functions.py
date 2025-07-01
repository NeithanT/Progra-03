import random    


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

    # Check if the ace can be turned into an 11
    if has_ace == True and total <= 11:
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

    if len(cards_list) > 0 and cards_list[0] == "5D":
        five_of_diamonds += 1

    if sum_cards(cards_list) <= 21:
        while i < len(cards_list):
            card = cards_list[i]
            if len(card) >= 2 and card.startswith("10"):
                num_small_cards += 1
            elif card[0] == "A":
                num_aces += 1
            elif card[0] == "7":
                num_sevens += 1
            elif card[0] in "JQK":
                num_figures += 1
            elif card[0] in "2345689":
                num_small_cards += 1
            i += 1
        
        total = sum_cards(cards_list)
        points = 0
        if total == 21 and num_sevens == 3:
            points += 5
        if num_aces == 2 and len(cards_list) == 2:
            points += 4
        if five_of_diamonds == 1:
            points += 3
        if len(cards_list) == 5 and num_figures == 0:
            points += 2
        if total == 21 and num_figures >= 1 and num_aces >= 1 and len(cards_list) == 2:
            points += 1
        if total == 21:
            points += 1
    else:
        points = 0
        
    print("Special points:", points)
    return points
