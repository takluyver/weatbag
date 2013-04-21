class Tile:
    
    def describe(self):
        print("s3e1")

    def action(self, player, do):
        pass

    # For future hackers:
    # I have placed this restriction here so that
    # the player cannot accidentaly enter 
    # the bug quest early. (which should start by going south from e1)
    # Unless the bug quest is appropriately modified,
    # please do not remove this restriction from this tile.
    def leave(self, player, direction):
        restricted_directions = { 'n' }
        if direction in restricted_directions:
            print("The undergrowth in that direction "
                "is impassable. You turn back.")
            return False
        else:
            return True
