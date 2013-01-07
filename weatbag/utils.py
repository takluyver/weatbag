"""Utility functions for the game."""

def transfer(item, from_collection, to_collection, n=1):
    """Move an item from one dictionary of objects to another.
    
    Returns True if the item was successfully transferred, False if it's not in
    from_collection.
    
    For example, to have the player pick up a pointy stick::
    
        if transfer('pointy stick', tile.contents, player.inventory):
            print("You take the stick.")
        else:
            print("There's no stick here.")
    """
    if from_collection.get(item, 0) < n:
        return False
    from_collection[item] -= n
    if item in to_collection:
        to_collection[item] += n
    else:
        to_collection[item] = n
    return True
