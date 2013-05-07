
from weatbag import words

class Tile:
    map_word = "Hill"
  
    def describe(self):
      print("To the South, the foliage begins to thin and the path winds "
          "forward up a steep hillside. A rugged granite rock formation tops "
          "the hill, its centerpiece two slabs of rock leaning together "
          "to form a crude arch." )
  
    def action(self, player, do):
        # Nothing to do here yet.
        print("Sorry, I don't understand")

      
    def leave(self, player, direction):
        restricted_directions = { 'e' }

        # I placed this restriction here to prevent 
        # early entrance to the bug quest
        # which should be started by going South from e1
        if direction in restricted_directions:
            print("The undergrowth in that direction "
                "is impassable. You turn back.")
            return False
        else:
            return True

