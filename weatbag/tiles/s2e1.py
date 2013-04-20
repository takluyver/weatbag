from weatbag import words

class Tile:
    def __init__(self):
        self.first_time = True

    def describe(self):
        print("You have reached upstream."
            "You see the bug.")

    def action(self, player, do):
        if (do[0] in words.look) and ('bug' in do):
            print("Traceback (most recent call last):\n"
                " File \"computergame.py\", line 97397, in matrix.py\n"
                "IndexError: list index out of range")
            input()
            if self.first_time == True:
                print("Suddenly, you realize!")
                self.first_time = False
                input()
            print("It's not a bug, it's a feature!")

    def leave(self, player, direction):
        restricted_directions = { 'w', 'e' }
        if direction in restricted_directions:
            print("The undergrowth in that direction "
                "is impassable. You turn back.")
            return False
        else:
            return True
