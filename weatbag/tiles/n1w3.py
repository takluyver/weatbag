class Tile:
    map_word = "Beach rocks"
    
    def describe(self):
        print("Woooah! Those rocks are full of lichens!\n")

    def action(self, player, do):
        print("Sorry, I don't speak gibberish.")

    def leave(self, player, direction):
        if direction == "s":
            print("Are you planing to throw your self to the rocks? You can't "
                  "go there!")
            return False
        elif direction == "n":
            print("The rocks are way to high for you. "
                  "Unfortunately you cannot climb them.")
            return False
        elif direction == "w":
            print("The rocks led you to a path uphill.")
            return True
        else:
            return True
