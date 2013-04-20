from weatbag import words

class Tile:
    def __init__(self):
        self.contents = {'island ticket': 1}
        self.minutes = "40"

    def describe(self):
        if self.contents['island ticket']:
            self.challenge()
        else:
            print("The brother and sister have vanished. You see a line of "
                  "trees across the sand.")

    def challenge(self):
        print("You aproach the children who you see now are a boy and a girl.\n"
              "They are playing and running around a raft.\n"
              "You ask them to give it to you.")
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
        if ( self.contents["island ticket"] > 0 ):
            try:
                if do[1] == "minutes": 
                    if do[0] == self.minutes:
                        print("Your guess have pleased me and my sister! "
                        "Let's go!")
                        print("The brother and sister will take you to the "
                        "island.")
                        self.contents['island ticket'] -= 1
                        player.give('island ticket')
                    else:
                        print("We're afraid this is not the correct answer. "
                            "Try another one.")
                elif (do[0] in words.take) and (do[1] == "sister" or 
                                                do[1] == "girl"):
                    print("You little bastard, leave my sister down!\n"
                        "What kind of an asshole are you? Taking advantage of "
                        "little children?\nWe will transfer you for free.")
                    print("The brother and sister take you to the island!")
                    self.contents['island ticket'] -= 1
                    player.give('island ticket')

                elif (do[0] in words.take) and (do[1] == "brother" or
                                                do[1] == "boy"):
                    print("You bastard, take me down!\n"
                      "We will transfer you for free!")
                    print("The brother and sister take you to the island!")
                    self.contents['island ticket'] -= 1
                    player.give('island ticket')

                elif (do[0] in words.take) and (self.contents['island ticket'] == 1):
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



