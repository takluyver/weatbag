class Tile:

    def describe(self):
        print("blah blah describe\n")

    def action(self, player, do):
        print("Sorry, I don't understand.\n")

    def leave(self, player, direction):
        if direction in ('s', 'w'):
            print("My dear traveler, you can't go there, you will fall of the "
                   "cliff!\n")
            return False
        else:
            return True
