from collections import Counter
from importlib import import_module

from . import action

class Player:
    def __init__(self, name):
        self.name = name
        self.inventory = Counter()
        self.position = (0,0)
    
    def has(self, item):
        "Does the player have any of item?"
        return self.inventory[item] > 0
    
    def give(self, item, n=1):
        "Put the item in the player's inventory."
        self.inventory.update([item]*n)
    
    def take(self, item, n=1):
        "Remove an item from the inventory. Raises KeyError if item isn't there."
        if self.inventory[item] >= n:
            self.inventory[item] -= n
        else:
            raise KeyError(item)

class World:
    def __init__(self):
        self.tiles = {}
        from .tiles import centre
        self.tiles[(0,0)] = centre.Tile()
    
    def __getitem__(self, key):
        try:
            return self.tiles[key]
        except KeyError:
            n,e = key
            modname = 'weatbag.tiles.'
            if n > 0:
                modname += 'n'+str(n)
            elif n < 0:
                modname += 's'+str(abs(n))
            
            if e > 0:
                modname += 'e'+str(n)
            elif n < 0:
                modname += 'w'+str(abs(n))
            
            try:
                mod = import_module(modname)
            except ImportError:
                raise KeyError(key)
            
            tile = mod.Tile()
            self.tiles[key] = tile
            return tile

def main():
    name = input("What is your name? ")
    player = Player(name)
    world = World()
    tile = world[0,0]
    while True:
        tile.describe()
        while True:
            do = action.get_action()
            if action.is_move(do):
                # check if we can leave tile
                if not getattr(tile, 'leave', lambda p,d: True)(player, do[1]):
                    continue
                # move
                n,e = player.position
                dn, de = action.process_move(do[1])
                new_posn = n+dn, e+de
                try:
                    tile = world[new_posn]
                except KeyError:
                    print("The undergrowth in that direction is impassable. "
                          "You turn back.")
            else:
                action.handle_action(tile, player, do)

