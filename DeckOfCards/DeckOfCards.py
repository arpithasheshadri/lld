import random

class Card:
  def __init__(self, suit, rank):
    self.suit = suit
    self.rank = rank

  def __str__(self):
    return f"{self.rank} of {self.suit}"
    
class Deck:
  def __init__(self):
    self.suits = ["Clubs", "Heart", "Spade", "Diamonds"]
    self.ranks = ["A","2","3","4","5","6","7","8","9","J","Q","K"]
    self.cards = self._generate_deck()
    self.dealt_cards = []
    
  def _generate_deck(self):
    return [Card(suit, rank) for suit in self.suits for rank in self.ranks]

  def shuffle(self):
    random.shuffle(self.cards)

  def deal(self):
    if not self.cards:
      print("no more cards to deal")
      return None
    card = self.cards.pop()
    self.dealt_cards.append(card)
    return card

  def reset(self):
    self.cards.extend(self.dealt_cards)
    self.dealt_cards = []
    self.cards = self._generate_deck()
    self.shuffle()

  def __str__(self):
    return f"Deck with {len(self.cards)} cards remaining."
    
def main():
  deck = Deck()
  
  deck.shuffle()
  
  for i in range(5):
    card = deck.deal()
    print(card)
    
  print(deck)
  deck.reset()
  print(deck)
    
if __name__ == "__main__":
  main()