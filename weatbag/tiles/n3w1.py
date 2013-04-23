class Tile:
    def describe(self):
        print("\nThe beach is quiet. On the south are children playing.")
    
    def action(self, player, do):
        print("\nSorry, I don't understand")
        
    def leave(self, player, direction):
        if direction=='w':
            print("\nI'm afraid you can't go west.\nThe sea on that part is "
                  "fool of electric eels and you don't have a transport.")
            return False
        elif direction=='e':
            print("\nThere is the side of a cave in front of you.\nYou can't go "
                  "east.")
            return False
        return True
