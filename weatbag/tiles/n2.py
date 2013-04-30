from weatbag import words
from weatbag.utils import transfer

class Tile:
    def __init__(self):
        self.contents = {'match': 42}
    
    def describe(self):
        print("You are standing in the mouth of a cave. The air "
            "feels cool and is filled with the stench of rotting flesh. "
            "A dark path leads to the north. An exit to the south.")
        if self.contents['match'] > 0:
            print("Someone has dropped a box of matches on the ground.")
    
    def leave(self, player, direction):
        if direction=='n' and not player.has('flaming torch'):
            print("You can't explore the cave without being able to see. "
                  "You'll need that stalwart friend of the adventurer, "
                  "the flaming torch.")
            return False
        else:
            return True
    
    def action(self, player, do):
        if (do[0] in words.take) and ('matches' in do):
            if transfer('match', self.contents, player.inventory, n=42):
                print("You pick up the matches.")
            else:
                print("You've already taken the matches.")
        
        elif (do[0] in words.use or do[0]=='light') and do[1]=='torch':
            if player.has('unlit torch') and player.has('match'):
                player.take('unlit torch')
                player.take('match')
                player.give('flaming torch')
                print("The torch catches, casting a flickering light on the "
                      "cave walls.")
            else:
                print("You'll need a torch and a match.")
        
        else:
            print("Sorry, I don't understand")

test_items = ['unlit torch']
