"""A thesaurus of words the player might use, so you can easily accept
synonyms of the word you want.

e.g. This will recognise take, pick, get or collect::

    if do[0] in weatbag.words.take:
        #...
"""
# Verbs
move = {'move', 'walk', 'go', 'travel', 'cross', 'pace', 'traverse'}
give = {'give', 'feed', 'present', 'impart', 'pass'}
use = {'eat', 'use', 'wear', 'utilise'}
fight = {'fight', 'kill', 'hit', 'attack', 'afflict'}
drop = {'drop', 'unload'}
take = {'pick', 'take', 'get', 'collect', 'occupy', 'acquire', 'adopt', 'withdraw'}
look = {'look', 'inspect', 'examine', 'search', 'check'}
attack = {'attack', 'swing', 'hit', 'punch', 'kick', 'fight'}
combine = {'combine', 'join', 'mix', 'unite', 'compound', 'aggregate', 'blend', 'coalesce', 'meld'}
talk = {'talk', 'speak', 'converse'}

# Nouns
inventory = {'inventory', 'possessions', 'belongings', 'bag'}
surroundings = {'surroundings', 'around', 'scenery'}

# Prepositions
prepositions = {'up', 'down', 'on', 'under', 'in', 'at', 'to', 'with', 'and'}

# Yes/No
yes = {'yes', 'y', 'yup', 'ye'}
no = {'no', 'n', 'nope'}

# Control
instructions = {'instructions', 'help', '?', 'tutorial'}
exit = {'exit', 'quit'}
