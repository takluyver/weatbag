from weatbag import words
from weatbag.utils import transfer

class Tile:
    def __init__(self):
        self.opendoor = False

    def describe(self):
        if self.opendoor:
            print("The hut's door is open and the kitties are playing with " 
                  "their momcat!\n")
        else:
            print("You are standing in front of the hut's door. The hut "
                  "looks very small and you wonder who could live there...\n"
                  "It has a door but you can't open it because the doorknob "
                  "is missing.\n") 
    
    def action(self, player, do):
        if (do[0] in words.use) and do[1]=='doorknob':           
            if player.has('doorknob'):
                player.take('doorknob') 
                print("Doorknob fits fine, clicks and voila... Door is open!\n"
                      "\nYou are in a cozy living room with a cat and 5 kittens"
                      " resting on a couch.\nThere is another room at west.\n")
                self.opendoor = True
            else:
                print("You'll need a doorknob to open the door.\n")
                self.opendoor = False
        else:
            print("Sorry, I don't understand.\n")    
            
    def leave(self, player, direction):
        if direction == 'w' and not self.opendoor:
            print("First you need to enter the hut.\n")
            return False
        elif direction == 's':
            print("Meeeeh, nothing of importance is going on there, try "
                  "another direction.\n")
            return False
        else:
            return True   
                                  
test_items = ['doorknob']
