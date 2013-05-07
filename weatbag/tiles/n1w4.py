from weatbag.utils import transfer

class Tile:
    def __init__(self):
        self.contents = {'neko': 1}
        self.challenge_completed = False
        self.sequence = "1113213211"
        
    def describe(self):  
        if not self.challenge_completed:
            print("The rocks led you to a path uphill.\n*Poof* A purrr-sian "
                  "cat appears in front of you!\n")
            self.challenge()
        else:
            print("The rocks led you to a path uphill.\nIt's a little bit "
                  "windy and a flock of seagulls is flying above you.")

    def challenge(self):
        print("Meow good traveler! I have a question for you.\n"
              "You might as well go away and ignore me and my awesome fur but "
              "if you pass my little test I will reward you!\n\n"
              "Here is a series of numbers.\n"
              "What is the next number in the sequence?\n"
              "1\n"
              "11\n"
              "21\n"
              "1211\n"
              "111221\n"
              "312211\n"
              "13112221\n")              
        #The next number in the sequence is 1113213211, because the rule for 
        #creating the next number is to simply describe the previous number. 
        #The first number is 1, or 1 (one) 1, so you get 11. 
        #To describe 11, you have two 1's, or 21. Now you have one 2 and one 1, 
        #so the next number is 1211. The solution is to simply continue 
        #describing the previous number using only numbers.\n")
        
    def action(self, player, do):
        if not self.challenge_completed:
            if do[0] == self.sequence:
                print("You are a clever human, aren't you?!\n\n"
                      "Here is my offering. I give you this maneki-neko.\n"
                      "If you ever come across a wall of kittens and you want "
                      "them to let you pass you will use this lucky charm!")                      
                #https://en.wikipedia.org/wiki/Maneki-neko
                self.contents['neko'] -= 1
                player.give('neko')
                self.challenge_completed = True
            else:
                print("Wut? Try h4rd3r st00p3d hum4n!")
        else:
            print("I don't understand...")
            
    def leave(self, player, direction):
        if direction == "s":
            print("Oh dear Basdet! You can't go north, you will fall of the "
                   "cliff!\n")
            return False
        elif direction == "n":
            print("It looks like the side of a wooden hut.\n"
                  "Since you don't walk though walls (yet) "
                  "you can't go there.\n")
            return False
        else:
            return True
