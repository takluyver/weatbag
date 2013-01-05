The Tile Interface
==================

Module name
-----------

Your tile will have a module name such as ``weatbag.tiles.s3e11``, which
determines its position on the grid. The co-ordinates use compass directions: n/s
followed by e/w. If one co-ordinate is 0, it should be left out. So the tiles
around the centre are named:

+------+------+-------+------+------+
| n2w2 | n2w1 | n2    | n2e1 | n2e2 |
+------+------+-------+------+------+
| n1w2 | n1w1 | n1    | n1e1 | n1e2 |
+------+------+-------+------+------+
| w2   | w1   | centre| e1   | e2   |
+------+------+-------+------+------+
| s1w2 | s1w1 | s1    | s1e1 | s1e2 |
+------+------+-------+------+------+
| s2w2 | s2w1 | s2    | s2e1 | s2e2 |
+------+------+-------+------+------+

The Tile class
--------------

Your module should define a class called ``Tile``, with the following interface:

.. class:: Tile()

   .. method:: describe()
   
      Describe the scene and anything in it. This is called when the player
      enters the tile, and again if they look around.

   .. method:: action(player, do)
   
      Called when the player does something inside the tile. You need to
      interpret the action and carry it out.
      
      :param player: the active :class:`~weatbag.Player` instance
      :param action: list of strings - the player's input, split up into words,
                     lowercase and with prepositions removed

   .. method:: leave(player, direction)
   
      *Optional.* Called when the player tries to leave the square. To let them
      leave, return `True`, or to prevent them, print an explanation and return
      `False`. If the method isn't found, the player can always leave.
      
      :param player: the active :class:`~weatbag.Player` instance
      :param direction: the direction the player is trying to leave, as a single
                        lowercase character, n/e/s/w
      explanation
