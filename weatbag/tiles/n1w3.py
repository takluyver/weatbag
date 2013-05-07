class Tile:

    def describe(self):
        print("The sandy beach is transforming into big rocks but it looks "
              "like you are able to climb them.\n"
              "Just be carefull because they are a bit slipery.")

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
        else:
            return True
