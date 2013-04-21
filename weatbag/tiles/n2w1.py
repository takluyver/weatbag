from weatbag import words

class Tile:
    def __init__(self):
        self.challenge_not_completed = True
        self.minutes = "40"

    def describe(self):
        print("You see two children who you notice now are a boy and a girl.\n"
              "They are playing and running around a raft.")
        if self.challenge_not_completed:
            self.challenge()
        else:
            print("They take you to the western island!")

    def challenge(self):
        print("You ask them to give it to you.")
        print("The little boy laughs  and replies: \nSo you think you "
              "are brave enough to go to that island? Very well, but we cannot"
              " give you our raft. "
              "What we can do is transfer you there ourselves. But first you "
              "must answer this:\n\n")
        print("Ignore weight and weather variables and listen carefully.\nIt "
              "takes for me to transfer a person on the island exactly one hour.\n"
              "It takes double the time for my sister.\nIf we combine our powers "
              "in how many minutes will we transfer you on the island?\n")
        print("To make a guess, type a number followed by 'minutes'")

    def action(self, player, do):
        if self.challenge_not_completed:
            try:
                if do[1] == "minutes": 
                    if do[0] == self.minutes:
                        print("Your guess have pleased me and my sister! "
                        "Let's go!")
                        print("The brother and sister will take you to the "
                        "island.")
                    else:
                        print("We're afraid this is not the correct answer. "
                            "Try another one.")
                elif (do[0] in words.take) and (do[1] == "sister" or 
                                                do[1] == "girl"):
                    print("You little bastard, leave my sister down!\n"
                        "What kind of an asshole are you? Taking advantage of "
                        "little children?\nWe will transfer you for free.")
                    print("The brother and sister take you to the island!")
                elif (do[0] in words.take) and (do[1] == "brother" or
                                                do[1] == "boy"):
                    print("You bastard, take me down!\n"
                      "We will transfer you for free!")
                    print("The brother and sister take you to the island!")
                elif (do[0] in words.take) and self.challenge_not_completed:
                    print("I told you we won't give you our raft, "
                        "you have to guess the correct amount of time!")
            except:
                print("Please try guessing a number, like '42 minutes'.")
    def leave(self, player, direction):
        if direction == "w":
            print ("You can't go there by swimming, that part is full of "
                 "electric eels.")
            return False
        else:
            return True


