Other API components
====================

The player
----------

.. autoclass:: weatbag.Player
   :members: has, give, take

   .. attribute:: name
   
      The name given by the player when they started the game.

   .. attribute:: position
   
      The player's position in the world as (n, e) co-ordinates.

   .. attribute:: inventory
   
      A :class:`collections.Counter` storing the item's in the player's bag.

Understanding commands
----------------------

.. automodule:: weatbag.words

Combining items
---------------

To allow items to be combined to form other items, add a module in ``weatbag.items``
with the same name as one of the items, replacing spaces with underscores. There,
define a function called ``combine``, which will take the name of a second
object. You only need to define this for one object; the game will try to find
it for both objects being combined.

If the objects can be combined, it should describe what has happened, and return
a list of the new objects created. Otherwise, it should return ``None``. For
example, this function is in :mod:`weatbag.items.unlit_torch`::

    def combine(other):
        if other == 'match':
            print("The torch sputters into life.")
            return ['flaming torch']
        
        return None

Utility functions
-----------------

.. autofunction:: weatbag.utils.transfer

