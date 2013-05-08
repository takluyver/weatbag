class Tile:

    def describe(self):
        print("\n")

    def action(self, player, do):
        print("Sorry, I don't understand.\n")

    def leave(self, player, direction):
        if direction == "w":
            print("No-no! You'll break your head to the rocks down there!\n")
            return False
        elif direction == "s":
            print("You follow the path uphill. Just be careful of the slipery "
                  "rocks.")
            return True
        else:
            return True
