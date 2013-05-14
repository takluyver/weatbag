from weatbag import words
from weatbag.utils import transfer

class Tile:
    def __init__(self):
        self.challenge_completed = False
        
    def describe(self):
        print("You are on the beach. You see a small kiosk selling "
              "ice creams!\n")
        if not self.challenge_completed:
            self.challenge()
            
    def challenge(self):
        print("You go there and see that there's an old lady inside who stir a "
              "pot. A fat ginger cat outside the kiosk is digging holes in the "
              "sand.\nYou say hi, and the old lady replies:\n"
              "Hello to you traveler, I'm Grace Hopper and this is my cat "
              "Sandy Claws. I could offer you a cream but first you must "
              "answer me this:\n"
              "Tom's mother has three children. One is named April, one is "
              "named May. What is the third one named?\n")

    def action(self, player, do):
        print("I don't understand.\n")
        
        
#sandy claws
