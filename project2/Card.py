import random
#global varible
# suits=("Hearts","Diamonds","Spades","Clubs")
# ranks=("Two","Three","Four","Five","Six","Seven")
values={"Two":2,"Three":3,"Four":4,"Five":5}

class Card:
    def __init__(self,suit,rank):
        self.suit=suit
        self.rank=rank
        self.value=values[rank]
        
    def __str__(self) -> str:
        return self.rank+" of "+ self.suit

# twoHeart=Card("Hearts","Two")
# print(twoHeart)