class Tile:

    def describe(self):
        print("The beach is really quiet and you can hear and see the seagulls "
              "on the sea.")

    def action(self, player, do):
        print("What is this giberish?")

    def leave(self, player, direction):
        if direction == "e":
            print("You can't go back by swimming, that part is full of "
                  "electric eels.\n")
            return False
        elif direction == "s":
            print("I'm afraid I can't let you go there Dave.\n")
            return False
        elif direction == "w":
            print("The sandy beach is transforming into big rocks but it looks "
                  "like you are able to climb them.\n"
                  "Just be careful because they are a bit slipery.")
            return True
        else:
            return True
