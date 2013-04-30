from weatbag import words

class Tile:
    def __init__(self):
        self.first_visit = True

    def describe(self):
        if self.first_visit:
            print("You are now on the island. The children are returning back "
                  "to the mainland with their raft.\n"
                  "In front of you there are some trees and a small path.\n"
                  "Feeling adventurous?\n")
            self.first_visit = False
        else:
            print("The beach is quiet. Nothing seems to be going on.")

    def action(self, player, do):
        if do[0] in words.yes:
            print("Awesome! Follow the path!")
        elif do[0] in words.no:
            print("You might be in the wrong place then. Pack your stuff and "
                  "quit the game.")
        else:
            print("Sorry, wat?!")

    def leave(self, player, direction):
        if direction == "e":
            print("You can't go back by swimming, that part is full of "
                  "electric eels.\n")
            return False
        elif direction == "s":
            print("I'm afraid I can't let you go there Dave.\n")
            return False
        else:
            return True
