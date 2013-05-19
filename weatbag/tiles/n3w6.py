class Tile:

    def describe(self):
        print("Rocks. Big rocks. Slippery rocks all over!\n")

    def action(self, player, do):
        print("Sorry, I don't understand.\n")

    def leave(self, player, direction):
        if direction == "w":
            print("No-no! You'll break your head on the rocks down there!\n")
            return False
        elif direction == "s":
            print("You follow the path uphill. Just be careful of the slippery "
                  "rocks.")
            return True
        elif direction == "n":
            print("You are almost down at the beach.")
            return True
        else:
            return True
