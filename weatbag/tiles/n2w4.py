from weatbag import words
from weatbag.utils import transfer

class Tile:
    def __init__(self):
        self.opendoor = False

    def describe(self):
        if self.opendoor:
            print("\nThe hut's door is open and the kitties are playing with " 
                  "their momcat!")
        else:
            print("\nYou are standing in front of the hut's door. The hut "
                  "looks very small and you wonder who could live there...\n"
                  "It has a door but you can't open it because the doorknob "
                  "is missing.") 
    
    def action(self, player, do):
        if (do[0] in words.use) and do[1]=='doorknob':           
            if player.has('doorknob'):
                player.take('doorknob') 
                print("\nDoorknob fits fine, clicks and voila... Door is open!\n"
                      "\nYou are in a cozy living room with a cat and 5 kittens"
                      " resting on a couch.\nThere is another room at west.")
                self.opendoor = True
            else:
                print("\nYou'll need a doorknob to open the door.")
                self.opendoor = False
        else:
            print("\nSorry, I don't understand.")    
            
    def leave(self, player, direction):
        if direction == 'w' and not self.opendoor:
            print("\nFirst you need to enter the hut.")
            return False
        elif direction == 's':
            print("Meeeeh, nothing of importance is going on there, try "
                  "another direction.")
            return False
        else:
            return True   
                                  
test_items = ['doorknob']
