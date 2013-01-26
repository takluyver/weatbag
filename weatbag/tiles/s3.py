from weatbag import words

class Tile:
  def __init__(self):
    self.short_man_here = True
    self.pants_on_fire = False
    self.talk_or_fight = None

  def describe(self):
    print( "You reach the top of the hill and look around the rock "
           "formations. You find nothing but dust, a mud puddle, and" 
           "withered shrubs.\n")
    if self.short_man_here:
      self.pants_on_fire = True
      print( "Just as you are returning to the path, a ball of fire "
             "hurtles through the air and explodes at your feet, setting "
             "one of your pant legs on fire. You hear high pitched cackling and "
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

    elif self.short_man_here:
      self.action_short_man(player, do)

    elif self.short_man_gone:
      print("I'm sorry, I don't understand.")

  def leave(self, player, direction):
    if self.pants_on_fire:
      print("Running now will only feed the fire!")
      return False
    elif self.short_man_here:
      print("This fellow is dangerous. I better not turn my back on him.")
      return False
    else:
      return True
    
        
  def action_pants_on_fire(self, player, do):             
    if 'roll' in do:
       self.pants_on_fire = False
       print("Wisely following the teachings of your elders, you freeze, "
             "drop to the ground and roll around until the fire is "
             "extinguished. Covered in dirt and pantleg in tatters, you "
             "stand up and face your assailant, a rather short man "
            "with pale skin and bushy orange hair."
             "Do you talk to him or rush him?")

    elif 'puddle' in do:
      self.pants_on_fire = False
      print("You dash over the the mud puddle and splash water on your "
            "legs until the fire is quenched. Covered in mud and pantleg"
            "in taters, you stand up and face your assailant, a rather short man "
            "with pale skin and bushy orange hair."
            "Do you talk to him or attack him?")
    else:
      print("You had better find a way to put out this fire. Your legs "
            "are beginning to burn!")
    

  def action_short_man(self, player, do):
    if do[0] in words.attack:
      print("Not one to be played around with, you charge the man. His amusement "
            "quickly turns to surprise and then fear as your size and "
            "determination become apparent. The man stumbles backwards and emits "
            "a yelp. Just before he hits the groud there is a dry popping noise "
            "a flash of light and the man is gone. ")
    elif do[0] in words.talk:
      print("\"What the hell was that?\" you growl.\n"
            "The man jumps deftly onto a boulder, looks at you over his "
            "shoulder for just a moment, and then jumps out of sight. "
            "You quickly climb after him, but he has somehow disappeared.")
    self.short_man_here = False

        






