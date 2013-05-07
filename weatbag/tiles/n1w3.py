class Tile:

    def describe(self):
        print("Woooah! Those rocks are full of lichens!\n")

    def action(self, player, do):
        print("Sorry, I don't speak giberish.\n")

    def leave(self, player, direction):
        if direction == "s":
            print("Are you planing to throw your self to the rocks? You can't "
                  "go there!\n")
            return False
        elif direction == "n":
            print("The rocks are way to high for you. "
                  "Unfortunatelly you cannot climb them.")
            return False
        else:
            return True
