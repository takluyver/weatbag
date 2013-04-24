from weatbag import words
from weatbag.utils import transfer

class Tile:
    def __init__(self):
        self.contents = {'doorknob': 1}
    
    def describe(self):
        if self.contents['doorknob']:
            print("\nAs you walk through the path you find something shiny on "
            "the ground beside some rocks.\nIt looks like a brass doorknob.")
        else:
            print("\nThere is nothing to do here, all you see is your path and "
            "the trees around!")
    def action(self, player, do):
        if (do[0] in words.take) and ('doorknob' in do):
            self.take_doorknob(player)
            
        else:
            print("\nSorry, I don't understand.")
    
    def take_doorknob(self, player):
        if transfer('doorknob', self.contents, player.inventory):
            print("\nYou pick up the doorknob.")
        else:
            print("\nThere is nothing here.")
            
    def leave(self, player, direction):
        if direction == "n":
            print("Oops. You can't go there. There is a rocky wall.\n")
            return False
        else:
            return True
