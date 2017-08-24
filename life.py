# This is a simple Python implementation of the "Game of Life", a cellular automaton devised by the British mathematician John Horton Conway in 1970.

# The "game" is a zero-player game, meaning that its evolution is determined by its initial state, requiring no further input. One interacts with the Game of Life by creating an initial configuration and observing how it evolves.

# The universe of the Game of Life is an infinite two-dimensional orthogonal grid of square cells, each of which is in one of two possible states, alive or dead, or "populated" or "unpopulated". Every cell interacts with its eight neighbours, which are the cells that are horizontally, vertically, or diagonally adjacent. At each step in time, the following transitions occur:

# 1. Any live cell with fewer than two live neighbours dies, as if caused by underpopulation.
# 2. Any live cell with two or three live neighbours lives on to the next generation.
# 3. Any live cell with more than three live neighbours dies, as if by overpopulation.
# 4. Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.

# The initial pattern constitutes the seed of the system. The first generation is created by applying the above rules simultaneously to every cell in the seed-births and deaths occur simultaneously, and the discrete moment at which this happens is sometimes called a tick (in other words, each generation is a pure function of the preceding one). The rules continue to be applied repeatedly to create further generations.

import numpy

# Core function for modelling game rules given a state matrix
def live( state ):
    # Rule 2
    newstate = state.copy()

    rows, cols = state.shape
    for r in range( rows ):
        for c in range( cols ):
            # Compute neighbouring cells
            neighbours = numpy.sum( state[ max( r-1, 0 ):min( r+2, rows ), max( c-1, 0 ):min( c+2, cols ) ] ) - state[ r, c ]

            # Rules 1 and 3
            if state[ r, c ] and ( neighbours < 2 or neighbours > 3 ):
                newstate[ r, c ] = 0
            # Rule 4
            elif not state[ r, c] and neighbours == 3:
                newstate[ r, c ] = 1

    return( newstate )

# Game constraints
life = numpy.zeros( (6, 6), dtype=numpy.byte )
life[2, 1:5] = 1

# Life evolution
for i in range( 100 ):
    print( life )
    life = live( life )
