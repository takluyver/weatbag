from weatbag import words
import weatbag

class Tile:
    def __init__(self):
        self.contents = {'bug': 1}
        pass

    def describe(self):
        print("There is a stream here.\n"
            "It runs from South to North.")

        if self.contents['bug'] > 0:
            print("You see a huge ugly bug rush past you, "
                "following the river south.")
            self.contents['bug'] -= 1
        else:
            print("You remember this is where you saw that bug going south")

    def action(self, player, do):
        pass
