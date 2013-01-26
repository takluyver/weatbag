import sys
from . import words
from weatbag.items import combine

def get_action():
    """Prompts for an action, splits it into words, and removes any prepositions.

    movement actions will be represented by the move token object in this module,
    followed by a one-letter direction.
    """
    action = []
    while len(action) == 0:
        action = input('> ').lower().split()
        action = [w for w in action if w not in words.prepositions]
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
        for item, n in player.inventory.most_common():
            if n < 1:
                break
            print(item, '(%d)' % n)
    
    elif len(do) >= 3 and (do[0] in words.combine):
        for split in range(2, len(do)):
            item1 = ' '.join(do[1:split])
            item2 = ' '.join(do[split:])
            if player.has(item1):
                if player.has(item2):
                    results = combine(item1, item2)
                    if results is not None:
                        player.take(item1)
                        player.take(item2)
                        player.inventory.update(results)
                    else:
                        print("You can't combine {} with {}".format(item1, item2))
                
                else:
                    print("You don't have a {}".format(item2))
                
                return
            
            elif player.has(item2):
                print("You don't have a {}".format(item1))
                return
            
        else:
            print("You don't have those items.")
    
    else:
        tile.action(player, do)

move_coords = {
    'n': (0,  1),
    's': (0, -1),
    'w': (-1, 0),
    'e': (1,  0)
}
