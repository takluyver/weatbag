
from weatbag import words

class Tile:
  
  def describe(self):
    print("The foliage begins to thin and the path winds forwards "
            "up a steep hillside. A rugged granite rockformation tops "
            "the hill, its centerpiece two slabs of rock leaning together "
            "to form a crude arch. Nondescript fields lie to the "
            "East and West.")

  def action(self, player, do):
      # Nothing to do here yet.
      print("Sorry, I don't understand")

  # Used for more colorfull invisible wall messages in leave.
  wrong_direction_counter = 0

  # Only allow movement to south, norht
  def leave(self, player, direction):
    if direction is 'e' or 'w':
      if self.wrong_direction_counter <=1 :
        print("There's nothing but non-descript fields over here. Better "
              "not leave the path.")
      else:
        print("You spend an hour wandering through the field and confirm that "
              "it is indeed nondescript. Upon returning to the path, the hilltop "
              "appears ever more alluring.")
      self.wrong_direction_counter += 1
      return False
    else:
      return True
