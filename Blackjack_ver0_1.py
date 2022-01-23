from itertools import repeat
from random import choice

No_cards = ["Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten",
            "Jack", "Queen", "King", "Ace",
           ]
cards_value = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 11, 11, 11,]
cards_col = ["Clubs", "Spades", "Diamond", "Hearts",]
burned_cards = []
crupiers_cards = []
ccard_value = []
your_cards = []
ycard_value = []
win = 0
while win == 0:
    current_card = choice(No_cards) + " of " + choice(cards_col)
    curr_value = 0
    if "Two" in current_card:
            curr_value = 2
    elif "Three" in current_card:
            curr_value = 3
    elif "Four" in current_card:
            curr_value = 4
    elif "Five" in current_card:
            curr_value = 5
    elif "Six" in current_card:
            curr_value = 6
    elif "Seven" in current_card:
            curr_value = 7
    elif "Eight" in current_card:
            curr_value = 8
    elif "Nine" in current_card:
            curr_value = 9
    elif "Ten" in current_card:
            curr_value = 10
    elif "Jack" or "Queen" or "King" or "Ace" in current_card:
            curr_value = 11
    else:


#  Crupiers turn
        if current_card not in burned_cards:
            crupiers_cards += [current_card]
            ccard_value = curr_value
            print("Now crupier have these cards on hand:\n {} \nAnd their value is equal to:\n{}.".format(crupiers_cards,
                                                                                                ccard_value))
            burned_cards.append(current_card)
        else:
            repeat()
print(curr_value)
print(burned_cards)
print(current_card)