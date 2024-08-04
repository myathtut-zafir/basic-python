

import random

from project2.Card import Card
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
# print(test)
# for deck in new_deck.all_cards:
#     print(deck)
    

class Player:
    def __init__(self,name) -> None:
        self.name=name
        self.all_cards=[]

    def remove(self):
        return self.all_cards.pop(0)
    
    def add_cards(self,new_cards):
        if type(new_cards)==type([]):
            self.all_cards.extend(new_cards)
        else:
            self.all_cards.append(new_cards)
            
    def __str__(self) -> str:
        return f'player {self.name} has {len(self.all_cards)} cards.'

new_player=Player("mgmg")
new_player.add_cards(test)
new_player.add_cards([test,test,test,test])
new_player.remove()
print(new_player)
