from weatbag import words
import random

class Tile:
    map_word = "Dwarf"
    
    def __init__(self):
        self.contents = {'unlit torch': 1}
        self.lucky_number = random.randrange(1,100)
        self.guess_count = 0
    
    def describe(self):
        if self.contents['unlit torch']:
            self.challenge()
        else: 
            print("You see a pile of dust on the ground.")

    def challenge(self): 
        print("A dwarf suddenly appears and says 'If you guess my "
            "lucky number, I might give you a reward!'")
        print("To make a guess, type 'guess' followed by a number "
            "between 1-100.")
    
    def action(self, player, do):
        if do[0] == "guess" and self.contents['unlit torch']: 
            try: 
                if do[1] == "correctly": 
                    print("You sly dog, you!")
                    print("The dwarf hands you a torch! "
                        "He then suddenly vanishes, "
                        "leaving behind a pile of dust.")
                    self.contents['unlit torch'] -= 1
                    player.give('unlit torch')
                    return

                guess = int(do[1])
                self.guess_count += 1
                if guess > self.lucky_number: 
                    print("Too high! Guess again!")
                elif guess < self.lucky_number: 
                    print("Too low! Guess again!")
                else: 
                    print("You guessed my lucky number in %d guesses!" % 
                        (self.guess_count))
                    print("The dwarf hands you a torch! "
                        "He then suddenly vanishes, "
                        "leaving behind a pile of dust.")
                    self.contents['unlit torch'] -= 1
                    player.give('unlit torch')
            except: 
                print("Please try guessing a number, like 'guess 7'.")

        #if action is "take" AND there is still a dwarf around to complain,
        #then complain.
        elif (do[0] in words.take) and (self.contents['unlit torch'] == 1):
            print("You can't have my prize, "
                "you have to guess the lucky number!")
        else:
            print("Sorry, I don't understand.")
