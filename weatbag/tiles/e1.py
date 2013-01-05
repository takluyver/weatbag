from weatbag import words

class Tile:
    def __init__(self):
        self.contents = {'berries': 1}
    
    def describe(self):
        print("The path crosses a small stream.")
        if self.contents['berries']:
            print("There are some berries hanging from a tree. They look edible. "
                  "If you're hungry enough, anyway.")
    
    def action(self, player, do):
        if (do[0] in words.take) and ('berries' in do):
            self.take_berries(player)
        else:
            print("Sorry, I don't understand.")
    
    def take_berries(self, player):
        if self.contents['berries'] > 0:
            self.contents['berries'] -= 1
            player.give('berries')
            print("Reaching up, you pick the berries.")
        else:
            print("There are no berries here.")
