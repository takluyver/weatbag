from weatbag import words
from weatbag.utils import transfer

class Tile:
    map_word = "Box riddle"
    
    def __init__(self):
        self.contents = {'knife': 1}
        self.challenge_completed = False
        
    def describe(self):
        print("Your feet make a crackling sound as your feet snap some twigs "
              "on the ground.")
        if not self.challenge_completed:
            self.challenge()
        elif self.challenge_completed and self.contents["knife"]>0:
            print("You look around and you see an open box with a knife "
                 "inside. You should probably take it. A knife can be usefull.")
         
    def challenge(self):
        print("You just steped into something different. It is a metal box and "
              "it looks like something is written on it. You clear the dirt "
              "off it and what you see carved in the box lid is:\n\n"
              "stands\n"
              "-------\n"
              "0_2345\n\n"
              "You try to open the box but it won't open.\n"
              "Now... as you might have guessed already, it is a magic box!\n"
              "If you *understand* what these carvings represent the box will "
              "open!\n")
        # What the riddle says is "No one understands"

    def action(self, player, do):
        if do == ["no", "one", "understands"]:
            print("And that is absolutely right!\n"
                  "The lid opens and you see a brand new army knife!\n")
            self.challenge_completed = True
            
        elif (do[0] in words.take) and ('knife' in do) and self.challenge_completed:    
            self.take_knife(player, do)
        else:
            print("Sorry, I don't understand.")
            
    def take_knife(self, player, do):
        if transfer('knife', self.contents, player.inventory):
            print("You put the knife in your bag.\n")
        else:
            print("There is nothing here.\n")
            
    def leave(self, player, direction):
        if direction == "s":
            print("You can't go there, it's a wall. It looks like the side of "
                  "a wooden hut.")
            return False
        else:
            return True
