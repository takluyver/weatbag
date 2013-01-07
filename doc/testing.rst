Testing tiles
=============

To save you repeatedly playing through the game to test your latest changes,
there's a script to skip to any given tile::

    ./test_tile.py n2

If the player needs specific items to test the tile, add a list called test_items
to the module. The test script will add these to the player's inventory. For
example, tile n2 defines::

    test_items = ['unlit torch']
