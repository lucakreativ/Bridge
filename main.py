class Color():
    def __init__(self, int_rep=None, char_rep=None, str_rep=None):
        chars = ['c', 'd', 'h', 's']
        strs = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
        if int_rep!=None:
            self.int_rep = int_rep
            self.char_rep = chars[int_rep]
            self.str_rep = strs[int_rep]
        elif char_rep!=None:
            self.int_rep = chars.index(char_rep)
            self.char_rep = char_rep
            self.str_rep = strs[self.int_rep]
        elif str_rep!=None:
            self.int_rep = strs.index(str_rep)
            self.char_rep = chars[self.int_rep]
            self.str_rep = str_rep
        else:
            raise TypeError('Color() missing an argument')
    def __str__(self):
        return(self.str_rep)


class Card():
    def __init__(self, color, value):
        """

        :param color: str, int or char
        :param value: int
            values from 2 to 14, 2-10 = 2-10, 11 = Jack, 12 = Queen, 13 = King, 14 = Ace
        """
        self.color = Color(char_rep=color)
        self.value = value
