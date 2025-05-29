import random

class Deck:
    
    suits = ['hearts', 'diamonds', 'clubs', 'spades']
    values = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
    
    def __init__(self):
       self.__create_cards()
    
    def __str__(self):
        return " | ".join([str(card) for card in self.cards])
    
    def __create_cards(self):
        self.cards = []
        for suit in Deck.suits:
            for value in Deck.values:
                self.cards.append(Card(suit, value))
    
    def shuffle(self):
       random.shuffle(self.cards)
    
    def deal(self):
        if len(self.cards) == 0:
            return None
        # last_card = self.cards[len(self.cards) - 1]
        # del self.cards[len(self.cards) - 1]
        # return last_card
        return self.cards.pop()
        

    def count_remaining(self):
        return len(self.cards)

    def get_remaining(self):
        return [card.present() for card in self.cards]

            
class Card:
    
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
    
    def __str__(self):
        return f'{self.suit} / {self.value}'
    
    def present(self):
        return f'{self.value} of {self.suit}'


x  = Deck()

print(x.get_remaining())