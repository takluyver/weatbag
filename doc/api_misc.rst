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

Utility functions
-----------------

.. autofunction:: weatbag.utils.transfer

