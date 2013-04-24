class Tile:
    def describe(self):
        print("The beach is quiet. On the south are children playing.\n")
    
    def action(self, player, do):
        print("wo0t w0ot?! o_O")
        
    def leave(self, player, direction):
        if direction == 'w':
            print("I'm afraid you can't go west.\nThe sea on that part is "
                  "fool of electric eels and you don't have a transport.\n")
            return False
        elif direction == 'e':
            print("There is the side of a cave in front of you.\nYou can't go "
                  "east.\n")
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
