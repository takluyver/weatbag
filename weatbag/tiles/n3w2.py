from weatbag import words
from weatbag.utils import transfer

class Tile:
    def __init__(self):
        self.give_catfood = False
           
    def describe(self):
        if not self.give_catfood:
            print("You are at the beach and there is an old man with an "
                  "enormous beard that is getting his little boat ready to go "
                  "across to the mainland.\nNaturally, you are asking him to "
                  "take you in his boat.\nThe old man replies:\nOf course I "
                  "can take you with me, my dear adventurer but first I need "
                  "some catfood so I can feed the kitties across in the "
                  "mainland!")
        else:
            print("There's the old fisherman with his boat, he can take you "
                  "across if you like!")
    
    def action(self, player, do):
        if (do[0] in words.use or do[0] in words.give) and do[1]=='catfood':           

#   I only added words.use because player might
#   use the word "use" insteed of "give".

            if player.has('catfood'):
                player.take('catfood') 
                print("Great! Now we can sail!")
                self.give_catfood = True
        else:
            print("Sorry, I don't understand.")
    
    def leave(self, player, direction):
        if direction=='e'and not self.give_catfood:
            print("You can't swim, remember the electric eels? You need a "
                  "transport to go across.")
            return False
        return True
            
test_items = ['catfood']
