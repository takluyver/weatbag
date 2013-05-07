#!/usr/bin/python3
"""Run this script to get a map of the whole game, to use when writing new
tiles.
"""
import os.path

from weatbag.map import show_map
from weatbag import World, name_to_coords
from weatbag.tiles import centre

tiledir = os.path.dirname(centre.__file__)

world = World()

for f in os.listdir(tiledir):
    coords = name_to_coords(f)
    if coords == (0, 0):
        continue
    world[coords]  # Load the tile

show_map(world.tiles)
