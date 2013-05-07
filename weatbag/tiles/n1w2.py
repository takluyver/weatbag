class Tile:

    def describe(self):
        print("The beach is really quiet and you can hear and see the "
                  "seagulls on the sea.")

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
        else:
            return True
