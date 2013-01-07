#!/usr/bin/env python3
import sys
from importlib import import_module
from weatbag import Player, interact, name_to_coords

if len(sys.argv) != 2:
    print("Usage: ./test_tile.py <tile module>")
    print("E.g. : ./test_tile.py n2")
    sys.exit()

player = Player('Test player')
player.position = name_to_coords(sys.argv[1])

mod = import_module('weatbag.tiles.' + sys.argv[1])
if hasattr(mod, 'test_items'):
    player.inventory.update(mod.test_items)
    print("You have test items:")
    for item, n in player.inventory.most_common():
        if n < 1:
            break
        print(item, '(%d)' % n)
    print()

interact(player)

