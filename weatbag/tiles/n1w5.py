class Tile:

    def describe(self):
        print("blah blah describe\n")

    def action(self, player, do):
        print("Sorry, I don't understand.\n")

    def leave(self, player, direction):
        if direction == "s":
            print("My dear traveler, you can't go south, you will fall of the "
                   "cliff!\n")
            return False
        elif direction == "n":
            print("It looks like the side of a wooden hut.\n"
                  "Since you don't walk though walls (yet) "
                  "you can't go there.\n")
            return False
        else:
            return True
