# Hand.py a hand class

# The methods for this class:
class Hand:
    def __init__ (self):
        #start the list to empty self.hand
        self.hand = []



    def reset():
        #resets the hand to empty hand
        self.hand = []

    def add (card):
        #appends card to hand
        self.hand.append(card)

    def size():
        #returns length of the list
        return self.hand.len()
        #returns integer

    def get_card (i):
        if i >= self.size():
            print "ERROR Index Out Of Range"
            return
        return self.hand[i]
        #returns card at index i
    def get_card_value():
        #gives you the sum of the value of the cards 
        sum = 0
        for i in hand:
            sum = sum+1

        #returns init




# Author Lorenzo Hernandez     3/11/2016
