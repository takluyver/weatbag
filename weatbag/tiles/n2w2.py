class Tile:
   def describe(self):
       print("\nYou are now on the island. In front of you there are some trees "
       "and a small path.\nFeeling adventurous?")
   
   def action(self, player, do):
       print("Sorry, I don't understand")
       
   def leave(self, player, direction):
       if direction == "e":
           print ("\nYou can't go back by swimming, that part is full of "
                "electric eels.")
           return False
       else:
           return True
