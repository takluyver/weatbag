class Tile:
    def describe(self):
        print("You push through the undergrowth - "
            "the path is overgrown but continues on...")
    
    def action(self, player, do):
        # Nothing to do here yet.
        print("Sorry, I don't understand")

    def leave(self, player, direction):
        restricted_directions = { 'e' }

        # I placed this restriction here to prevent 
        # early entrance to the bug quest
        # which should be started by going South from e1
        if direction in restricted_directions:
            print("The undergrowth in that direction "
                "is impassable. You turn back.")
            return False
        else:
            return True

