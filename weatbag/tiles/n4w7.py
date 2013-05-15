from weatbag import words
from weatbag.utils import transfer

class Tile:
    def __init__(self):
        self.challenge_completed = False
        
    def describe(self):
        print("The only thing around this place is sand, small rocks, the "
              "beach waters, about a dozen of kitties playing around and "
              "a lighthouse on the north.\n")
        if not self.challenge_completed:
            self.kitties()
            
                  
    def kitties(self):
         print("You aproach the kitties and to your surprise they all start "
               "rubbing at your legs and mewing! What is even more surprising "
               "is that your brain understands and translates meaws into "
               "words!\n"
               "You can clearly hear them say:\n"
               "'PLZ SIR, IT VRY HAWT HEER, CAN U TREAT US SUM  MICE CREAM?! "
               "ALL U NED IZ 2 USE SUM MICE AN SUM CREAM AN READY IT IZ! "
               "PLEEEEASE!' *mieaw* *rub* *rub*\n")

    def action(self, player, do):
            if do[0] in words.use and do[1] == "mice" and do[2]=="cream":
                if player.has("cream") and player.has("mice"):
                    player.take("cream")
                    player.take("mice")
                    print("Balls of tasty omnom mice cream fall from your "
                          "hands!\nThe kittens look very pleased!\n"
                          "Because they are happy they give you an advice:\n"
                          "'U SHUD AVOID BY ANY MEANZ TEH LIGHTHAUS! "
                          "BAD KAT LIVEZ THAR!'\n")
                    self.challenge_completed = True
            else:
                print("You'll need some mice and cream.")

    def leave(self, player, direction):
        if direction in ("s", "w"):
            print("It's the open sea. You can't go anywhere near by "
                  "swimming.\n")
            return False
        elif direction == "n":
            print("You are heading to the lighthouse.")
            return True
        else:
            return True

test_items = ['mice', 'cream']
