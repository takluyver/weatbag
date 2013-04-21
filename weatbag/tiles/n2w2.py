from weatbag import words
from weatbag.utils import transfer

class Tile:
    def __init__(self):
        self.contents = {'doorknob': 1}
    
    def describe(self):
        print("You are now on the island.")
        if self.contents['doorknob']:
            print("As you walk around you find something shiny on the ground. "
            "It looks like a brass doorknob.")
        else:
            print("There is nothing interesting here")
    def action(self, player, do):
        if (do[0] in words.take) and ('doorknob' in do):
            self.take_doorknob(player)
            
        else:
            print("Sorry, I don't understand.")
    
    def take_doorknob(self, player):
        if transfer('doorknob', self.contents, player.inventory):
            print("You pick up the doorknob.")
        else:
            print("There is nothing here.")

    def leave(self, player, direction):
        if direction == "e":
            print ("You can't go back by swimming, that part is full of "
                 "electric eels.")
            return False
        else:
            return True
