from weatbag import words

class Tile:
  def __init__(self):
    self.short_man_gone = False
    self.short_man_life = 2
    self.pants_on_fire = False

  def describe(self):
    print( "You reach the top of the hill and look around the rock "
           "formations. You find nothing but dust, a mud puddle, and" 
           "withered shrubs.\n")
    if not self.short_man_gone:
      self.pants_on_fire = True
      print( "Just as you are returning to the path, a ball of fire "
             "hurtles through the air and explodes at your feet, setting "
             "your pants on fire. You hear high pitched cackling and "
             "snorting.\n")
    else:
      print( "You see the charred ground, "
             "reminding you of your encounter with the short man who set "
             "your pants on fire. That was a close one. There is a steep "
             "path leading down the hill to the North. To the south, the "
             "hiltop path continues.\n")
  

  def action(self, player, do):
    if self.pants_on_fire:
      self.action_pants_on_fire(player, do)

    elif not self.short_man_gone:
      self.action_short_man(player, do)

    elif self.short_man_gone:
      print("I'm sorry, I don't understand.")
      
    
        
  def action_pants_on_fire(self, player, do):             
    if do.count('roll') > 0: 
       self.pants_on_fire = False
       print("Wisely following the teachings of your elders, you freeze, "
             "drop to the ground and roll around until the fire is "
             "extinguished. Covered in dirt and pants in tatters, you "
             "stand up and face your assailant, a short man.") 
    elif do.count('puddle') > 0:
      self.pants_on_fire = False
      print("You dash over the the mud puddle and splash water on your "
            "legs until the fire is quenched. Covered in mud and pants "
            "in taters, you stand up and face your assailant, a short man.")
    else:
      print("You had better find a way to put out this fire. Your legs "
            "are beginning to burn!")
    

  def action_short_man(self, player, do):
    print("Not done yet.")
    return

        
