from weatbag import words
import random 

class Tile:
    def __init__(self):
        self.enemy_dead = False
        self.enemy_life = 2
    
    def describe(self):
        if not self.enemy_dead: 
            print("You encounter an orc! He's got a mean look, but you're a "
                "strong one. You should be able to take him. Attack or flee?")
        else: 
            print("You see an orc corpse here.")


    def enemy_swing(self, player): 
        if self.enemy_dead: 
            return
        print("The enemy takes a swing at you!")
        hit = random.choice((True,False))
        if hit: 
            print("He hits you!")
            player.hit_points -= 1
            self.report_player_state(player)
        else: 
            print("He misses!")

    def player_swing(self, player): 
        hit = random.choice((True,False))
        if hit: 
            print("You hit him!")
            self.enemy_life -= 1
        else: 
            print("You miss!")

        if self.enemy_life == 0: 
            print("You have killed the orc!")
            self.enemy_dead = True

    def report_player_state(self, player): 
        print("You are %s" % (player.state_string()))
    
    def leave(self, player, direction):
        if direction =='w':
            print("Cave wall this way.")
            return False
        elif not self.enemy_dead: 
            if not random.choice((True,False)): 
                print("The orc blocks your way!")
                self.enemy_swing(player)
                return False
            else: 
                print("You manage to flee!")
                return True
        return True

    no_path_msg = "There is no path leading in that direction."
    
    def action(self, player, do):
        if do[0] == "flee":
            self.leave(player, 's')
            return

        if do[0] in words.attack: 
            self.player_swing(player)
            self.enemy_swing(player)
        elif do[0] in words.use and do[1]=="berries":
            if player.has("berries"):
                player.take("berries")
                player.hit_points += 2
                if player.hit_points > player.MAX_HIT_POINT:
                    player.hit_points = player.MAX_HIT_POINT
                print("You ate the berries and feel better now.")
            else:
                print("Sorry you don't have any berries.")
        else:
            print("Sorry, I don't understand")
