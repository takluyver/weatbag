from weatbag import words

class Tile:
    def __init__(self):
        self.challenge_not_completed = True
        self.minutes = "40"

    def describe(self):
        print("You see two children who you notice now are a boy and a girl.\n"
              "They are playing and running around a raft.\n")
        if self.challenge_not_completed:
            self.challenge()
        else:
            print("\nThe children will take you to the western island!")

    def challenge(self):
        print("You ask them to give it to you."
              "The little boy laughs  and replies: \n"
              "So you think you are brave enough to go to that island? "
              "Very well, but we cannot give you our raft. "
              "What we can do is transport you there ourselves. But first you "
              "must answer this:\n\n"
              "Ignore weight and weather variables and listen carefully.\n"
              "It takes me exactly one hour to transport a person to "
              "the island.\n"
              "It takes my sister double that time.\n"
              "If we combine our power, "
              "how many minutes will it take to transport you to the island?\n"
              "To make a guess, type a number followed by 'minutes'.\n")

    def action(self, player, do):
        if self.challenge_not_completed:
            try:
                if do[1] == "minutes": 
                    if do[0] == self.minutes:
                        print("Your guess have pleased me and my sister! "
                              "\nLet's go!")
                        print("The brother and sister will take you to the "
                              "island.\n")
                        self.challenge_not_completed = False
                    else:
                        print("We're afraid this is not the correct answer. "
                              "Try another one.\n")
                elif (do[0] in words.take) and (do[1] == "sister" or 
                                                do[1] == "girl"):
                    print("You bastard! Let my sister down!\n"
                          "What kind of an asshole are you? "
                          "Taking advantage of little children?\n"
                          "We will transport you for free.\n")
                    print("The brother and sister will take you "
                          "to the island!\n")
                    self.challenge_not_completed = False
                elif (do[0] in words.take) and (do[1] == "brother" or
                                                do[1] == "boy"):
                    print("You bastard, put me down!\n"
                          "We will trasnport you for free!\n")
                    print("The brother and sister will take you "
                          "to the island!\n")
                    self.challenge_not_completed = False
                elif (do[0] in words.take) and self.challenge_not_completed:
                    print("I told you we won't give you our raft, "
                          "you have to guess the correct amount of time!\n")
            except:
                print("Please try guessing a number, like '42 minutes'\n.")
    def leave(self, player, direction):
        if direction == "w" and self.challenge_not_completed:
            print ("You can't go there by swimming, that part is full of "
                   "electric eels.\n")
            return False
        elif direction == 'e':
            print("The undregrowth in that direction is impassable. "
                  "You turn back.")
            return False
        else:
            return True
