import random as rd

class Card:

    def __init__(self, col, val):
        col_chars = ['c', 'd', 'h', 's']
        col_strs = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
        val_chars = ['2', '3', '4', '5', '6', '7', '8', '9', '0', 'J', 'Q', 'K', 'A']
        val_strs = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
        if type(col) == int:
            self.col = col
            self.col_char = col_chars[col]
            self.col_str = col_strs[col]
        elif type(col) == str and len(col) == 1:
            self.col_char = col_chars.index(col)
            self.col = col
            self.col_str = col_strs[self.col]
        elif type(col) == str:
            self.col = col_strs.index(col)
            self.char_rep = col_chars[self.col]
            self.str_rep = col
        if type(val) == int:
            self.val = val
            self.val_char = val_chars[val]
            self.val_str = val_strs[val]
        elif type(val) == str and len(val) == 1:
            self.val = val_chars.index(val)
            self.val_char = val
            self.val_str = val_strs[self.val]
        elif type(val) == str:
            self.val = val_strs.index(val)
            self.val_char = val_chars[self.val]
            self.val_str = val

    def __repr__(self):
        return self.col_char + '' + self.val_char

class Deck:
    def __init__(self, shuffled=True):
        self.cards = []
        for col in range(4):
            for val in range(13):
                self.cards.append(Card(col, val))
        if shuffled:
            self.shuffle()

    def shuffle(self):
        rd.shuffle(self.cards)

    def deal(self, player, shuffle=True):
        if shuffle: self.shuffle()
        player[0].cards = self.cards[0:13]
        player[1].cards = self.cards[13:26]
        player[2].cards = self.cards[26:39]
        player[3].cards = self.cards[39:52]

class Player:
    def __init__(self, name=None, pos='n'):
        self.name = name
        self.pos = pos
        self.bids = []
        self.cards = []

    def play(self):
        return self.cards.pop(rd.randint(0, len(self.cards) - 1))

    def bid(self, bids):
        forum_d(self.cards, bids)

class Bids:
    def __init__(self):
        cols = ['c', 'd', 'h', 's', 'n']
        self.bids = ["p"]
        for val in range(7):
            for col in range(5):
                self.bids.append({
                    "name": f"{val} {cols[col]}",
                    "bidder": None,
                    "val": val,
                    "col": col
                })
        highest_bid = "p"

def game(player=None):
    if player == None: player = [Player(pos=i) for i in range(4)]
    deck = Deck()
    deck.deal(player)
    bidding(player)
    playing(player)

def playing(player):
    for i in range(13):
        for j in range(i, i + 4):
            print(player[j % 4].play(), end=' - ')
        print('')

def bidding(player):
    bids = Bids
    i = 0
    while True:
        player[i].bid()
        i+=1
        i=i%4

game()
