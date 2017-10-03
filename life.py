import numpy
import pygame
import time, sys, argparse
from pygame.locals import *

# Core function for modelling game rules given a state matrix
def live( state ):
    # Rule 2
    new_state = state.copy()

    rows, cols = state.shape
    for r in range( rows ):
        for c in range( cols ):
            # Compute neighbouring cells
            neighbours = numpy.sum( state[ max( r-1, 0 ):min( r+2, rows ), max( c-1, 0 ):min( c+2, cols ) ] ) - state[ r, c ]

            # Rules 1 and 3
            if state[ r, c ] and ( neighbours < 2 or neighbours > 3 ):
                new_state[ r, c ] = 0
            # Rule 4
            elif not state[ r, c] and neighbours == 3:
                new_state[ r, c ] = 1

    return( new_state )

def setup_game( width, height, tilesize, board ):
    initial_life = numpy.zeros( (height, width), dtype=numpy.byte )

    done = False
    while done == False:
        for event in pygame.event.get():

            # Capture mouse events until return key is pressed
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    done = True

            # Mark/unmark grid cell with mouse interaction
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                column = pos[0] // tilesize
                row = pos[1] // tilesize
                initial_life[ row ][ column ] = not initial_life[ row ][ column ]

        plot( initial_life, board, tilesize)

    return initial_life

def plot( state, board, tilesize ):
    rows, cols = state.shape
    for r in range( rows ):
        for c in range( cols ):
            if state[ r, c ]:
                pygame.draw.rect( board, ( 0,0,0 ), ( c*tilesize, r*tilesize, tilesize, tilesize ) )
            else:
                pygame.draw.rect( board, ( 255,255,255 ), ( c*tilesize, r*tilesize, tilesize, tilesize ) )
    
    pygame.display.update()

# Game constraints
parser = argparse.ArgumentParser( description='yaglib' )
parser.add_argument( '--cellsize', help='Pixel size for each grid cell', dest='cellsize', action='store', type=int, default=5 )
parser.add_argument( '--gridwidth', help='Width for cells grid', dest='gridwidth', action='store', type=int, default=120 )
parser.add_argument( '--gridheight', help='Height for cells grid', dest='gridheight', action='store', type=int, default=120 )
args = parser.parse_args()

tilesize = args.cellsize
width = args.gridwidth
height = args.gridheight

# Initialize pygame assets
pygame.init()
board = pygame.display.set_mode( ( width*tilesize, height*tilesize ) )

# Initialize game conditions
life = setup_game( width, height, tilesize, board )

# Life evolution
while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    time.sleep( 0.1 )

    plot( life, board, tilesize)
    life = live( life )
