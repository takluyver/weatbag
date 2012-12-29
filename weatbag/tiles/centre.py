from weatbag import words

class Tile:
    def __init__(self):
        self.contents = {'rope': 1}
    
    def describe(self):
        print("You are in a sizeable clearing in the forest. At your feet, you see "
              "a mysterious trap door, with three golden keyholes. Paths lead off "
              "in four directions, which your unerring sense of direction tells you "
              "correspond to the four compass points.")
        if self.contents.get('rope'):
            print("A short length of rope is lying on the floor.")
   
    def action(self, player, do):
        if (do[0] in words.take) and ('rope' in do):
            if self.contents['rope'] > 0:
                self.contents['rope'] -= 1
                player.give('rope')
                print("You put the rope in your bag. That could come in handy.")
            else:
                print("You already collected the rope.")
        
        else:
            print("Sorry, I don't understand.")
