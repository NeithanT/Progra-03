import random
import functions 

user_cards=[]

def request_card():
    """
    Function to request a card from the deck.
    """
    global user_cards
    deck= functions.choose_deck()
    card = functions.choose_card(deck)
    
    list_cards = functions.save_user_cards(card,user_cards)
    print(list_cards)
    
    return list_cards
