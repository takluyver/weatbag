from weatbag import words
from weatbag.utils import transfer

class Tile:
    def __init__(self):
        self.contents = {'mice': 2}
    
    def describe(self):
        if self.contents['mice']:
            print("As you walk the rocky path at the edge of the cliff you "
                  "hear a squeaking sound and you notice two mouse traps on the "
                  "ground. Each has one mouse trapped inside.\n"
                  "You could take the silly rodents but really... what the "
                  "hell are you gonna do with them?\n")
        else:
            print("You walk the path at the edge of the cliff. Nothing "
                  "to do here.\n")

    def action(self, player, do):
        if (do[0] in words.take) and ('mice' in do):
            self.take_mice(player)
        else:
            print("Sorry, I don't understand.\n")

    def take_mice(self, player):
        if transfer('mice', self.contents, player.inventory, n=2):
            print("Ok then. You took the mice.\n")
        else:
            print("No more mice for now. Got to leave the traps do their "
                  "job.\n")

    def leave(self, player, direction):
        if direction == "s":
            print("My dear traveler, you can't go south, you will fall off the "
                   "cliff!\n")
            return False
        elif direction == "n":
            print("It looks like the side of a wooden hut.\n"
                  "Since you don't walk though walls (yet) "
                  "you can't go there.\n")
            return False
        elif direction == "w":
            print("You follow the path uphill.")
            return True
        else:
            return True
