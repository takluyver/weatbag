class Tile:
    def describe(self):
        print("The beach is quiet. To the south children are playing.\n")
    
    def action(self, player, do):
        print("wo0t w0ot?! o_O")
        
    def leave(self, player, direction):
        if direction == 'w':
            print("I'm afraid you can't go west.\nThe sea on that part is "
                  "full of electric eels and you don't have a transport.\n")
            return False
        elif direction == 'e':
            print("There's a steep mountainside here which you can't climb.")
            return False
        elif direction == 'n':
            print("               ,               , \n"
                  "             _/((             \)\ \n"
                  "    _.---. .'   `\           /    '. .---._ \n"
                  "  .'      `     ^ T=       =P ^     `      '. \n"
                  " /     \       .--'         `--.       /     \ \n"
                  "|      /       )'-.         .-'(       \      | \n"
                  "; ,   <__..-(   '-.)       (.-'   )-..__>   , ; \n"
                  " \ \-.__)    ``--._)       (_.--``    (__.-/ / \n"
                  "  '.'-.__.-.                       .-.__.-'.' \n"
                  "    '-...-'                        '-...-' \n"
                  "               ,               , \n"
                  "             _/((             \)\ \n"
                  "    _.---. .'   `\           /    '. .---._ \n"
                  "  .'      `     ^ T=       =P ^     `      '. \n"
                  " /     \       .--'         `--.       /     \ \n"
                  "|      /       )'-.         .-'(       \      | \n"
                  "; ,   <__..-(   '-.)       (.-'   )-..__>   , ; \n"
                  " \ \-.__)    ``--._)       (_.--``    (__.-/ / \n"
                  "  '.'-.__.-.                       .-.__.-'.' \n"
                  "    '-...-'                        '-...-' \n")
            print("A wall of kitties doesn't allow you to go North.\nBut that "
                  "doesn't make you mad... You can't be mad at kitties, "
                  "rite?!\n")
            return False
        return True
