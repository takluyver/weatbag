from weatbag import words
from weatbag.utils import transfer

class Tile:
    def __init__(self):
        self.contents = {"cream": 1}
        self.challenge_completed = False
        
    def describe(self):
        print("You are on the beach. You see a small kiosk selling "
              "ice creams!\n")
        if not self.challenge_completed:
            self.challenge()
            
    def challenge(self):
        print("You go and see an old lady inside stir a pot. A fat ginger cat "
              "outside the kiosk is digging holes in the sand.\n"
              "You say hi, and the old lady replies:\n"
              "Hello to you traveler, I'm Grace Hopper and this is my cat "
              "Sandy Claws. I could offer you some cream but first you must "
              "answer me this:\n"
              "Tom's mother has three children. One is named April, one is "
              "named May. What is the third one named?\n")

    def action(self, player, do):
        if do[0]=="tom" and self.contents["cream"]:
            print("That's correct. Now you can have some cream! "
                  "There... already in your bag!\nHave a mice day!\n")
            self.contents["cream"] -= 1
            player.give("cream")
            self.challenge = True
        elif do[0] in words.take and "cream" in do and self.contents["cream"]:
            print("No, it doesn't work this way. First you gotta answer my "
                  "question!")
        elif do[0] in words.take and "cream" in do:
            print("Don't be greedy, you have all the cream you're gonna "
                  "need.\n")
        else:    
            print("I don't understand.\n")
        
    def leave(self, player, direction):
        if direction in ("n", "e"):
            print("It's the open sea. You can't go anywhere near by "
                  "swimming.\n")
            return False
        elif direction == "s":
            print("A bunch of pine trees...")
            return True
        else:
            return True
