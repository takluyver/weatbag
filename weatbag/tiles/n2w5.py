from weatbag import words
from weatbag.utils import transfer

class Tile:
    def __init__(self):
        self.contents = {'catfood': 2}
    
    def describe(self):
        if self.contents['catfood']:
            print("You look around and you see a shelf with catfood cans.\n"
                  "I don't know about you, but a catfood can is always handy!\n"
                  "Never know when you'll need to feed a kitty!\n")

    def action(self, player, do):
        if (do[0] in words.take) and ('catfood' in do):
            self.take_catfood(player) 
            self.contents['catfood'] -= 1
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
