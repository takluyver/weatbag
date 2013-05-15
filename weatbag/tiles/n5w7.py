from weatbag import words

class Tile:
    def __init__(self):
        self.trapped = True

    def describe(self):
        if self.trapped:
            print("You are inside the light house. You hear a clicking sound and "
              "the door closes behind you.\nIt is dark, and an enormous cat "
              "sits on a computer compiling felinux kernels.\n"
              "You try to open the door and leave but you realize it is "
              "locked.\n"
              "The cat turns at you and hisses loudly.\n"
              "She grawls and because you now speak cat, you understand what "
              "she says.\n\n"
              "Puny human, how dare you disturb my peace!\n"
              "If you tell a lie I will hang you; if you tell the truth I will "
              "shoot you.\n\n"
              "It looks like you are condemned... Though if you think a bit "
              "more there is an apropriate answer that gets your ass out of "
              "this hell!\n")


    # The exact answer is 'You will hang me'. If she hang him, then the 
    # statement was true and she could only hang him for telling a lie. 
    # If she shoot him, then it makes the statement a lie and she was only 
    # to shoot him for telling the truth. 
    # An alternate solution is to say, "You will not shoot me," leading to the 
    # same quandary for the killercat.


    def action(self, player, do):
        if self.trapped:
            if do[0]=="you" and do[1]=="will" and do[2]=="hang" and do[3]=="me":
                print("You dirty little human, I can only let you go now!\n")
                self.trapped = False
            elif do[0]=="you" and do[1]=="will" and do[2]=="not" and do[3]=="shoot" and do[4]=="me":
                print("You dirty little human, I can only let you go now!\n")
                self.trapped = False
            else:
                print("Keep saying bullshit and your end is close!")
        else:
            print("I don't understand.")
        
#lighthouse
