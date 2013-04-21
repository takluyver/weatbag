from weatbag import words
from weatbag.utils import transfer

class Tile:
    def __init__(self):
        self.contents = {'key': 1}
    
    def describe(self):
        print("You are now on the island.")
        if self.contents['key']:
            print("As you walk around you find something shiny on the ground. Looks like a key.")
    
    def action(self, player, do):
        if (do[0] in words.take) and ('key' in do):
            self.take_key(player)
        else:
            print("Sorry, I don't understand.")
    
    def take_key(self, player):
        if transfer('key', self.contents, player.inventory):
            print("You pick up the key.")
        else:
            print("There is nothing here.")

    def leave(self, player, direction):
        if direction == "e":
            print ("You can't go back by swimming, that part is full of "
                 "electric eels.")
            return False
        else:
            return True
