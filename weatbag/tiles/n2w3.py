class Tile:
    def __init__(self):
        self.first_visit = True
        self.tree_fallen = False

    def describe(self):
        print("You are walking through the trees. It looks like the path you "
              "took leads to a small wooden hut.\n")
        if not self.first_visit and not self.tree_fallen:
            print("You saw a tree fall and it didn't make any sound and "
                  "WOW... that was weired because you were there and "
                  "observed it!\n")
            self.tree_fallen = True
        self.first_visit = False    
        # "If a tree falls in a forest and no one is around to hear it,
        # does it make a sound?" is a philosophical thought experiment that
        # raises questions regarding observation and knowledge of reality.
    def action(self, player, do):
        print("Wat?!")

    def leave(self, player, direction):
        if direction == "s":
            print("STAHP! Hammer Time!\n(Meaning you just can't go to that "
                  "direction yet. Sorry! :))\n")
            return False
        else:
            return True
