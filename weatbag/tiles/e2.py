from weatbag import words
import random

class Tile:
    def __init__(self):
        self.contents = {'flaming torch': 1}
        self.lucky_number = random.randrange(1,100)
    
    def describe(self):
        if self.contents['flaming torch']:
            self.challenge()
        else: 
            print("You see a pile of dust on the ground.")

    def challenge(self): 
        print("A wizard suddenly appears and says 'If you guess my "
            "lucky number, I might give you a reward!'")
        print("Say 'guess' followed by a number between 1-100 to guess.")
    
    def action(self, player, do):
        if do[0] == "guess" and self.contents['flaming torch']: 
            try: 
                guess = int(do[1])
                if guess > self.lucky_number: 
                    print("Too high! Guess again!")
                elif guess < self.lucky_number: 
                    print("Too low! Guess again!")
                else: 
                    print("You guessed my lucky number!")
                    print("The wizard hands you a flaming torch! "
                        "He then suddenly vanishes, leaving behind a pile of dust.")
                    self.contents['flaming torch'] -= 1
                    player.give('flaming torch')
            except: 
                print("Please try guessing a number, like 'guess 7'.")
        elif (do[0] in words.take):
            print("You can't have my prize, you have to guess the lucky number!")
        else:
            print("Sorry, I don't understand.")
