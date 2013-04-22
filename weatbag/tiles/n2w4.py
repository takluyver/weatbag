from weatbag import words
from weatbag.utils import transfer


class Tile:
    def describe(self):
        print("You are standing in front of the hut's door. The hut looks very "
              "small and you wonder who could live there... It has a door but "
              "you can't open it because the doorknob is missing.") 
    
    def action(self, player, do):
        if (do[0] in words.use) and do[1]=='doorknob':           
            if player.has('doorknob'):
                player.take('doorknob') 
                print("Doorknob fits fine, clicks and voila... Door is open!\n"
                      "You are in a cozy living room with a cat and 5 kittens "
                      "resting on a couch.\nThere is another room at west.")
               
            else:
                print("You'll need a doorknob to open the door.")
        else:
            print("Sorry, I don't understand.")    
            
    def leave(self, player, direction):
        if direction=='w' and player.has('doorknob'):
            print("First you need to enter the hut.")
            return False
        else:
            return True   
                      
test_items = ['doorknob']
