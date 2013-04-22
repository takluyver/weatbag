from weatbag import words
from weatbag.utils import transfer


class Tile:
    def describe(self):
        print("You are standing in front of the hut.\nIt has a door but you "
              "can't open it because the doorknob is missing.")
    
    def action(self, player, do):
        if (do[0] in words.use) and do[1]=='doorknob':            
            if player.has('doorknob'):
                player.give('doorknob')
                print("Doorknob fits fine, clicks and voila! Door is open!")
            else:
                print("You'll need a doorknob to open the door.")
        else:
            print("Sorry, I don't understand.")       
                      
test_items = ['doorknob']
