from weatbag import words

class Tile:
    def describe(self):
        print("You are standing in the mouth of a cave. The air feels cool and "
            "is filled with the stench of rotting flesh. "
            "A dark path leads to the north. An exit to the south.")
    
    def leave(self, player, direction):
        if direction=='s':
            return True
        if player.has('flaming torch'):
            return True
        print("You can't explore the cave without being able to see. You'll need "
              "that stalwart friend of the adventurer, the flaming torch.")
    
    def action(self, player, do):
        if (do[0] in words.use or do[0]=='light') and do[1]=='torch':
            if player.has('unlit torch'):
                player.take('unlit torch')
                player.give('flaming torch')
                print("The torch catches, casting a flickering light on the "
                      "cave walls.")
            else:
                print("Good plan, but you don't have a torch.")
        
        else:
            print("Sorry, I don't understand")

test_items = ['unlit torch']
