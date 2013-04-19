class Tile:
    
    def describe(self):
        print("The trees open out onto a beautiful beach. "
            "Small waves lap at the sand. Ahead of you, "
            "the ocean stretches as far as you can see.")
    
    def action(self, player, do):
        # Nothing to do here yet.
        print("Sorry, I don't understand")
    
    def leave(self, player, direction):
        if direction=='w':
            print("You've forgotten how to swim.")
            return False
        return True
            
