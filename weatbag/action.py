import sys
from . import words

def get_action():
    """Prompts for an action, splits it into words, and removes any prepositions.
    
    movement actions will be represented by the move token object in this module,
    followed by a one-letter direction.
    """
    action = []
    while len(action) == 0:
        action = input('> ').lower().split()
    for prep in words.prepositions.intersection(action):
        action.remove(prep)
    

        # Look around
        return look_around
    

        return (move, action[1][0])
    return action

move_directions = {'n','e','s','w','north','east','south','west'}

def is_move(do):
    return len(do) == 2 and (do[0] in words.move) and (do[1] in move_directions)        

def handle_action(tile, player, do):
    if len(do) == 1 and do[0] == 'quit':
        sys.exit()
        
    elif len(do) == 2 and (do[0] in words.look) and (do[1] in words.surroundings):
        # Look around
        tile.describe()
    
    elif len(do) == 2 and (do[0] in words.look) and (do[1] in words.inventory):
        # Look at bag
        for item, n in inventory.most_common():
            if n < 1:
                break
            print(item, '(%d)' % n)
    
    else:
        tile.action(player, do)

def process_move(direction):
    direction = direction[0].lower()
    if direction == 'n':
        return (0, 1)
    if direction == 's':
        return (0, -1)
    if direction == 'w':
        return (-1, 0)
    if direction == 'e':
        return (1, 0)
    return (0, 0)
