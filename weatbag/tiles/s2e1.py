# Second and final bug quest tile.
#
# To future hackers:
# This is part of a short quest which beggins by
# going South from e1. Plase consider this when coding neighbouring tiles.
# thnx :)
from weatbag import words

class Tile:
    def __init__(self):
        self.first_time = True

    def describe(self):
        print("You have reached upstream."
            "You see the bug.")

    def action(self, player, do):
        if ('bug' in do) and ( do[0] in words.attack or
                               do[0] in words.look or
                               do[0] == 'crush' or
                               do[0] == 'fix' ):
            print("Traceback (most recent call last):\n"
                " File \"computergame.py\", line 97397, in matrix.py\n"
                "IndexError: list index out of range")
            input()
            if self.first_time == True:
                print("Suddenly, you realize!")
                self.first_time = False
                input()
            print("It's not a bug, it's a feature!")

    def leave(self, player, direction):
        restricted_directions = { 'w', 'e', 's' }
        if direction in restricted_directions:
            print("The undergrowth in that direction "
                "is impassable. You turn back.")
            return False
        else:
            return True
