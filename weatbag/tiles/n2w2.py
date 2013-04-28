class Tile:
    def describe(self):
        print("You are now on the island. In front of you there are some trees "
              "and a small path.\nFeeling adventurous?\n")

    def action(self, player, do):
        print("Sorry, wat?!")

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
