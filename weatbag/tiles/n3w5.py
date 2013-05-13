from weatbag import words
from weatbag.utils import transfer

class Tile:
    def __init__(self):
        self.contents = {'knife': 1}
        self.challenge_completed = False
        
    def describe(self):
        print("Your feet do a crackling sound as your feet snapp some twigs on "
              "the ground.\n")
        if not self.challenge_completed:
            self.challenge()
            self.challenge_completed = True
            
    def challenge(self):
        print("You just steped into something different. It is a metal box and "
              "it looks like something is written on it. You clear the dirt "
              "of it and what you see carved in the box lid is:\n\n"
              "stands\n"
              "-------\n"
              "0_2345\n\n"
              "You try to open the box but it won't open.\n"
              "Now obviously as you might have guessed already it is a magic "
              "box! If you *understand* what these carvings represend the box "
              "will open!")
        # What the riddle says is "No one understands"

    def action(self, player, do):
        if do[0] == "no" and do[1] == "one" and do[2] == "understands":
            print("And that is absolutely right!\n"
                  "The lid opens and you see a brand new army knife!")
        else:
            print("Sorry, I don't understand.\n")
            

