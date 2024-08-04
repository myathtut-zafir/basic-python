from project2.Card import Card

import random
suits=("Hearts","Diamonds","Spades","Clubs")
ranks=("Two","Three","Four","Five")

class Deck:
    def __init__(self) -> None:
        self.all_cards=[]
        for suit in suits:
            # print (suit)
            for rank in ranks:
                create_card=Card(suit,rank)
                self.all_cards.append(create_card)
    def shuffle(self):
        random.shuffle(self.all_cards)
    def deal_one(self):
        return self.all_cards.pop()

new_deck=Deck()
new_deck.shuffle()
test=new_deck.deal_one()
print(test)
# for deck in new_deck.all_cards:
#     print(deck)
    
