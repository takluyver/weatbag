from weatbag import words
from weatbag.utils import transfer

class Tile:
    def __init__(self):
        self.contents = {'catfood': 2}
    
    def describe(self):
        if self.contents['catfood']>0:
            print("You look around and you see a shelf with catfood cans.\n"
                  "I don't know about you, but a catfood can is always handy!\n"
                  "Never know when you'll need to feed a kitty!\n")
        else:
            print("You see an empty self.")

    def action(self, player, do):
        if (do[0] in words.take) and ('catfood' in do):
            self.take_catfood(player) 
        else:
            print("Sorry, I don't understand.\n")
           
    def take_catfood(self, player):
        if transfer('catfood', self.contents, player.inventory, n=2):
            print("You did wise. You took the catfood!\n")
        else:
            print("There is nothing here.\n")

    def leave(self, player, direction):
        if direction == 'w'or direction == 's' or direction == 'n':
            print("Area 51. No trespassing beyond this point.\n")
            return False
        else:
            return True
