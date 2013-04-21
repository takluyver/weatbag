from weatbag import words
import weatbag

class Tile:
    def __init__(self):
        self.contents = {'bug': 1}
        self.first_visit = True
        pass

    def describe(self):
        print("There is a stream here. "
            "It runs from South to North.")

        if self.contents['bug'] > 0:
            print("You see a huge, ugly bug rush past you, "
                "following the river South.")
            self.contents['bug'] -= 1
        else:
            print("You remember this is where you saw that bug going South.")

    def action(self, player, do):
        pass

    def leave(self, player, direction):
        restricted_directions = { 'w', 'e' }
        if direction in restricted_directions:
            print("The undergrowth in that direction "
                "is impassable. You turn back.")
            return False
        elif direction ==  's':
            print("Bugs are the enemy and must be crushed!\n"
                "So you decide to follow the bug upstream.")
            input()
            self.first_visit = False
            return True
        else:
            if self.first_visit:
                print("Bugs do not interest you very much.\n"
                    "Lets get out of here.")
                self.first_visit = False
                input()
            return True
