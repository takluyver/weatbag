from weatbag import words

class Tile:
    map_word = "Lighthouse"
    
    def __init__(self):
        self.trapped = True

    def describe(self):
        if self.trapped:
            print("You are inside the lighthouse. You hear a clicking sound and "
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
              "more there is an appropriate answer that gets your ass out of "
              "this hell!\n")

    # The exact answer is 'You will hang me'. If she hangs him, then the
    # statement was true and she could only hang him for telling a lie. 
    # If she shoot him, then it makes the statement a lie and she was only
    # to shoot him for telling the truth.
    # An alternate solution is to say, "You will not shoot me," leading to the
    # same quandary for the killercat.
         
        else:
            print("You are inside the lighthouse. There's a computer in a "
                  "corner and some printed papers on the ground with "
                  "scribblings like:\n\n"
                  "SO IM LIKE FIBBING WIT N OK?\n"
                  "    LOL ITERATE FIBONACCI TERMS LESS THAN N /LOL\n"
                  "    SO GOOD N BIG LIKE EASTERBUNNY\n"
                  "    BTW, FIBONACCI LIKE BUNNIES! LOL\n"
                  "    U BORROW CHEEZBURGER\n"
                  "    U BORROW CHEEZBURGER\n"
                  "    I CAN HAZ CHEEZBURGER\n"
                  "    HE CAN HAZ CHEEZBURGER\n"
                  "    WHILE I CUTE?\n"
                  "        I AND HE CAN HAZ HE AND I ALONG WITH HE\n"
                  "        IZ HE BIG LIKE N?\n"
                  "            KTHXBYE\n"
                  "        U BORROW HE\n\n"
                  "Ah huh you think... lolpython fibonacci. Crazy catworks. "
                  "Nothing to do here!\n")

# http://www.dalkescientific.com/writings/diary/archive/2007/06/01/lolpython.html

    def action(self, player, do):
        if self.trapped:
            if do == ["you","will","hang","me"]:
                print("You dirty little human, I can only let you go now!\n")
                self.trapped = False
            elif do == ["you","will","not","shoot","me"]:
                print("You dirty little human, I can only let you go now!\n")
                self.trapped = False
            elif player.has("catfood") and (do[0] in words.use or do[0] in words.give) and "catfood" in do:
                print("Do you think that if you bribe me with catfood I'll let "
                      "you leave?\nCatfood will not save you this time.\n"
                      "The fat cat steals one catfood and eats it. You should "
                      "be more carefull next time.")
                player.take("catfood")
                self.trapped = False
            else:
                print("Keep saying bullshit and your end is close!")
        else:
            print("I don't understand.")
            
    def leave(self, player, direction):
        if self.trapped and direction in ("w", "n"):
            print("You are my prisoner, I won't let you leave. But even if you "
                  "could leave these are the inner walls of the lighthouse you "
                  "idiot! And then the sea.")
            return False
        elif self.trapped and direction in ("e", "s"):
            print("What do you think you are doing? I won't let you leave. "
                  "You are my prisoner!")
            return False
        elif direction in ("w", "n"):
            print("It's the lighthouse walls. What are you gonna do? "
                  "Hit your head on them?")
            return False
        else:
            print("You are out!")
            return True
           
test_items = ["catfood"]
