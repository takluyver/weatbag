class Tile:
    map_word = "Beach curve"
    
    def describe(self):
        print("The beach makes a nice little curve on that spot. There are "
              "some pine trees around too. A really quiet sceenery!\n")

    def action(self, player, do):
        print("Sorry, I don't understand.\n")

    def leave(self, player, direction):
        if direction == "s":
            print("You follow the path uphill. There are some rocks. Just be "
                  "careful, they all have this gooey green stuff on them!\n")
            return True
        elif direction == "e":
            print("You are going through the pine trees.\n")
            return True
        else:
            return True
