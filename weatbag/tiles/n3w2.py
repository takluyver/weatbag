from weatbag import words
from weatbag.utils import transfer

class Tile:
    def __init__(self):
        self.give_catfood = False
           
    def describe(self):
        if not self.give_catfood:
            print("\nYou are at the beach and there is an old man with an "
                  "enormous beard that is getting his little boat ready to go "
                  "across to the mainland.\nNaturally, you are asking him to "
                  "take you in his boat.\nThe old man replies:\nOf course I "
                  "can take you with me, my dear adventurer but first I need "
                  "some catfood so I can feed the kitties across in the "
                  "mainland!")
        else:
            print("\nThere's the old fisherman with his boat, he can take you "
                  "across if you like!")
    
#   I only added words.use because player might
#   use the word "use" insteed of "give".
    def action(self, player, do):

        if do[0] in words.use or do[0] in words.give:
            if 'catfood' in do:
                if player.has('catfood'):
                    if self.give_catfood ==  False:
                        player.take('catfood')
                        self.give_catfood =  True
                        print("\nGreat! Now we can sail!")
                    else:
                        player.take('catfood')
                        print("\nOh how nice of you. You are the best!")
            elif len(do) > 1:
                print("\nI have no use for that.")
        else:
            print("\nSorry, I don't understand.")
    

    def leave(self, player, direction):
        if direction=='e'and not self.give_catfood:
            print("\nYou can't swim, remember the electric eels? You need a "
                  "transport to go across.")
            return False
        return True
            
#two catfoods!
test_items = ['catfood','catfood']
