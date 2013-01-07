from collections import Counter
from importlib import import_module
import re

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
            modname = 'weatbag.tiles.' + coords_to_name(*key)
            try:
                mod = import_module(modname)
            except ImportError:
                raise KeyError(key)
            
            tile = mod.Tile()
            self.tiles[key] = tile
            return tile

def coords_to_name(e, n):
    modname = ''
    if n > 0:
        modname += 'n'+str(n)
    elif n < 0:
        modname += 's'+str(abs(n))
    
    if e > 0:
        modname += 'e'+str(e)
    elif e < 0:
        modname += 'w'+str(abs(e))
    
    return modname

_tile_name_re = re.compile(r'([ns]\d+)?([ew]\d+)?')
def name_to_coords(tilename):
    ns, es = _tile_name_re.match(tilename).groups()
    if ns is None:
        n = 0
    elif ns[0] == 'n':
        n = int(ns[1:])
    else:
        n = -int(ns[1:])
    
    if es is None:
        e = 0
    elif es[0] == 'e':
        e = int(es[1:])
    else:
        e = -int(es[1:])
    
    return e, n

def main():
    name = input("What is your name? ")
    player = Player(name)
    interact(player)
    
def interact(player):
    world = World()
    tile = world[player.position]
    tile.describe()
    while True:
        do = action.get_action()
        if action.is_move(do):
            direction = do[1][0].lower()
            # check if we can leave tile
            if not getattr(tile, 'leave', lambda p,d: True)(player, direction):
                continue
            # move
            e,n = player.position
            de, dn = action.move_coords[direction]
            new_posn = e+de, n+dn
            try:
                tile = world[new_posn]
            except KeyError:
                print("The undergrowth in that direction is impassable. "
                      "You turn back.")
            else:
                player.position = new_posn
                tile.describe()
        else:
            action.handle_action(tile, player, do)

