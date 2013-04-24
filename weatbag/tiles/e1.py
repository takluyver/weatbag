from weatbag import words
from weatbag.utils import transfer

class Tile:
    def __init__(self):
        self.contents = {'berries': 1}
    
    def describe(self):
        print("The path crosses a small stream.")
        if self.contents['berries']:
            print("There are some berries hanging from a tree. "
                "They look edible. "
                "If you're hungry enough, anyway.")
    
    def action(self, player, do):
        if (do[0] in words.take) and ('berries' in do):
            self.take_berries(player)
        else:
            print("Sorry, I don't understand.")
    
    def take_berries(self, player):
        if transfer('berries', self.contents, player.inventory):
            print("Reaching up, you pick the berries.")
        else:
            print("There are no berries here.")

    def leave(self,player,direction):
        if direction ==  's':
            print("You decide the path is too boring for you,\n"
                "so you follow the stream south, looking for adventure...")
            input()
            return True
        else:
            return True
