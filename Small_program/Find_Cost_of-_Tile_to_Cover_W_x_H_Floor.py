import math

"""
Find Cost of Tile to Cover W x H Floor – 
Calculate the total cost of tile it would take to cover a floor plan of 
width and height, using a cost entered by the user.
"""

def tile_cost():
    room_width = int(input('Please enter room width in cm: '))
    room_high = int(input('Please enter room width in cm: '))
    tile_size = int(input('Please enter tile size in cm: '))
    tile_cost = int(input('Please enter cost of one tile: '))

    room_area = room_high*room_width
    tile_area = tile_size**2
    tile_amount = room_area/tile_area
    total_cost = (math.ceil(tile_amount)*tile_cost)

    print(f'Total cost of titles is equl to: {total_cost}')

tile_cost()