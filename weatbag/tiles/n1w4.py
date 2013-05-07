class Tile:
    def __init__(self):
        self.challenge_completed = False

    def describe(self):
        print("\n")
        if not self.challenge_completed:
            self.challenge()
        else:
            print("")

    def challenge(self):
        print("\n")
            pass

    def action(self, player, do):
        if not self.challenge_completed:
            pass
        else:
            print("I don't understand...")
            
    def leave(self, player, direction):
        if direction == "s":
            print ("Oh dear Basdet! You can't go north, you will fall of the "
                   "cliff!\n")
            return False
        else:
            return True
