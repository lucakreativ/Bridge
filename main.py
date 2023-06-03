import random as rd


class Color:
    def __init__(self, col):
        chars = ['c', 'd', 'h', 's']
        strs = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
        if type(col) == int:
            self.int_rep = col
            self.char_rep = chars[col]
            self.str_rep = strs[col]
        elif type(col) == str and len(col) == 1:
            self.int_rep = chars.index(col)
            self.char_rep = col
            self.str_rep = strs[self.int_rep]
        elif type(col) == str:
            self.int_rep = strs.index(col)
            self.char_rep = chars[self.int_rep]
            self.str_rep = col
        else:
            raise TypeError('Color() missing an argument')

    def __str__(self):
        return self.char_rep


class Value:
    def __init__(self, val):
        chars = ['2', '3', '4', '5', '6', '7', '8', '9', '0', 'J', 'Q', 'K', 'A']
        strs = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
        if type(val) == int:
            self.int_rep = val
            self.char_rep = chars[val]
            self.str_rep = strs[val]
        elif type(val) == str and len(val) == 1:
            self.int_rep = chars.index(val)
            self.char_rep = val
            self.str_rep = strs[self.int_rep]
        elif type(val) == str:
            self.int_rep = strs.index(val)
            self.char_rep = chars[self.int_rep]
            self.str_rep = val
        else:
            raise TypeError('Value missing an argument')

    def __str__(self):
        return self.char_rep


class Card:

    def __init__(self, color, value):
        self.col = Color(color)
        self.val = Value(value)

    def __str__(self):
        return self.col.__str__() + '' + self.val.__str__()


class Deck:
    def __init__(self, shuffled=True):
        self.cards = []
        for col in range(4):
            for val in range(12):
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

    def play(self):
        return self.cards.pop(rd.randint(0, len(self.cards)-1))


def game(player):
    deck = Deck()
    deck.deal(player)
    current_player = 0
    for i in range(13):
        for j in range(i, i + 4):
            print(player[i % 4].play())

