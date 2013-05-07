from weatbag import words
from weatbag.utils import transfer

class Tile:
    def __init__(self):
        self.contents = {'rats': 2}
    
    def describe(self):
        if self.contents['rats']:
            print("As you walk the path at the edge of the cliff you hear a "
                  "squeaking sound and you notice two rat traps on the ground. "
                  "Each are having one rat inside them trapped.\n"
                  "You could take the nasty rodents but really... what the "
                  "hell are you gonna do with them?\n")
        else:
            print("You walk the path at the edge of the cliff. Nothing "
                  "to do here.\n")

    def action(self, player, do):
        if (do[0] in words.take) and ('rats' in do):
            self.take_rats(player)
        else:
            print("Sorry, I don't understand.\n")

    def take_rats(self, player):
        if transfer('rats', self.contents, player.inventory, n=2):
            print("You take the rats.\n")
        else:
            print("No more rats for now. Got to leave the traps do their "
                  "job.\n")

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
