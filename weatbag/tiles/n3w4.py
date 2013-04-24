class Tile:
   def describe(self):
       print("\nLooks like you are in a walking mood because you still follow "
       "the path.\nYou hear birds singing, some small waves on the background, "
       "there is a nice flowery smell, rays of sun make the tree sceenery "
       "heavenly...\nI totaly get you, it's a nice path to have a walk!")
                   
   def action(self, player, do):
       print("\nSorry, I don't understand")
       
   def leave(self, player, direction):
       if direction == "n":
           print("No trespasing. Violators will vanish without a trace.\n")
           return False
       elif direction == "w":
           print("No trespasing. Violators will vanish without a trace.\n")
           return False
       else:
           return True
