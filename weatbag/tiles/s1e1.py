# First bug quest tile.
#
# To future hackers:
# This is part of a short quest which begins by
# going South from e1. Plase consider this when coding neighbouring tiles.
# thnx :)
from weatbag import words
import weatbag

class Tile:
    map_word = "Bug quest"
    
    def __init__(self):
        self.bug_is_here = True
        self.first_visit = True
        self.hasnt_gone_south = True
        pass

    def describe(self):
        print("There is a stream here. "
            "It runs from South to North.")

        if self.bug_is_here:
            print("You see a huge, ugly bug rush past you, "
                "following the river South.")
            self.bug_is_here = False
        else:
            print("You remember this is where you saw that bug going South.")

    # Nothing to do here.
    def action(self, player, do):
        pass

    # Player can only exit the bug quest going back North.
    # Player gets different messages the first time they
    # exit this tile, depending on their direction.
    def leave(self, player, direction):
        restricted_directions = { 'w', 'e' }
        if direction in restricted_directions:
            print("The undergrowth in that direction "
                "is impassable. You turn back.")
            return False
        elif direction ==  's' and self.hasnt_gone_south:
            print("Bugs are the enemy and must be crushed!\n"
                "So you decide to follow the bug upstream.")
            input()
            self.first_visit = False
            self.hasnt_gone_south = False
            return True
        else:
            if self.first_visit:
                print("Bugs do not interest you very much.\n"
                    "Lets get out of here.")
                self.first_visit = False
                input()
            return True
