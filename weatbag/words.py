"""A thesaurus of words the player might use, so you can easily accept
synonyms of the word you want.

e.g. This will recognise take, pick, get or collect::

    if do[0] in weatbag.words.take:
        #...
"""

move = {'move','walk','go'}
give = {'give', 'feed', 'present'}
use = {'eat', 'use', 'wear'}
fight = {'fight', 'kill', 'hit', 'attack'}
drop = {'drop'}
take = {'pick', 'take', 'get', 'collect'}
look = {'look', 'inspect', 'examine'}
attack = {'attack', 'swing', 'hit', 'punch', 'fight'}
inventory = {'inventory', 'possessions', 'belongings', 'bag'}
surroundings = {'surroundings', 'around', 'scenery'}

prepositions = {'up', 'down', 'on', 'under', 'in', 'at', 'to'}
