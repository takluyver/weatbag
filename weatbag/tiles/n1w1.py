class Tile:
    def describe(self):
        print("\nThere is a small island northwest.\n"
            "Unfortunatelly, you can't swim because the sea is full of "
            "electric eels so you need a transport to go there.\n"
            "Luckilly to the north you see 2 children with a raft sitting "
            "under a tree." )
    
    def action(self, player, do):
        pass

    def leave(self, player, direction):
        if direction == "w":
            print ("\nYou can't go there by swimming, that part is full of "
                 "electric eels.")
            return False
        else:
            return True
