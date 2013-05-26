class Tile:
    map_word = "Pine forest"
    
    def describe(self):
        print("There are not so many trees around but the ground is full of "
              "pine needles and pine cones.\n")

    def action(self, player, do):
        print("I don't understand.")
        
    def leave(self, player, direction):
        if direction == "e":
            print("Area 51. No trespassing beyond this point.")
            return False
        elif direction == "n":
            print("There is an opening that leads you to the beach on the "
                  "northen side of the island.")
            return True
        else:
            return True
